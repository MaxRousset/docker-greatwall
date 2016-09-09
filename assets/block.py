#!/bin/python3
# -*- coding: utf-8 -*-


import wget, os, glob

#~ os.chdir("/usr/local/etc/unbound/")

# Trash old files if exist
try:
	os.remove("unbound.conf")
	os.remove("hosts")
except OSError:
    pass

unbound_conf = open("unbound.conf", "w")

url = "http://192.168.0.10:10080/chinois/BlockingList/raw/master/hosts"
wget.download (url)

for ligne  in open("a.txt"):
	unbound_conf.write(ligne)



for ligne  in open("hosts"):
	
	# Netoyage entete et commentaires
	if "0.0.0.0" in ligne and "#" not in ligne:
		
		# recuperation de l adresse seul
		sites = ligne.split(" ")
		sites[-1] = sites[-1].strip()
		site = str(sites[1])
		
		# creation du fichier de conf pour unbound 
		unbound_conf.write('	local-zone: "'+site+'" redirect\n')
		unbound_conf.write('	local-data: "'+site+' A 127.0.0.1"\n')



for ligne  in open("z.txt"):
	unbound_conf.write(ligne)


# Trash old files if exist
try:
	os.remove("hosts")
except OSError:
    pass

