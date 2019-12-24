# TODO: Build other version support.

import os
import urllib.request
import serial.tools.list_ports

def get_ports():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    return connected

print('Installing tools...')
os.system('pip install esptool')
os.system('pip install adafruit-ampy')
print('')
print('Getting ESP32 microPython firmware...')
print('Note, this is the Bluetooth not LAN version.')
urllib.request.urlretrieve('https://micropython.org/resources/firmware/esp32spiram-idf4-20191224-v1.12-5-g42e45bd69.bin', os.getcwd() + '/firmware.bin')

ports = get_ports()

print('Select port connected to ESP32:')
port_index = 0
for port in ports:
    print(f'    {port_index}: {port}')
    port_index += 1
port_num = int(input())

print('Installing firmware.')
input('Please be sure the upload button is pressed and hit a key to continue.')
os.system(f'esptool.py --chip esp32 --port {ports[port_num]} write_flash -z 0x1000 firmware.bin')

print('Creating WiFi credentials file.')
ssid = input('WiFi SSID name? ')
pswd = input('WiFi password? ')
with open('wifi_creds.txt', 'w') as f:
    f.write(f'ssid={ssid}\n')
    f.write(f'password={pswd}')

print('Installing credentials to the ESP32 at /wifi_creds.txt')
os.system(f'ampy -d 1 -p {ports[port_num]} put wifi_creds.txt')
