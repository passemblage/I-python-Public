import os, sys
from urllib.request import urlopen
from _thread import start_new_thread

global cy_path_v, version, console_o

version = "cytron 4"

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

def console_cytron():
    while console_o == 0:
        if input() == "cytron":
            if console_o == 0:
                start_new_thread(console,())
                break

def console():
    global console_o
    console_o = 1
    while True:
        ipt = input('~} ').split(" ")
        if ipt[0] == "":
            pass
        elif ipt[0] == "exit":
            console_o = 0
            start_new_thread( console_cytron,())
            break
        elif ipt[0] == "version":
            print(cy_version())
        elif ipt[0] == "path":
            print(cy_path())
        elif ipt[0] == "mkdir":
            try:
                cy_mkdir(ipt[1], ipt[2])
            except:
                print("erreur: 'chem rela + nom'")
        elif ipt[0] == "wget":
            try:
                cy_wget(ipt[1], ipt[2], ipt[3])
            except:
                print("erreur: 'chem rela + nom + addr'")
        elif ipt[0] == "mkfil":
            try:
                cy_mkfil(ipt[1], ipt[2], ipt[3])
            except:
                print("erreur: 'chem rela + nom + text'")
        elif ipt[0] == "rfil":
            try:
                print(cy_rfil_rela(ipt[1], ipt[2]))
            except:
                print("erreur: 'nom'")
        elif ipt[0] == "aide" or ipt[0] == "help":
            print("exit    > sort de la console")
            print("version > affiche la version")
            print("path    > affiche le chemain")
            print("mkdir   > crée un dossier")
            print("wget    > crée un fichier depuis le web")
            print("mkfil   > créé un fichier")
            print("rfil    > affiche le contenue d'un fichier")
            print("help    > affiche l'aide")
        else:
            print("commande inconnu")
        
start_new_thread( console_cytron,())