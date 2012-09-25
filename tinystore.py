#!/usr/bin/python

from base64 import urlsafe_b64encode
from urllib2 import urlopen
from sys import argv, stderr
from os import stat

def split_str_into_len(s, l=256*1024):
	for i in range(0, len(s), l):
		yield s[i:i+l]

def get_url(chunk):
	return urlopen("http://tinyurl.com/api-create.php?url="+chunk+".tiny").read().split("/")[-1]

def store_file(data):
	encoded_data = urlsafe_b64encode(data)
	urls = []
	for chunk in split_str_into_len(encoded_data):
		urls.append(get_url(chunk))
	return get_url("".join(urls))

def read_file(file_name):
	fp = open(file_name, "rb")
	data = fp.read()
	fp.close()
	return data


if __name__ == "__main__":
	if len(argv) < 2:
		stderr.write("no file given\n")

	file_name = argv[1]

	if stat(file_name).st_size > 9*(1024**3):
		stderr.write("maximum file size 9gb\n")

	print store_file(read_file(file_name))
