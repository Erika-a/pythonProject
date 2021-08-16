"""
r = requests.get("https://www.bilibili.com")

r.encoding = 'utf-8'
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.apparent_encoding)
print(r.content)

"""

"""
def gethtmltext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__ == "__main__"
    url = "https://www.baidu.com"
    print(gethtmltext(url))
"""

u = pow(2, 10)

print(u)

import sys

print(sys.float_info)

a = 5
b = 5.5
c = a + b

print(c)
