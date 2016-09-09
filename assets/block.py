#!/bin/python3
# -*- coding: utf-8 -*-


import wget, os, glob

# Trash old files if exist
try:
    os.remove("dns.txt")
except OSError:
    pass


dns_conf = open("dns.txt", "a")

unbound_conf = open("unbound.conf", "w")

#~ source = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn-social/hosts"
#~ wget.download (source)


for ligne  in open("a.txt"):
	unbound_conf.write(ligne)



for ligne  in open("hosts"):
	
	# Netoyage entete et commentaires
	if "0.0.0.0" in ligne and "#" not in ligne:
		
		# filtre
		sites = ligne.split(" ")
		sites[-1] = sites[-1].strip()
		
		# recuperation des adresses brut
		site = str(sites[1])
		
		# creation du fichier de conf pour unbound 
		unbound_conf.write('	local-zone: "'+site+'" redirect\n')
		unbound_conf.write('	local-data: "'+site+' A 127.0.0.1"\n')

for ligne  in open("z.txt"):
	unbound_conf.write(ligne)

#~ os.remove("hosts")
#~ a = str(open("a.txt"))
#~ dns = str(open("dns.txt"))
#~ z = str(open("z.txt"))
#~ unbound_conf.write(a+dns+z)
#~ files = glob.glob( '*.txt' )

#~ with open( 'unbound.conf', 'w' ) as result:
    #~ for file_ in files:
        #~ for line in open( file_, 'r' ):
            #~ result.write( line )
