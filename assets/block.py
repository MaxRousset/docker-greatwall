#!/bin/python3
# -*- coding: utf-8 -*-


import wget, os, glob, sys


""" Go to working directory """
pathname = os.path.dirname(sys.argv[0])
os.chdir(os.path.abspath(pathname))


""" Trash old config if exist """ #  todo : replace by if
try:
	os.remove("unbound.conf")
	os.remove("hosts")
except OSError:
    pass

""" Get hosts files """
URL = str(sys.argv[1])
wget.download (URL)


""" Generate config file for unbound """
def gen_config():
	unbound_conf = open("unbound.conf", "w")

	# Write header config
	for ligne  in open("header.conf"):
		unbound_conf.write(ligne)

	# Write site to block to config
	for ligne  in open("hosts"):
		# Get adress of bad host from hosts file
		if "0.0.0.0" in ligne and "#" not in ligne:
			hosts = ligne.split(" ")
			hosts[-1] = hosts[-1].strip()
			host = str(hosts[1])
			unbound_conf.write('	local-zone: "'+host+'" redirect\n	local-data: "'+host+' A 127.0.0.1"\n')

	# write footer to config
	for ligne  in open("footer.conf"):
		unbound_conf.write(ligne)

	os.remove("hosts")
	print ("\nConfig generated !");


gen_config()
