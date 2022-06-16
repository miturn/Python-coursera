import urllib.request, urllib.parse, urllib.error
import json
import ssl
import pprint

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.json'
else :
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
        #address = 'http://py4e-data.dr-chuck.net/comments_42.json'
    
    
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    info = json.loads(data)
    
    tot_count = 0
        
    def comment_count(dict_key, count):
        total_count = 0
        for k, v in dict_key.items():
            if k == 'comments':
                for l in v:
                   total_count = total_count + l.get(count, 0)
        return total_count

  
    print(comment_count(info, 'count'))