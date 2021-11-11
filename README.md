# DeciMate for Raspberry Pi
<p>Please note this is experimental code with little to no error checking used at your own risk.</p>
<p>I will not be held responsible for any bricking of Decimators or any other failure as a result of using this code.</p>
<p>This python script for raspberry pi makes use of the python module at https://github.com/quentinmit/decimctl</p>
<p>It provides a very basic HTTP server which makes use of HTTP GET requests to control Decimator Design products.</p>

<p>Installation is a matter of installing the DeciServe.py script and the decimctl module folder to the same folder.</p>
<p>Run DeciServe.py as sudo to provide access to USB</p>

<p>Commands are issued in the following ways:</p>
<p>http://address-of-pi:8080/list  # lists Decimator products connected to USB</p>
<p>Example: http://192.168.1.1:8080/list</p>

<p>http://address-of-pi:8080/status/serial-number  # lists status of Decimator serial-number</p>
<p>Example: http://192.168.1.1:8080/status/CPC10934</p>

<p>Use Companion generic HTTP GET to issue commands</P>
<p>http://address-of-pi:8080/set/serial-number/parameter/parameter-value</p>
<p>Example: http://192.168.1.1:8080/set/CPC10934/SO_Source/1  # Set SDI output of CPC10934 to HDMI input</p>

<p>This has been tested with Companion 2.1.3 and a single Decimator Design MD-CROSS V2</p>

  
