import os, sys

global cy_path_v, version

version = "cytron 2"

cy_path_v = os.path.dirname(sys.argv[0])

def cy_version():
    return(version)

def cy_path():
    return(cy_path_v)

def cy_mkdire(chem, nom):
    cy_temp = cy_path_v + chem + "/" + nom
    try:
        os.makedirs(cy_temp)
        print("done")
    except:
        pass

def cy_mkfil(chem, nom, text):
    cy_temp = cy_path_v + chem + "/" + nom
    fil = open(cy_temp, "w")
    fil.write(text)
    fil.close()

def cy_rfil(chem):
    fil = open(chem, "r")
    return(fil.read())

cy_mkdire("/", "cytron")
cy_mkdire("/cytron" ,"user")
cy_mkdire("/cytron" ,"sys")