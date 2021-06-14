import os, sys
from urllib.request import urlopen
from _thread import start_new_thread

global cy_path_v, version, console_o

version = "cytron 6"

console_o = 0
cy_path_v = os.path.dirname(sys.argv[0])

def cy_console_print():
    if console_o == 0:
        start_new_thread(console,())

def cy_version():
    return(version)

def cy_path():
    return(cy_path_v)

def cy_mkdire(chem, nom):
    cy_mkdir(chem, nom)

def cy_mkdir(chem, nom):
    cy_temp = cy_path_v + chem + "/" + nom
    os.makedirs(cy_temp)


def cy_wget(chem, nom, addr):
    cy_temp = cy_path_v + chem + "/" + nom
    with open(cy_temp, 'wb') as img:
        img.write(urlopen(addr).read())

def cy_mkfil(chem, nom, text):
    cy_temp = cy_path_v + chem + "/" + nom
    fil = open(cy_temp, "w")
    fil.write(text)
    fil.close()

def cy_rfil(chem):
    fil = open(chem, "r")
    return(fil.read())

def cy_rfil_rela(chem, nom):
    cy_temp = cy_path_v + chem + "/" + nom
    fil = open(cy_temp, "r")
    return(fil.read())

def console():
    global console_o
    console_o = 1
    while True:
        ipt = input('~} ').split(" ")
        print(cy_run(ipt))

def cy_run(ipt):
    if ipt[0] == "":
        pass
    elif ipt[0] == "version":
        return(cy_version())
    elif ipt[0] == "path":
        return(cy_path())
    elif ipt[0] == "mkdir":
        try:
            cy_mkdir(ipt[1], ipt[2])
            return("DONE!")
        except:
            return("erreur: 'chem rela + nom'")
    elif ipt[0] == "wget":
        try:
            cy_wget(ipt[1], ipt[2], ipt[3])
            return("DONE!")
        except:
            return("erreur: 'chem rela + nom + addr'")
    elif ipt[0] == "mkfil":
        try:
            cy_mkfil(ipt[1], ipt[2], ipt[3])
            return("DONE!")
        except:
            return("erreur: 'chem rela + nom + text'")
    elif ipt[0] == "rfil":
        try:
            return(cy_rfil_rela(ipt[1], ipt[2]))
        except:
            return("erreur: 'nom'")
    elif ipt[0] == "aide" or ipt[0] == "help":
        return("version > affiche la version\npath    > affiche le chemain\nmkdir   > crée un dossier\nwget    > crée un fichier depuis le web\nmkfil   > créé un fichier\nrfil    > affiche le contenue d'un fichier\nhelp    > affiche l'aide")
    else:
        return("commande inconnu")