#!/usr/bin/env python3
import urllib.request
print("in client")
fp= urllib.request.urlopen("http://localhost:1234/")
encodedcontent = fp.read()
decodedcontent = encodedcontent.decode("utf8")
print(decodedcontent)
fp.close()