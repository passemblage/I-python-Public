import sys, os
from urllib.request import urlopen

import tkinter as tk
from _thread import start_new_thread

global ip_path
ip_path = os.path.dirname(sys.argv[0])+"/I-python"

fenetre = tk.Tk()
fenetre.attributes('-fullscreen', False)
fenetre.geometry('600x400')
fenetre.resizable(width=0, height=0)
fenetre.title("I-python")

dp_titre = tk.Label(fenetre, text="installation de I-python", font=('', 18))
dp_titre.pack()
dp_titre.place(x=0, y=0, width=600, height=40)

annuler = tk.Button(fenetre, text='annuler',bg = "#00ff00", activebackground="black", command =fenetre.destroy)
annuler.pack()
annuler.place(x=235, y=350, width=50, height=25)


def condition():
    global condition_ba, accepter
    condition_ba = tk.Text(fenetre, width=30)
    condition_ba.pack()
    condition_ba.place(x= 50 ,y=50,width= 500,height=250)

    try:
        condition_ba.insert(0.0, urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/fichier/README.md').read())
        condition_ba.configure(state='disabled')

        accepter = tk.Button(fenetre, text='accepter',bg = "#00ff00", activebackground="black", command =accepter_a)
        accepter.pack()
        accepter.place(x=310, y=350, width=50, height=25)

    except:
        condition_ba.insert(0.0, "échec: merci de vérifier votre connexion internet ou réessayer plus tard")
        condition_ba.configure(state='disabled')
        annuler.place(x=275, y=350, width=50, height=25)

def accepter_a():
    global version_stable, version_developpement
    condition_ba.destroy()
    accepter.destroy()
    annuler.place(x=275, y=350, width=50, height=25)

    version_stable = tk.Button(fenetre, text="dernière version\nstable -D",font=('', 12),bg = "#00ff00", activebackground="black", command=version_stable_a)
    version_stable.pack()
    version_stable.place(x=130 , y=155 , width=140, height=70)

    version_developpement = tk.Button(fenetre, text="dernière version de\n développement [Q",font=('', 12),bg = "#00ff00", activebackground="black", command=version_developpement_a)
    version_developpement.pack()
    version_developpement.place(x=330 , y= 155, width=140, height=70)

def accepter_a_d():
    version_developpement.destroy()
    version_stable.destroy()
    annuler.destroy()

def crea_dir():
    try:
        os.makedirs(ip_path)
    except:
        pass

def info_ba_crea():
    global info_ba
    info_ba = tk.Text(fenetre, width=30)
    info_ba.configure(state='disabled')
    info_ba.pack()
    info_ba.place(x= 50 ,y=50,width= 500,height=250)

def info_ba_add(info):
    global info_ba
    info_ba.configure(state='normal')
    info_ba.insert(tk.END, info+"\n")
    info_ba.configure(state='disabled')

def version_stable_t():

    try:
        with open(ip_path+"/cytron.py", 'wb') as img:
            img.write(urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/versions/-D/cytron.py').read())
            info_ba_add(">>> cytron.py installé avec succès\n")
    except:
        info_ba_add("échec: merci de vérifier votre connexion internet ou réessayer plus tard\n")

    info_ba_add("Téléchargement du fichier principal depuis Github")
    try:
        with open(ip_path + "/main.py", 'wb') as img:
            img.write(urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/versions/-D/main.py').read())
            info_ba_add(">>> main.py installé avec succès\n\nTout les fichiers on était installés avec succès")
            fin()
    except:
        info_ba_add("\néchec: merci de vérifier votre connexion internet ou réessayer plus tard\n")
        quit_i()

def version_developpement_t():
    info_ba_add("Téléchargement du sous système cytron depuis Github")
    try:
        with open(ip_path+"/cytron.py", 'wb') as img:
            img.write(urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/versions/%5BQ/cytron.py').read())
            info_ba_add(">>> cytron.py installé avec succès\n")
    except:
        info_ba_add("échec: merci de vérifier votre connexion internet ou réessayer plus tard\n")

    info_ba_add("Téléchargement du fichier principal depuis Github")
    try:
        with open(ip_path + "/main.py", 'wb') as img:
            img.write(urlopen('https://raw.githubusercontent.com/passemblage/I-python-Public/main/versions/%5BQ/main.py').read())
            info_ba_add(">>> main.py installé avec succès\n\nTout les fichiers on était installés avec succès")
            fin()
    except:
        info_ba_add("\néchec: merci de vérifier votre connexion internet ou réessayer plus tard\n")
        quit_i()

def version_stable_a():
    accepter_a_d()
    crea_dir()
    info_ba_crea()
    start_new_thread( version_stable_t,())

def version_developpement_a():
    accepter_a_d()
    crea_dir()
    info_ba_crea()
    start_new_thread( version_developpement_t,())

def quit_i():
    quit_i_b = tk.Button(fenetre, text='quitter',bg = "#00ff00", activebackground="black", command =fenetre.destroy)
    quit_i_b.pack()
    quit_i_b.place(x=275, y=350, width=50, height=25)

def fin():
    global fin_b
    fin_b = tk.Button(fenetre, text='terminer',bg = "#00ff00", activebackground="black", command =fin_a)
    fin_b.pack()
    fin_b.place(x=275, y=350, width=50, height=25)

def lance_p():
    os.system("python "+ ip_path + "/main.py")

def lance_a():
    start_new_thread( lance_p,())
    fenetre.destroy()

def fin_a():
    info_ba.destroy()
    fin_b.destroy()

    lance = tk.Button(fenetre, text='lancer I-python',bg = "#00ff00", activebackground="black", command =lance_a)
    lance.pack()
    lance.place(x=150, y=100, width=300, height=25)

    quit = tk.Button(fenetre, text='quitter',bg = "#00ff00", activebackground="black", command =fenetre.destroy)
    quit.pack()
    quit.place(x=150, y=135, width=300, height=25)

condition()
fenetre.mainloop()