import sys, os
from urllib.request import urlopen

ip_path = os.path.dirname(sys.argv[0])+"/I-python"
os.makedirs(ip_path)

input("Appuyez sur entrée après avoir lu et accepté les conditions d’utilisation\n")
done = 1

print("Téléchargement du sous système cytron depuis le serveur de la passemblage")
try:
    with open(ip_path+"/cytron.py", 'wb') as img:
        img.write(urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/versions/%5BQ/cytron.py').read())
        print("cytron.py installé avec succès\n")
except:
    print("échec: merci de vérifier votre connexion internet ou réessayer plus tard\n")
    done = 0


print("Téléchargement du fichier principal depuis le serveur de la passemblage")
try:
    with open(ip_path + "/main.py", 'wb') as img:
        img.write(urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/versions/%5BQ/main.py').read())
        print("main.py installé avec succès\n")
except:
    print("échec: merci de vérifier votre connexion internet ou réessayer plus tard\n")
    done = 0


if done == 1:
    input("Tout les fichiers on était installés avec succès\n\nAppuyez sur entrée pour lancé I-python")
    try:
        os.system("python "+ ip_path + "/main.py")
    except:
        input("échec: merci de lancé main.py manuellement")
else:
    input("échec: appuyez sur entrée pour quitter")