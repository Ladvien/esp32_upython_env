def auto_wifi():
    import network
    import uos
    import time
    def exists(file_name):
        try:
            uos.stat(file_name)
            return True
        except OSError:
            return False

    # File containing wifi credentials.
    wifi_cred_filename = 'wifi_creds.txt'
    # Get an interface object.
    sta_if = network.WLAN(network.STA_IF)
    # Activate the interface.
    sta_if.active(True)
    # Make sure it is active.
    print('Interface active: {0}'.format(sta_if.active()))

    # Get credentials from file on ESP32.
    print('Looking for credentials')
    if exists(wifi_cred_filename):
        print('Found WiFi credential file.')    
        with open(wifi_cred_filename) as f:
            file_lines = f.readlines()

        ssid = file_lines[0].replace('\n', '').replace('ssid=', '')
        pswd = file_lines[1].replace('\n', '').replace('password=', '')

        if ssid == '' or pswd == '':
            print('Credentials not found in /wifi_creds.txt.')
            quit()
        else:
            # Show the credentials found
            print('SSID:       {0}'.format(ssid))
            print('Password:   {0}'.format(pswd))
    else:
        print('No WiFi credentials were found.  Please run "tools_setup.py".')
        quit()

    # Attempt to connect
    sta_if.connect(ssid, pswd)

    # Check IPs
    time.sleep(4)
    print(sta_if.isconnected())

