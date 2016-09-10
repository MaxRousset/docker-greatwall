#!/bin/python3
# -*- coding: utf-8 -*-


import wget, os, glob, sys


""" Go to working directory """
pathname = os.path.dirname(sys.argv[0])
os.chdir(os.path.abspath(pathname))


""" Trash old config if exist """
try:
	os.remove("unbound.conf")
	os.remove("hosts")
except OSError:
    pass

""" Get hosts files """
URL = "http://192.168.0.10:10080/chinois/BlockingList/raw/master/hosts"
wget.download (URL)


""" Generate config file for unbound """
def gen_config():
	unbound_conf = open("unbound.conf", "w")

	# write header config
	for ligne  in open("a.txt"):
		unbound_conf.write(ligne)

	# write site to block to config
	for ligne  in open("hosts"):
		# Netoyage entete et commentaires , recuperation de l adresse seul
		if "0.0.0.0" in ligne and "#" not in ligne:
			sites = ligne.split(" ")
			sites[-1] = sites[-1].strip()
			site = str(sites[1])
			unbound_conf.write('	local-zone: "'+site+'" redirect\n	local-data: "'+site+' A 127.0.0.1"\n')

	# write footer to config
	for ligne  in open("z.txt"):
		unbound_conf.write(ligne)

	os.remove("hosts")
	print ("\nConfig generated !");


gen_config()
