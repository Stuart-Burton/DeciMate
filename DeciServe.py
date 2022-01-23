#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import decimctl

log_raw_data = False

def device_list():
    devices = decimctl.list_devices()
    device_text = ""
    if not devices:
        device_text = "<p>No devices found</p>"
    for manufacturer, desc, serial in devices:
        device_text = device_text + ("<p>%s Model: %s Serial: %s</p>" % (manufacturer, desc, serial))
    return device_text

def device_status(serial):
    device_text = ""
    status = decimctl.Device(log_raw_data, serial)
    stat_text = str(status.registers).split(";\n")
    for item in stat_text:
        item = item.replace("<", "[")
        item = item.replace(">", "]")
        device_text = device_text +"<p>"+ str(item) + "</p>"
    status.close()
    return device_text


def device_param_set(deci_serial, deci_param, deci_param_var):
    device = decimctl.Device(log_raw_data, deci_serial)
    device.open()
    setattr(device.registers, deci_param, int(deci_param_var))
    stat_text = ("Decimator %s %s set to %s\n"% (deci_serial, deci_param, deci_param_var))
    device.close()
    return stat_text


def parse_path(path_var):
    path_var = path_var.strip("/").split("/")
    print("Parse_Path entry ",path_var)
    html_text = ""
    if path_var[0] == "list":
        html_text = device_list()
        # print(html_text)
    elif path_var[0] == "status":
        ser_num = path_var[1]
        html_text = device_status(ser_num)
    elif path_var[0] == "set":
        deci_serial = path_var[1]
        deci_param = path_var[2]
        deci_param_var = path_var[3]
        html_text = device_param_set(deci_serial, deci_param, deci_param_var)
    else:
        html_text = "<p>Path not understood, retry?</p>"
    return html_text

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        path_var = str(self.path)
        self._set_response()
        html_text = parse_path(path_var)
        # print("Returned text ",html_text)

        self.wfile.write("{}".format(html_text).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
