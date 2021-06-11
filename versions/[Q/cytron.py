import os, sys
from urllib.request import urlopen

global cy_path_v, version

version = "cytron 3"

cy_path_v = os.path.dirname(sys.argv[0])

def cy_version():
    return(version)

def cy_path():
    return(cy_path_v)

def cy_mkdire(chem, nom):
    cy_mkdir(chem, nom)

def cy_mkdir(chem, nom):
    cy_temp = cy_path_v + chem + "/" + nom
    try:
        os.makedirs(cy_temp)
    except:
        pass

def cy_wget(chem, nom, addr):
    with open(chem + nom, 'wb') as img:
        img.write(urlopen(addr).read())

def cy_mkfil(chem, nom, text):
    cy_temp = cy_path_v + chem + "/" + nom
    fil = open(cy_temp, "w")
    fil.write(text)
    fil.close()

def cy_rfil(chem):
    fil = open(chem, "r")
    return(fil.read())