#!/usr/bin/python3
"""script that fetches URL"""


from urllib.request import urlopen
if __name__ == '__main__':
    with urlopen("https://alx-intranet.hbtn.io/status") as web:
        body = web.read()
        body_decoded = body.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body_decoded))
