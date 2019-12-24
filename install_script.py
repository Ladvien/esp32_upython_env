import os
import argparse
import serial.tools.list_ports

parser = argparse.ArgumentParser()
parser.add_argument('-f', help = 'Filename to upload.') 
args = parser.parse_args()

def get_ports():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    return connected


ports = get_ports()

print('Select port connected to ESP32:')
port_index = 0
for port in ports:
    print(f'    {port_index}: {port}')
    port_index += 1
port_num = int(input())

os.system(f'ampy -d 1 -p {ports[port_num]} put {args.f}')
print(f'Finished installing {args.f}')
print('Attempting to start program...')
os.system(f'ampy -d 1 -p {ports[port_num]} run {args.f}')
print(f'Started running {args.f}')

