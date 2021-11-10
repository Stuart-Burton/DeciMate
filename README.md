# DeciMate
Please note this is experimental code with little to no error checking used at your own risk.
I will not be held responsible for any bricking of Decimators or any other failure as a result of using this code.
This python script for raspberry pi makes use of the python module at https://github.com/quentinmit/decimctl
It provides a very basic HTTP server which makes use of HTTP GET requests to control Decimator Design products.

Installation is a matter of installing the DeciServe.py script and the decimctl module folder to the same folder.
Run DeciServe.py as sudo to provide access to USB

Commands are issued in the following ways:
http://<address-of-pi>/list  # lists Decimator products connected to USB
Example: http://192.168.1.1/list

http://<address-of-pi>/status/<serial-number>  # lists status of Decimator <serial-number>
Example: http://192.168.1.1/status/CPC10934

http://<address-of-pi>/set/<serial-number>/<parameter>/<parameter-value>
Example: http://192.168.1.1/set/CPC10934/SO_Source/1  # Set SDI output to HDMI input

This has been tested with Companion 2.1.3 and a single Decimator Design MD-CROSS V2

  
