import urllib.request


url = 'http://www.fishc.com'

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

# open('fish.txt',wb) as f:
    

print(html)
hstr = str(html)
print(response.read(300))
