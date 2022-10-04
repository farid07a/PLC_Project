import snap7
# Snap7 client used for connection to a siemens 7 server.
client = snap7.client.Client()
client.connect("127.0.0.1", 0, 0, 1012)
client.get_connected()


