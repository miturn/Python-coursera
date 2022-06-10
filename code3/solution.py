import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    num_count = 0
    tot_count = 0
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    root = ET.fromstring(data)

    for count in root.iter('count'):
        num_count = num_count + int(count.text)
        tot_count = tot_count + 1

    print(tot_count)
    print(num_count)
    break
