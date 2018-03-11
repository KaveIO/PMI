import codecs, collections, json, gzip, os, sys, xml.sax

with gzip.open("pmi_data/dblp.json.gz", "rb") as f, open("pmi_data/dblp.json", "wb") as w:
	w.write(f.read())
w.close()