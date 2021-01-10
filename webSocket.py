from microWebSrv import MicroWebSrv
import utime
import network

STA_SSID= 'Estare' 
STA_PSK= 'xerox38*'

def do_connect():
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active(): ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not ap_if.active(): sta_if.active(True)
    if not sta_if.isconnected(): sta_if.connect(STA_SSID, STA_PSK)

    sta_if.connect(STA_SSID, STA_PSK)

do_connect()


wsflag = False

def _acceptWebSocketCallback(webSocket, httpClient) :
  print("WS ACCEPT")
  webSocket.RecvTextCallback   = _recvTextCallback
  webSocket.RecvBinaryCallback = _recvBinaryCallback
  webSocket.ClosedCallback     = _closedCallback

def _recvTextCallback(webSocket, msg) :
  print("WS RECV TEXT : %s" % msg)
  webSocket.SendText("Reply for %s" % msg+ str(t))
  global wsflag
  global ws
  ws = webSocket
  wsflag = True

def _recvBinaryCallback(webSocket, data) :
  print("WS RECV DATA : %s" % data)

def _closedCallback(webSocket) :
  print("WS CLOSED")
  

mws = MicroWebSrv()                                    # TCP port 80 and files in /flash/www
mws.MaxWebSocketRecvLen     = 256                      # Default is set to 1024
mws.WebSocketThreaded       = False                    # WebSockets without new threads
mws.AcceptWebSocketCallback = _acceptWebSocketCallback# Function to receive WebSockets
mws.Start() 

t=0
while not wsflag : pass 

while True:
  print(t)
  if  not ws.IsClosed() : ws.SendText(str(t))
  utime.sleep_ms(100)
  t+=1


