import ssl
import builtwith
import whois

# ssl._create_default_https_context = ssl._create_unverified_context
# content = builtwith.parse("https://noc-stage.daicompanies.com")
# print(content)


# domain = whois.whois("https://google.com")
# print(domain)


import requests
import re

pattern = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>')

# response = requests.get("https://m.163.com/")
# # print(response, len(response.text))
# if response.status_code == 200:
#     all_matches = pattern.findall(response.text)
#     for href, text in all_matches:
#         print(href, text)
# print(response, response.text)

resp = requests.get("https://static.ws.126.net/163/frontend/images/2022/empty.png")
with open("163.png", "wb") as img:
    img.write(resp.content)
