import requests
import re
base_url = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/the-exiled_247/index.html"
response = requests.get(url).text

regexp = re.compile(r'<div class="item active">\s*<img src="../../(.*?)"')
result = " ".join(re.findall(regexp, response))

img_link = base_url + result
net_img_link = requests.get(img_link)
with open("2.png", "wb") as f:
    f.write(net_img_link.content)
