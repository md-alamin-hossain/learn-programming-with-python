import requests
import re
url = "http://books.toscrape.com/catalogue/the-exiled_247/index.html"
text = requests.get(url).text

regexp  = re.compile(r'<div id="product_description" class="sub-header">\s*<h2>(.*?)</h2>\s*</div>\s*<p>(.*?)</p>', re.DOTALL | re.MULTILINE)

x = re.findall(regexp, text)
# with open("text.txt", "w") as f:
#     f.write(text)

print(x)
