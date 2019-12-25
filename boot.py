import time
import webrepl
from auto_wifi import auto_wifi

# Initialize WiFi.
sta_if = auto_wifi()

while not sta_if.isconnected():
    print('Waiting for WiFi connection...')
    time.sleep(2)
    
# Start Web Repl.
webrepl.start()
ip = sta_if.ifconfig()[0]
print('You can access the WebREPL at http://micropython.org/webrepl/#{0}:8266'.format(ip))