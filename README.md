tinyurlcompressor
=================

tinyurlcompressor exploits tinyurl.com to store files in the tinyurl database. It splits files into 256k chunks, base64-encodes it and uses [tinyurl api-create](http://tinyurl.com/api-create.php?url=http://DATA) to store the data in tinyurl's database. You get a single, 7 character key to get your data back.

Example:

	./tinystore.py README.md
	bpbx5uj

The data is stored at [http://tinyurl.com/bpbx5uj](http://tinyurl.com/bpbx5uj) and the file can be retrieved again:

	./tinyload.py bpbx5uj > README.md_new
