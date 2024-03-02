#!/usr/bin/python3
"""script that fetches URL"""


from urllib.request import urlopen
with urlopen("https://alx-intranet.hbtn.io/status") as web:
    body = web.read()
    body_decoded = body.decode('utf-8')
    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body_decoded))
