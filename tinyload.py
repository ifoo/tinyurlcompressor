#!/usr/bin/python

from base64 import urlsafe_b64decode
from urllib2 import urlopen, HTTPError
from sys import argv, stderr, stdout

def split_str_into_len(s, l=256*1024):
	for i in range(0, len(s), l):
		yield s[i:i+l]

def get_url(chunk):
	try:
		return urlopen("http://tinyurl.com/"+chunk).geturl()
	except HTTPError, e:
		return e.url.split("/")[-1]


if __name__ == "__main__":
	if len(argv) < 2:
		stderr.write("no id given\n")

	tid = argv[1]

	urllist = get_url(tid).split(".")[0]
	encoded_data = ""
	for url in split_str_into_len(urllist, 7):
		encoded_data += get_url(url).split(".")[0]

	stdout.write(urlsafe_b64decode(encoded_data))
