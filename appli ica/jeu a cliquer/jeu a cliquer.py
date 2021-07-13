#/d ! jeu a cliquer.py | https://raw.githubusercontent.com/passemblage/I-python-Public/main/appli%20ica/jeu%20a%20cliquer/jeu%20a%20cliquer.py | 1

import cytron

global argent
argent = 0.0
global nbclic
nbclic = 1.0
global prixclic
prixclic = 1.0

cytron.cy_mkdir("/cytron/sys/app/", "sauvegardes_jeu_a_cliquer")

try:
    fichier = cytron.cy_rfil_rela("/cytron/sys/app/sauvegardes_jeu_a_cliquer/", "save.txt")
    argent = float(fichier.split("\n")[0])
    nbclic = float(fichier.split("\n")[1])
    prixclic = float(fichier.split("\n")[2])
except:
    fichier_de_base = str(argent + "\n" + nbclic + "\n" + prixclic)
    cytron.cy_mkfil("/cytron/sys/app/sauvegardes_jeu_a_cliquer/", "save.txt", fichier_de_base)

global texte_ame
texte_ame = tk.Label(fenetre, text="Amelioration clicks :  ", font=('', 30), bg = "red")
texte_ame.pack()
texte_ame.place(x=largeur/2-200, y=hauteur-140)

def clic_argent():
    global argent
    argent += nbclic
    bouton_principal.config(text=int(argent)) 

global bouton_principal
bouton_principal = tk.Button(fenetre, text=int(argent),font=('', 30), bg = "red", activebackground="red", command=clic_argent)
bouton_principal.pack()
bouton_principal.place(x=largeur/2-200, y=hauteur/2 , width=400, height=70)

def amelioration_clic():
    global prixclic, nbclic, argent
    if argent > prixclic:
        argent += -prixclic
        prixclic *= 1.5
        nbclic += 1
        bouton_principal.config(text=int(argent)) 
        bouton_amelioration.config(text=("prix : " + str(int(prixclic)) + "  " + str(int(nbclic))) + " clics") 

global bouton_amelioration
bouton_amelioration = tk.Button(fenetre, text=("prix : " + str(int(prixclic)) + "  " + str(int(nbclic)) + "clics"),font=('', 20), bg = "red", activebackground="red", command=amelioration_clic)
bouton_amelioration.pack()
bouton_amelioration.place(x=largeur/2-200, y=hauteur-70 , width=400, height=70)

def off():
    def stop():
        global bouton_principal, bouton_amelioration, texte_ame
        bouton_principal.destroy()
        bouton_amelioration.destroy()
        texte_ame.destroy()
        #save
        global argent, nbclic, prixclic
        truc_a_save = str(str(argent) + "\n" + str(nbclic) + "\n" + str(prixclic))
        print(truc_a_save)
        cytron.cy_mkfil("/cytron/sys/app/sauvegardes_jeu_a_cliquer/", "save.txt", truc_a_save)
    while True:
        if icai_off == True:
            try:
                stop()
            except:
                pass
        else:
            time.sleep(0.2)
start_new_thread( off,())