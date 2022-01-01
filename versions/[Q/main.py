##############################       debut des importations       ##############################

import os, cytron, time
import tkinter as tk
import threading

from traceback import format_exc
from ssl import create_default_context
from smtplib import SMTP_SSL
from webbrowser import open as webopen
from _thread import start_new_thread
from datetime import datetime

##############################        fin des importations         ##############################

##############################  debut d'assignation des variables  ##############################

#globalisation des variables
global gen_couleur, console_open, menu_col_o, fsf, version_info, info_para, version_id, icai_off

# A CHANGER A CHAQUE VERSION:
version_id = "[Q 07.09"
version_info ="- NEWS -\n  adaptation cytron 13+"
info_para = "- COPYRIGHT -\n©2020-2022, I-python tout droit réservé à la PASSEMBLAGE.\nNous ne sommes pas affiliés avec Python.\
    \n\n- DEVLOPPEURS -\nlolo11: développement, programmation tests et bug ICA\npf4: développement, programmation, cytron, ICA et debug\
    \n\n- CONTACT -\nemail: passemblage@gmail.com\ndiscord: https://discord.gg/PFbymQ3d97"

#definition de la couleur par defaut
# si il y une coulleur valide dans le fichier data, on l'applique 
try: gen_couleur = cytron.rfil_rela("/cytron/sys", "data.txt").split("\n")[0]

# sinon on met en lime
except: gen_couleur= "#00FF00"

para_c_l = "#f0f0f0"
para_t_l = "black"

#definition des open (si une app est ouverte ou non)
menu_app_ouvert = "non"
para_app_o = 0
para_dark_o = 0
edt_open = 0
mda_open = 0
dp_open = 0
ce_open = 0
hedwige_open = 0
console_open = 0
menu_col_o = 0
ical_open = 0
icai_open = 0
icai_off = False
RUN = True

#initialisation de fsf : 0 = full screen, 1 = pas de full screen
fsf = 0

#set du nom de la fenetre
name_fenetre = "I-python"

#gestionaire des taches
global ttaches
ttaches = 0

##############################fin d'assignation des variables##############################

## CREATION DES DOSSIERS SYSTEME ##

cytron.mkdir("/", "cytron")
cytron.mkdir("/cytron" ,"user")
cytron.mkdir("/cytron" ,"sys")
cytron.mkdir("/cytron/sys" ,"app")
cytron.mkdir("/cytron/sys" ,"log")

#########debut du setup de la fenetre#########

#creation de la fenetre
fenetre = tk.Tk()

#fenetre en plein ecran
fenetre.attributes('-fullscreen', True)
fenetre.geometry('1040x700')

#set du titre de la fenetre
fenetre.title(name_fenetre)

##############################################
##############################################
###                                        ###
###                                        ###
###                THEMES                  ###
###                                        ###
###                                        ###
##############################################
##############################################

#changer le theme pour n'importe quoi
def theme_chang(color, text):
    global para_c_l, para_t_l, para_app_o
    fenetre.configure(bg=color)
    try: terminal_sortie.configure(bg=color,fg= text )
    except: pass
    para_c_l = color
    para_t_l = text
    if para_app_o == 1:
        para_app_d()
        para_app()

def init_fs():
    try: para_fsf_aff(cytron.rfil_rela("/cytron/sys", "data.txt").split("\n")[2])
    except: pass


#definition fonction theme clair
def para_lite():
    global para_dark_o
    theme_chang("#f0f0f0", "black")
    para_dark_o = 0

    try: modif_color(gen_couleur)
    except: pass

#definition fonction theme sombre
def para_dark(col):
    global para_dark_o, para_dark_col
    para_dark_col = col
    theme_chang(col, gen_couleur)
    para_dark_o = 1
    try:  modif_color(gen_couleur)
    except: pass


#setup du theme
try:       # si il y un theme valide dans le fichier data, on l'applique 
    setup_theme = int(cytron.rfil_rela("/cytron/sys", "data.txt").split("\n")[1])
    if setup_theme == 0: para_lite()
    else: para_dark("#171c2b")
except: para_lite()

#definition fonction alterner entre theme clair et sombre
def theme_c():
    if para_dark_o == 1: para_lite()
    else: para_dark("#171c2b")
    quitter_app()

##############################################
##############################################
###                                        ###
###                                        ###
###               MENU APP                 ###
###                                        ###
###                                        ###
##############################################
##############################################

#fonction pour quitter n'importe quelle app
def quitter_app():
    global console_open
    console_open = 0
    destroy_menu()
    para_app_d()
    edt_d()
    mda_d()
    hedwige_d()
    ce_d()
    dp_d()
    para_info_q()
    ical_d()
    icai_d()

def menu_app_titre():
    global menu_app_b
    menu_app_b = tk.Button(fenetre, font=('', 13), bg = gen_couleur, activebackground= gen_couleur, text = "MENU\n@ APP @", command =menu_app)
    menu_app_b.pack()
    menu_app_b.place(x=0,y=hauteur - 80 ,width=120,height=80)

def retour_app():
    app_retour_b.destroy()
    console.destroy()
    para_b.destroy()
    edt_b.destroy()
    hedwige_b.destroy()
    ce_b.destroy()
    ical_b.destroy()
    menu_app_titre()
    global menu_app_ouvert
    menu_app_ouvert = "non"

def menu_app():
    menu_app_b.destroy()
    global app_retour_b, menu_app_ouvert
    menu_app_ouvert = "oui"
    app_retour_b = tk.Button(fenetre,font=('', 13),bg = gen_couleur,activebackground=gen_couleur,text = "Retour",command =retour_app)
    app_retour_b.pack()
    app_retour_b.place(x=0,y=hauteur - 80,width=120,height=80)

    #bouton terminal d interpretation personalisé
    global console
    console = tk.Button(fenetre, text='Terminal\nd\'interpretation\npersonalisé', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command =console_)
    console.pack()
    console.place(x=0, y=52, width=120, height=70)

    #bouton cytron exploreur
    global ce_b
    ce_b = tk.Button(fenetre, text='cytron\n exploreur', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = ce_app)
    ce_b.pack()
    ce_b.place(x=0, y=122, width=120, height=70)

    #bouton ical
    global ical_b
    ical_b = tk.Button(fenetre, text="lanceur\nd'app ICA", font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = ical_app)
    ical_b.pack()
    ical_b.place(x=0, y=192, width=120, height=70)

    #bouton paramètres
    global para_b
    para_b = tk.Button(fenetre, text='paramètres', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command =para_app)
    para_b.pack()
    para_b.place(x=0, y=262, width=120, height=70)

    #bouton edt
    global edt_b
    edt_b = tk.Button(fenetre, text='Editeur\n de texte', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = edt_app)
    edt_b.pack()
    edt_b.place(x=0, y=332, width=120, height=70)

    #bouton hedwige
    global hedwige_b
    hedwige_b = tk.Button(fenetre, text='Hedwige', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = hedwige_app)
    hedwige_b.pack()
    hedwige_b.place(x=0, y=402, width=120, height=70)

    

#########fin du setup du menu d app#########

##############################################
##############################################
###                                        ###
###                                        ###
###               ESSENSIAL                ###
###                                        ###
###                                        ###
##############################################
##############################################

def essential_destroy():
    global menu_col_o, menu_app_ouvert
    quitter_app()
    quitter_app_b.destroy()
    ligne_menu_outil_d.destroy()
    ligne_menu_outil_g.destroy()
    info_b.destroy()
    if menu_col_o == 0:
        menu_col()
        retour_couleur()
        menu_color.destroy()
    else:
        retour_couleur()
        menu_color.destroy()
    if menu_app_ouvert == "oui": retour_app()
    menu_app_b.destroy()
    Label_Heure.destroy()

def essential(geo=""):
    global Label_Heure, ligne_menu_outil_g, info_b, ligne_menu_outil_d, quitter_app_b, largeur, hauteur, terminal_sortie, cplr_hauteur, cplr_taille, exit_fenetre, fsf
    if geo == "":
        if fsf == 1:
            largeur = fenetre.winfo_width()
            hauteur = fenetre.winfo_height()
        else:
            largeur = fenetre.winfo_screenwidth()
            hauteur = fenetre.winfo_screenheight()

    else:
        fenetre.geometry(geo)
        largeur = int(geo.split("x")[0])
        hauteur = int(geo.split("x")[1])

    menu_col2()

    #definition affichage heure
    Label_Heure = tk.Button(fenetre, font=('', 14), bg=gen_couleur,activebackground=gen_couleur, borderwidth=0,command = theme_c)
    def Heure():
        #récupérer le temps avec strftime du module time
        Label_Heure.config(text=time.strftime('%H:%M:%S'))
        #rafraichir après 0.8s
        Label_Heure.after(800, Heure)

    Heure()

    Label_Heure.place(x=largeur - 120,
                    y=hauteur - 45,
                    width=120,
                    height=45)

    #placement des lignes de menu d'outils
    ligne_menu_outil_d = tk.Button(fenetre, text='', font=('', 12), bg = gen_couleur, activebackground=gen_couleur, borderwidth=0)
    ligne_menu_outil_d.place(x=largeur - 120, y=0, width=2, height=hauteur)

    ligne_menu_outil_g = tk.Button(fenetre, text='', font=('', 12), bg = gen_couleur, activebackground=gen_couleur, borderwidth=0)
    ligne_menu_outil_g.place(x=118,y=0,width=2,height=hauteur)

    quitter_app_b = tk.Button(fenetre, text="quitter l'app", font=('', 12), bg = gen_couleur, activebackground=gen_couleur, command = quitter_app)
    quitter_app_b.place(x=0, y=26, width=120, height=26)

    info_b = tk.Button(fenetre, text= version_id + "\n" + cytron.version(), font=('', 12), bg = gen_couleur, activebackground=gen_couleur)
    info_b.place(x=largeur-120, y=0, width=120, height=52)

    # caluculs pour le relatif #
    cplr_hauteur = hauteur - (80 + 52)
    cplr_taille = cplr_hauteur / 22

    menu_app_titre()

def save_para():
    if fsf == 0: text = str(gen_couleur) + "\n" + str(para_dark_o)
    else: text = str(gen_couleur) + "\n" + str(para_dark_o) + "\n" + str(largeur) + "x" + str(hauteur)
    cytron.mkfil("/cytron/sys", "data.txt", text)


def relancer_essential():
    essential_destroy()
    essential()

#########fin du setup d essential#########

##############################################
##############################################
###                                        ###
###                                        ###
###               COULEURS                 ###
###                                        ###
###                                        ###
##############################################
##############################################

#########debut du setup des couleurs#########
def retour_couleur():
    global menu_col_o
    menu_col_o = 0
    color_retour.destroy()
    color_rose_clair.destroy()
    color_yellow.destroy()
    color_magenta.destroy()
    color_bleu_fonce.destroy()
    color_red.destroy()
    color_orange.destroy()
    color_green.destroy()
    color_blue.destroy()
    color_bleu.destroy()
    color_cyan.destroy()
    color_lime.destroy()
    color_violet.destroy()
    color_kaki.destroy()
    color_eme.destroy()
    color_blanc.destroy()
    color_rose.destroy()
    color_aubergine.destroy()
    color_bordeau.destroy()
    color_argent.destroy()
    color_charbon.destroy()
    color_cytron.destroy()
    color_printemps.destroy()
    menu_col2()

def menu_col():
    menu_color.destroy()
    global color_retour
    global menu_col_o
    menu_col_o = 1
    color_retour = tk.Button(fenetre,
                       font=('', 12),
                       bg = gen_couleur,
                       activebackground=gen_couleur,
                       text = "Retour",
                       command =retour_couleur)
    color_retour.pack()

    color_retour.place(x=largeur - 120, y= hauteur - 80, width=120, height=35)

    global color_rose_clair,color_yellow,color_magenta,color_bleu_fonce,color_red
    global color_orange,color_green,color_blue,color_bleu,color_cyan,color_lime
    global color_violet,color_kaki,color_eme,color_blanc,color_rose,color_aubergine
    global color_bordeau,color_gris,color_argent,color_charbon,color_cytron,color_printemps

    #bordeau
    def bordeau():
        modif_color('#aa1531')
    color_bordeau = tk.Button(fenetre,font=('', 12),bg = "#aa1531",activebackground='#aa1531',text = "BORDEAU",command = bordeau)
    color_bordeau.pack()
    color_bordeau.place(x=largeur - 120, y=52+cplr_taille*0, width=120, height=cplr_taille +1)

    #red
    def red():
        modif_color('red')
    color_red = tk.Button(fenetre, font=('', 12), bg = "red", activebackground='red', text = "ROUGE", command = red)
    color_red.pack()
    color_red.place(x=largeur - 120, y=52+cplr_taille*1, width=120, height=cplr_taille +1)

    #orange
    def orange():
        modif_color('#FF6100')
    color_orange = tk.Button(fenetre, font=('', 12), bg = "#FF6100", activebackground='#FF6100', text = "ORANGE", command = orange)
    color_orange.pack()
    color_orange.place(x=largeur - 120, y=52+cplr_taille*2, width=120, height=cplr_taille +1)

    #kaki / or
    def kaki():
        modif_color('#CC9729')
    color_kaki = tk.Button(fenetre,font=('', 12),bg = "#CC9729",activebackground='#CC9729',text = "OR",command = kaki)
    color_kaki.pack()
    color_kaki.place(x=largeur - 120, y=52+cplr_taille*3, width=120, height=cplr_taille +1)

    #moon
    def aubergine():
        modif_color('#f2e9a7')
    color_aubergine = tk.Button(fenetre,font=('', 12),bg = "#f2e9a7",activebackground='#f2e9a7',text = "MOON (dracula)",command = aubergine)
    color_aubergine.pack()
    color_aubergine.place(x=largeur - 120, y=52+cplr_taille*4, width=120, height=cplr_taille +1)

    #jaune
    def yellow():
        modif_color('yellow')
    color_yellow = tk.Button(fenetre,font=('', 12),bg = "yellow",activebackground='yellow',text = "JAUNE",command = yellow)
    color_yellow.pack()

    color_yellow.place(x=largeur - 120, y=52+cplr_taille*5, width=120, height=cplr_taille +1)

    #cytron
    def cytron():
        modif_color('#d0ff00')
    color_cytron = tk.Button(fenetre,font=('', 12),bg = "#d0ff00",activebackground='#d0ff00',text = "CYTRON",command = cytron)
    color_cytron.pack()
    color_cytron.place(x=largeur - 120, y=52+cplr_taille*6, width=120, height=cplr_taille +1)

    #lime
    def lime():
        modif_color('#00FF00')
    color_lime = tk.Button(fenetre,font=('', 12),bg = "#00FF00",activebackground='#00FF00',text = "LIME",command = lime)
    color_lime.pack()
    color_lime.place(x=largeur - 120, y=52+cplr_taille*7, width=120, height=cplr_taille +1)

    #printemps
    def printemps():
        modif_color('#10c342')
    color_printemps = tk.Button(fenetre,font=('', 12),bg = "#10c342",activebackground='#10c342',text = "PRINTEMPS",command = printemps)
    color_printemps.pack()
    color_printemps.place(x=largeur - 120, y=52+cplr_taille*8, width=120, height=cplr_taille +1)

    #green
    def green():
        modif_color('green')
    color_green = tk.Button(fenetre,font=('', 12),bg = "green",activebackground='green',text = "VERT",command = green)
    color_green.pack()
    color_green.place(x=largeur - 120,y=52+cplr_taille*9,width=120,height=cplr_taille +1)

    #eme
    def eme():
        modif_color('#006666')
    color_eme = tk.Button(fenetre,font=('', 12),bg = "#006666",activebackground='#006666',text = "-EME-",command = eme)
    color_eme.pack()
    color_eme.place(x=largeur - 120,y=52+cplr_taille*10, width=120,height=cplr_taille +1)

    #cyan
    def cyan():
        modif_color('#44FCCA')
    color_cyan = tk.Button(fenetre,font=('', 12),bg = "#44FCCA",activebackground='#44FCCA',text = "CYAN",command = cyan)
    color_cyan.pack()
    color_cyan.place(x=largeur - 120, y=52+cplr_taille*11, width=120, height=cplr_taille +1)

    #bleu clair
    def bleu():
        modif_color('#00acff')
    color_bleu = tk.Button(fenetre,font=('', 12),bg = "#00acff",activebackground='#00acff',text = "BLEU CLAIR",command = bleu)
    color_bleu.pack()
    color_bleu.place(x=largeur - 120, y=52+cplr_taille*12, width=120, height=cplr_taille +1)

    #blue
    def blue():
        modif_color('blue')
    color_blue = tk.Button(fenetre,font=('', 12),bg = "blue",activebackground='blue',text = "BLEU",command = blue)
    color_blue.pack()
    color_blue.place(x=largeur - 120,y=52+cplr_taille*13, width=120,height=cplr_taille +1)

    #bleu_fonce
    def bleu_fonce():
        modif_color('#001589')
    color_bleu_fonce = tk.Button(fenetre,font=('', 12),bg = "#001589",activebackground='#001589',text = "BLEU FONCE",command = bleu_fonce)
    color_bleu_fonce.pack()
    color_bleu_fonce.place(x=largeur - 120, y=52+cplr_taille*14, width=120, height=cplr_taille +1)

    #violet
    def violet():
        modif_color('#8A06C8')
    color_violet = tk.Button(fenetre,font=('', 12),bg = "#8A06C8",activebackground='#8A06C8',text = "VIOLET",command = violet)
    color_violet.pack()
    color_violet.place(x=largeur - 120, y=52+cplr_taille*15, width=120, height=cplr_taille +1)

    #rose
    def rose():
        modif_color('#EF00A7')
    color_rose = tk.Button(fenetre,font=('', 12),bg = "#EF00A7",activebackground='#EF00A7',text = "ROSE",command = rose)
    color_rose.pack()
    color_rose.place(x=largeur - 120, y=52+cplr_taille*16, width=120, height=cplr_taille +1)

    #magenta
    def magenta():
        modif_color('magenta')
    color_magenta = tk.Button(fenetre,font=('', 12),bg = "magenta",activebackground='magenta',text = "MAGENTA",command = magenta)
    color_magenta.pack()
    color_magenta.place(x=largeur - 120, y=52+cplr_taille*17, width=120, height=cplr_taille +1)

    #rose_clair
    def rose_clair():
        modif_color('#FFAADD')
    color_rose_clair = tk.Button(fenetre,font=('', 12),bg = "#FFAADD",activebackground='#FFAADD',text = "ROSE CLAIR",command = rose_clair)
    color_rose_clair.pack()
    color_rose_clair.place(x=largeur - 120, y=52+cplr_taille*18, width=120, height=cplr_taille +1)

    #blanc
    def blanc():
        modif_color('#FFFFFF')
    color_blanc = tk.Button(fenetre,font=('', 12),bg = "#FFFFFF",activebackground='#FFFFFF',text = "BLANC",command = blanc)
    color_blanc.pack()
    color_blanc.place(x=largeur - 120, y=52+cplr_taille*19, width=120, height=cplr_taille +1)

    #argent
    def argent():
        modif_color('#c8c8c8')
    color_argent = tk.Button(fenetre,font=('', 12),bg = "#c8c8c8",activebackground='#c8c8c8',text = "ARGENT",command = argent)
    color_argent.pack()
    color_argent.place(x=largeur - 120, y=52+cplr_taille*20, width=120, height=cplr_taille +1)

    #charbon
    def charbon():
        modif_color('#505050')
    color_charbon = tk.Button(fenetre,font=('', 12),bg = "#505050",activebackground='#505050',text = "CHARBON",command = charbon)
    color_charbon.pack()
    color_charbon.place(x=largeur - 120, y=52+cplr_taille*21, width=120, height=cplr_taille +1)


def menu_col2():
    global menu_color
    menu_color = tk.Button(fenetre,font=('', 12),bg = gen_couleur,activebackground= gen_couleur,text = "Theme",command = menu_col)
    menu_color.pack()
    menu_color.place(x=largeur - 120,y= hauteur - 80,width=120,height=35)

def modif_color(rgb):
    ###### GLOBALS ######
    global para_dark_o, para_t_l, gen_couleur
    gen_couleur = rgb
    para_t_l = "black"

    ###### BOUTONS ######

    ## clasique ##
    Label_Heure.configure(bg=rgb,activebackground=rgb)
    ligne_menu_outil_g.configure(bg=rgb,activebackground=rgb)
    ligne_menu_outil_d.configure(bg=rgb,activebackground=rgb)
    info_b.configure(bg=rgb,activebackground=rgb)
    quitter_app_b.configure(bg=rgb,activebackground=rgb)
    exit_fenetre.configure(bg=rgb,activebackground=rgb)

    # menu couleurs
    try: color_retour.configure(bg=rgb,activebackground=rgb)
    except: menu_color.configure(bg=rgb,activebackground=rgb)
    
    ## menu_app ##
    if menu_app_ouvert == "oui":
        app_retour_b.configure(bg=rgb,activebackground=rgb)
        retour_app()
        menu_app()
    else: menu_app_b.configure(bg=rgb,activebackground=rgb)

    ## terminal ##
    try:
        terminal_sortie.configure(fg="black")
        lancer_code.configure(bg=rgb,activebackground=rgb)
        terminal_ligne.configure(bg=rgb,activebackground=rgb)
    except: pass

    ## parametres ##
    if para_app_o == 1:
        para_color_ap_b.configure(bg=rgb,activebackground=rgb)
        para_lite_b.configure(bg="gray",activebackground="gray")
        para_dark_b.configure(bg=rgb,activebackground=rgb)
        para_fsf.configure(bg=rgb,activebackground=rgb)
        para_fst.configure(bg=rgb,activebackground=rgb)
        para_info_ex.configure(bg=rgb,activebackground=rgb)
        para_fsbr()
    try: para_info_q_b.configure(bg=rgb,activebackground=rgb)
    except: pass
    

    ## hedwige ##
    if hedwige_open == 1:
        hedwige_verif_b.configure(bg=rgb,activebackground=rgb)
        hedwige_start_b.configure(bg=rgb,activebackground="gray")

    ## edt ##
    if edt_open == 1:
        edt_save_b.configure(bg=rgb,activebackground=rgb)

    ## mda ##
    if mda_open == 1:
        mda_stop_b.configure(bg=rgb,activebackground=rgb)
        mda_anul_b.configure(bg=rgb,activebackground=rgb)
        mda_reboot_b.configure(bg=rgb,activebackground=rgb)

    ###### LABELS DARK ######
    if para_dark_o == 1:

        ## terminal ##
        try:
            terminal_code.configure(fg = "black", bg=gen_couleur)
            terminal__.configure(fg = rgb)
            terminal_sortie.configure(fg= rgb )
        except: pass

        ## hedwige ##
        if hedwige_open == 1:
            hedwige_titre.configure(fg = rgb)
            hedwige_info.configure(fg = rgb)
            hedwige_info2.configure(fg = rgb)
            hedwige_email_ba.configure(fg = "#000000", bg=gen_couleur)
            hedwige_psw_ba.configure(fg = "#000000", bg=gen_couleur)
            hedwige_email_r_ba.configure(fg = "#000000", bg=gen_couleur)
            hedwige_text_ba.configure(fg = "#000000", bg=gen_couleur)
        ## edt ##
        if edt_open == 1:
            edt_titre.configure(fg = rgb)
            edt_ba.configure(fg = "black", bg=gen_couleur)
            edt_name_ba.configure(fg = "black", bg=gen_couleur)

        ## mda ##
        if mda_open == 1:
            mda_titre.configure(fg = rgb)
            mda_version_id.configure(fg = rgb)

        ## parametres ##
        try:
            para_t_l = rgb
            para_lite_b.configure(bg=rgb,activebackground=rgb)
            para_dark_b.configure(bg="gray",activebackground="gray")
            para_color_ex.configure(fg = rgb)
            para_color_ba.configure(fg = gen_couleur)
            para_color_ba.configure(fg = "black", bg=gen_couleur)
            para_fsbr()
        except: pass
        try:
            para_titre.configure(fg = rgb)
            para_info_f.configure(fg = rgb)
        except: pass
        

    ###### LABELS LIGHT ######
    else:

        ## terminal ##
        try:
            terminal_code.configure(fg = "#000000", bg="#ffffff")
            terminal__.configure(fg = "#000000")
        except: pass

        ## hedwige ##
        if hedwige_open == 1:
            hedwige_email_ba.configure(fg = "#000000", bg="#ffffff")
            hedwige_psw_ba.configure(fg = "#000000", bg="#ffffff")
            hedwige_email_r_ba.configure(fg = "#000000", bg="#ffffff")
            hedwige_text_ba.configure(fg = "#000000", bg="#ffffff")

        ## edt ##
        if edt_open == 1:
            edt_titre.configure( fg = "#000000")
            edt_ba.configure(fg = "#000000", bg="#ffffff")
            edt_name_ba.configure(fg = "#000000", bg="#ffffff")

        ## mda ##
        if mda_open == 1:
            mda_titre.configure(fg = "#000000")
            mda_version_id.configure(fg = "#000000")

        ## parametres ##
        try:
            para_color_ba.configure( fg = "#000000")
            para_color_ba.configure(fg = "#000000", bg="#ffffff")
        except: pass

    
    ##### CLOSE & OPEN #####

    ## cytron exploreur ##
    if ce_open == 1:
        quitter_app()
        ce_app()

    ## ical ##
    if ical_open == 1:
        quitter_app()
        ical_app()

    if icai_open == 1:
        quitter_app()

#########fin du setup des couleurs#########
    
essential() #lancement de la fonction de setup

##############################################
##############################################
###                                        ###
###                                        ###
###             APLICATION                 ###
###                                        ###
###                                        ###
##############################################
##############################################

# 1 ########debut du setup de TIP######## 1 #
def destroy_menu():
    try:
        terminal_code.destroy()
        terminal_sortie.destroy()
        terminal__.destroy()
        lancer_code.destroy()
        terminal_ligne.destroy()
    except: pass

#definition fonction de l'interpreteur
def interpreter(code):
    global fsf

    commande = code.split(" ")
    
    if commande[0] == "clear" or commande[0] == "CLEAR":
        sortie = ""
        tip_sortie(sortie)

    elif commande[0] == "news" or commande[0] == "NEWS" or commande[0] == "new" or commande[0] == "NEW" or commande[0] == "info" or commande[0] == "INFO":
        sortie = version_info
        tip_sortie(sortie)

    elif commande[0] == "noir+noir=noir":
        para_dark("black")
        terminal__.configure(bg="black",fg=gen_couleur)
        sortie = "oki :)"
        tip_sortie(sortie)

    elif commande[0] == "aide":
        sortie = "dim => affiche les dimentions de I-python \nnews => affiche les infos sur la version\nfst => fullscreen True \nfsf => fullscreen False \nclear => clear l'ecran \nreb + *ARG* => reboot [0 ~} d+s / 1 ~} d / 2 ~} s] \ncytron *COMMANDE* => execute des commandes cytron (cytron aide)"
        tip_sortie(sortie)

    elif commande[0] == "dim" or commande[0] == "DIM":
        sortie = largeur,"x", hauteur
        tip_sortie(sortie)

    elif commande[0] == "fe":
        sortie = "fe inconnue"
        tip_sortie(sortie)

    elif commande[0] == "fsf":
        fsf = 1
        fenetre.attributes('-fullscreen', False)
        sortie = "fullscreen = False"
        tip_sortie(sortie)

    elif commande[0] == "fst":
        fsf = 0
        fenetre.attributes('-fullscreen', True)
        sortie = "fullscreen = True"
        tip_sortie(sortie)

    elif commande[0] == "cytron":
        try:
            arg = []
            for i in range(len(commande)-1):
                arg.append(commande[i+1])
            sortie = cytron.run(arg)
        except:
            sortie = "erreur pas d'argument"
        tip_sortie(sortie)

    elif commande[0] == "reb":
        try:
            if commande[1] == "0":
                essential_destroy()
                essential()

            elif commande[1] == "1": essential_destroy()

            elif commande[1] == "2": essential()

            else:
                sortie = "ERREUR : ARGUMENT INCONNUE ici -> " + commande[1]
                tip_sortie(sortie)

        except:
            essential_destroy()
            essential()
        

    #si pas de commande valide
    else:
        sortie = "ERREUR : COMMANDE INCONNUE"
        tip_sortie(sortie)

def tip_sortie(sortie):
    terminal_ligne.place(x=largeur/2 -205, y=120, width=2, height=len(str(sortie).split("\n")) * 20)
    terminal_sortie.config(text=sortie)

### app tip #####
def console_():
    quitter_app()

    global console_open, terminal_code, terminal__, lancer_code, terminal_sortie, terminal_ligne
    #si console fermee
    if console_open == 0:
        console_open = 1

        terminal_sortie = tk.Label(fenetre,bg=para_c_l, fg = para_t_l, font=('', 12),justify="left", anchor="nw")
        terminal_sortie.pack()
        terminal_sortie.place(x=largeur/2 -200, y=120, width=500, height=200,)

        terminal_code = tk.Entry(fenetre, width=30)
        terminal_code.insert(0, "entrez votre commande ici (taper AIDE pour commencer)")
        terminal_code.pack()
        terminal_code.place(x= 150 ,y=50,width=largeur - 300,height=20)

        terminal_ligne = tk.Button(fenetre, text='', font=('', 12), bg = gen_couleur, activebackground=gen_couleur, borderwidth=0)
        terminal_ligne.place(x=largeur/2 -205, y=120, width=2, height=0)

        if para_dark_o == 1:
            terminal_code.configure(fg = "black", bg=gen_couleur)
        else:
            terminal_code.configure(fg = "#000000", bg="#ffffff")

        terminal__ = tk.Label(fenetre, text="Terminal d'interprétation personalisé", bg=para_c_l, fg = para_t_l, font=('', 25))
        terminal__.pack()
        terminal__.place(x=largeur/2 - 257,y=2,width=515,height=40)

        #definition utilisationn bouton executer code
        def lancer_code_terminal():
            #on recupere le code
            code = terminal_code.get()
            #on l'interprete
            interpreter(code)

        lancer_code = tk.Button(fenetre, text="Executer", bg = gen_couleur, activebackground= gen_couleur, command=lancer_code_terminal)
        lancer_code.pack()
        lancer_code.place(x=largeur/2 -30, y=75,width=70, height=20)

# 1 ########fin du setup de TIP######## 1 #
# 3 ######## debut du setup des parametres ######## 3 #

def para_app():
    quitter_app()
    global para_color_ex, para_color_ba, para_color_ap_b, para_dark_b, para_lite_b, para_app_o, para_info_ex, para_fsf, para_fst
    para_app_o = 1
    para_titre_aff()
    para_color_ex = tk.Label(fenetre, text="couleur custom:",bg=para_c_l, fg = para_t_l, font=('', 12))
    para_color_ex.pack()
    para_color_ex.place(x=largeur/2 -248, y=50, width=120, height=40)

    para_color_ba = tk.Entry(fenetre, width=30)
    para_color_ba.insert(0, "      taper ici un Hex ou un nom de couleur")
    para_color_ba.pack()
    para_color_ba.place(x=largeur/2 -120, y=60, width=240, height=20)

    def para_color_ap():
        global para_color_er
        #on recupere la couleur
        rgb = para_color_ba.get()
        para_color_er_d()
        backup = gen_couleur
        if rgb == "cclebug":
            for loop in range(0, 10000000000): pass
            para_color_er_d()
            para_color_er = tk.Label(fenetre, text="ramener la coupe à la maison", bg=para_c_l, fg = para_t_l,font=('', 12))
            para_color_er.pack()
            para_color_er.place(x=largeur/2 -150, y=80, width=300, height=25)
        else:
            try: modif_color(rgb)
            except:
                modif_color(backup)
                para_color_er_d()
                para_color_er = tk.Label(fenetre, text="couleur invalide", bg=para_c_l, fg = para_t_l,font=('', 12))
                para_color_er.pack()
                para_color_er.place(x=largeur/2 -75, y=80, width=150, height=25)
                
    para_color_ap_b = tk.Button(fenetre, text="appliquer", bg = gen_couleur, activebackground= gen_couleur, command=para_color_ap)
    para_color_ap_b.pack()
    para_color_ap_b.place(x=largeur/2 + 137, y=60, width=70, height=20)

    para_lite_b = tk.Button(fenetre, text="paradise's dream",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=para_lite)
    para_lite_b.pack()
    para_lite_b.place(x=largeur/2 +5, y=120, width=135, height=25)

    para_dark_b = tk.Button(fenetre, text="dracula night", font=('', 13) , bg = gen_couleur, activebackground=gen_couleur, command=para_para_dark)
    para_dark_b.pack()
    para_dark_b.place(x=largeur/2 - 140, y=120, width=135, height=25)

    para_fst = tk.Button(fenetre, text="plein écran",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=para_fst_aff)
    para_fst.pack()
    para_fst.place(x=largeur/2 - 140, y=180, width=135, height=25)

    para_fsf = tk.Button(fenetre, text="mode fenetré",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=para_fsf_aff)
    para_fsf.pack()
    para_fsf.place(x=largeur/2 + 5, y=180, width=135, height=25)

    para_info_ex = tk.Button(fenetre, text="afficher les informations",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=para_info_aff)
    para_info_ex.pack()
    para_info_ex.place(x=largeur/2 - 140, y=240, width=280, height=25)

    para_fsbr()

    if para_dark_o == 1:
        para_lite_b.configure(bg=gen_couleur,activebackground=gen_couleur)
        para_dark_b.configure(bg="gray",activebackground="gray")
        para_color_ba.configure(fg = gen_couleur)
        para_color_ba.configure(fg = "black", bg=gen_couleur)
        
    else:
        para_lite_b.configure(bg="gray",activebackground="gray")
        para_dark_b.configure(bg=gen_couleur,activebackground=gen_couleur)
        para_color_ba.configure( fg = "#000000")
        para_color_ba.configure(fg = "#000000", bg="#ffffff")

def para_para_dark():
    para_dark("#171c2b")

def para_fsbr():
    if fsf == 1:
        para_fsf.configure(bg="gray",activebackground="gray")
    else:
        para_fst.configure(bg="gray",activebackground="gray")

def para_titre_aff():
    global para_titre
    para_titre = tk.Label(fenetre, text="Paramètres",bg=para_c_l, fg = para_t_l, font=('', 25))
    para_titre.pack()
    para_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

def para_fsf_aff(geo=""):
    global fsf
    fsf = 1
    fenetre.attributes('-fullscreen', False)
    essential_destroy()
    essential(geo)

def para_fst_aff():
    global fsf
    fsf = 0
    fenetre.attributes('-fullscreen', True)
    essential_destroy()
    essential()

def para_info_q():
    try:
        para_info_f.destroy()
        para_info_q_b.destroy()
        para_titre.destroy()
    except: pass

def para_info_r():
    para_info_q()
    para_app()


def para_info_aff():
    global para_info_f, para_info_q_b , para_titre
    para_app_d()

    para_titre = tk.Button(fenetre, text="Paramètres",bg=para_c_l, fg = para_t_l, activebackground=gen_couleur, font=('', 25), borderwidth=0, command=para_noir)
    para_titre.pack()
    para_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    para_info_f = tk.Label(fenetre, text=info_para,bg=para_c_l, fg = para_t_l, font=('', 12))
    para_info_f.pack()
    para_info_f.place(x=largeur/2 -250, y=90, width=500, height=200)

    para_info_q_b = tk.Button(fenetre, text="quitter",font=('', 12), bg = gen_couleur, activebackground=gen_couleur, command=para_info_r)
    para_info_q_b.pack()
    para_info_q_b.place(x=largeur/2 -255, y=hauteur - 100 , width=510, height=25)

def para_noir():
    para_dark("#000000")
    para_titre.configure(bg="#000000", activebackground="#000000")
    para_info_f.configure(bg="#000000")


def para_color_er_d():
    try: para_color_er.destroy()
    except: pass
def para_app_d():
    try:
        global para_app_o
        para_app_o = 0
        para_titre.destroy()
        para_color_ex.destroy()
        para_color_ba.destroy()
        para_color_ap_b.destroy()
        para_color_er_d()
        para_lite_b.destroy()
        para_dark_b.destroy()
        para_info_ex.destroy()
        para_fsf.destroy()
        para_fst.destroy()
    except: pass

# 3 ########fin du setup des parametres######## 3 #
# 4 ########debut du setup de l editeur de texte######## 4 #

def edt_app():
    quitter_app()

    global edt_titre, edt_open, edt_ba, edt_save_b, edt_name_ba, edt_open_b, edt_name_ba2
    edt_open = 1
    edt_titre = tk.Label(fenetre, text="Editeur de texte",bg=para_c_l, fg = para_t_l, font=('', 25))
    edt_titre.pack()
    edt_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    edt_ba = tk.Text(fenetre, width=30)
    edt_ba.insert(0.0, "tapez ici votre texte puis cliquez sur sauvegarder sans oublier l'extension (si vous ne savez pas enregistrer en .txt)")
    edt_ba.pack()
    edt_ba.place(x= 150 ,y=50,width=largeur - 300,height=hauteur-200)
# save #
    edt_save_b = tk.Button(fenetre, text="sauvgarder",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=edt_save)
    edt_save_b.pack()
    edt_save_b.place(x=largeur/2 +20, y=hauteur - 140, width=100, height=25)

    edt_name_ba = tk.Entry(fenetre, width=30)
    edt_name_ba.insert(0, "nom.extension")
    edt_name_ba.pack()
    edt_name_ba.place(x=largeur/2 -95, y=hauteur - 140, width=100, height=25)

# couleur #
    if para_dark_o == 1:
        edt_titre.configure(fg = gen_couleur)
        edt_ba.configure(fg = "black", bg=gen_couleur)
        edt_name_ba.configure(fg = "black", bg=gen_couleur)
    else:
        edt_titre.configure( fg = "#000000")
        edt_ba.configure(fg = "#000000", bg="#ffffff")
        edt_name_ba.configure(fg = "#000000", bg="#ffffff")

def edt_save():
    global edt_name_ba, edt_ba
    try:
        nom = edt_name_ba.get()
        text = edt_ba.get("0.0", "end")
        if nom.split("@")[0] == "DEV": cytron.mkfil("/", nom.split("@")[1], text)
        else: cytron.mkfil("/cytron/user", nom, text)
    except: dp_app("imposible de save ce fichier","@04AA")

def edt_d():
    global edt_open, edt_titre
    if edt_open == 1:
        edt_titre.destroy()
        edt_ba.destroy()
        edt_save_b.destroy()
        edt_name_ba.destroy()
        edt_open = 0

# 4 ########fin du setup de l editeur de texte######## 4 #
# 5 ########debut du setup du menu d'arret######## 5 #


def mda_app():
    quitter_app()

    global mda_titre, mda_open, mda_stop_b, mda_anul_b, mda_reboot_b, version_id, mda_version_id
    mda_open = 1
    mda_titre = tk.Label(fenetre, text="I-python",bg=para_c_l, fg = para_t_l, font=('', 25))
    mda_titre.pack()
    mda_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

#boutons

    mda_stop_b = tk.Button(fenetre, text="arret\nde I-python",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=quitter)
    mda_stop_b.pack()
    mda_stop_b.place(x=largeur/2 -50, y=hauteur/2 -130 , width=100, height=80)

    mda_anul_b = tk.Button(fenetre, text="annuler",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=quitter_app)
    mda_anul_b.pack()
    mda_anul_b.place(x=largeur/2 -50, y=hauteur/2 -40 , width=100, height=80)

    mda_reboot_b = tk.Button(fenetre, text="reb de\nI-python",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=relancer_essential)
    mda_reboot_b.pack()
    mda_reboot_b.place(x=largeur/2 -50, y=hauteur/2 +50 , width=100, height=80)

#id de la version

    mda_version_id = tk.Label(fenetre, text=version_id +" -|- " + cytron.version(), bg=para_c_l, fg = para_t_l,font=('', 10))
    mda_version_id.pack()
    mda_version_id.place(x=largeur/2 -100, y=hauteur-20, width=200, height=20)

def quitter(destroy=True):
    global RUN
    RUN = False
    save_para()
    if destroy: fenetre.destroy()

def mda_d():
    global mda_titre, mda_open, mda_stop_b, mda_anul_b, mda_reboot_b, mda_version_id
    if mda_open == 1:
        mda_titre.destroy()
        mda_stop_b.destroy()
        mda_reboot_b.destroy()
        mda_anul_b.destroy()
        mda_version_id.destroy()
        mda_open = 0

#bouton pour quitter
exit_fenetre = tk.Button(fenetre, text='Quitter',font=('', 12),bg = gen_couleur,activebackground=gen_couleur,command = mda_app)
exit_fenetre.pack()
exit_fenetre.place(x=0,y=0,width=120,height=26)

# 5 ########fin du setup du menu d'arret######## 5 #

# 6 ########debut du setup d'hedwige######## 6 #

def hedwige_app():
    quitter_app()
    global hedwige_titre, hedwige_open, hedwige_email_ba, hedwige_psw_ba, hedwige_info , hedwige_info2, hedwige_email_r_ba, hedwige_verif_b, hedwige_text_ba, hedwige_start_b
    hedwige_open = 1
    hedwige_titre = tk.Label(fenetre, text="Hedwige",bg=para_c_l, fg = para_t_l, font=('', 25))
    hedwige_titre.pack()
    hedwige_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    hedwige_info2 = tk.Label(fenetre, text="security by ENUCUA°", bg=para_c_l, fg = para_t_l,font=('', 13))
    hedwige_info2.pack()
    hedwige_info2.place(x=largeur/2 -80, y=45, width=160, height=25)

    hedwige_email_ba = tk.Entry(fenetre, width=30)
    hedwige_email_ba.insert(0, "votre Email (gmail uniquement)*")
    hedwige_email_ba.pack()
    hedwige_email_ba.place(x=largeur/2 -255, y=100 , width=250, height=25)

    hedwige_psw_ba = tk.Entry(fenetre, width=30)
    hedwige_psw_ba.insert(0, "mot de passe de votre messagerie*")
    hedwige_psw_ba.pack()
    hedwige_psw_ba.place(x=largeur/2 + 5, y=100 , width=250, height=25)

    hedwige_email_r_ba = tk.Entry(fenetre, width=30)
    hedwige_email_r_ba.insert(0, "Email du destinataire")
    hedwige_email_r_ba.pack()
    hedwige_email_r_ba.place(x=largeur/2 -255, y=170 , width=510, height=25)

    hedwige_verif_b = tk.Button(fenetre, text="cliquer ici et vérifier que l’option est bien activer pour le compte en question",font=('', 11), bg = gen_couleur, activebackground=gen_couleur, command=hedwige_verif)
    hedwige_verif_b.pack()
    hedwige_verif_b.place(x=largeur/2 -255, y=135 , width=510, height=25)

    hedwige_info = tk.Label(fenetre, text="* ces information sont uniquement envoyer a Google° pour vérifier votre identité\ncomme sur tous service de messagerie et ne sont en aucun cas stocker ou envoyer sur nos serveur", bg=para_c_l, fg = para_t_l,font=('', 10))
    hedwige_info.pack()
    hedwige_info.place(x=largeur/2 -400, y=hauteur-50, width=800, height=40)

    hedwige_text_ba = tk.Text(fenetre, width=30)
    hedwige_text_ba.insert(0.0, "tapez ici votre mail avec uniquement des chiffres et des lettres, pas de lettres accentuées ou de caractères spéciaux merci")
    hedwige_text_ba.pack()
    hedwige_text_ba.place(x= 150 ,y=205,width=largeur - 300,height=hauteur-315)

    hedwige_start_b = tk.Button(fenetre, text="envoyer",font=('', 12), bg = gen_couleur, activebackground="gray", command=hedwige_start)
    hedwige_start_b.pack()
    hedwige_start_b.place(x=largeur/2 -255, y=hauteur - 100 , width=510, height=25)

    if para_dark_o == 1:
        hedwige_email_ba.configure(fg = "#000000", bg=gen_couleur)
        hedwige_psw_ba.configure(fg = "#000000", bg=gen_couleur)
        hedwige_email_r_ba.configure(fg = "#000000", bg=gen_couleur)
        hedwige_text_ba.configure(fg = "#000000", bg=gen_couleur)
    else:
        hedwige_email_ba.configure(fg = "#000000", bg="#ffffff")
        hedwige_psw_ba.configure(fg = "#000000", bg="#ffffff")
        hedwige_email_r_ba.configure(fg = "#000000", bg="#ffffff")
        hedwige_text_ba.configure(fg = "#000000", bg="#ffffff")

def hedwige_verif():
    webopen("https://myaccount.google.com/lesssecureapps")

def hedwige_start():
    try:
        # on rentre les renseignements pris sur le site du fournisseur
        smtp_address = 'smtp.gmail.com'
        smtp_port = 465

        # on recup. les info de l'adresse e-mail de l'expediteur
        hedwige_email_address = hedwige_email_ba.get()
        hedwige_email_password = hedwige_psw_ba.get()

        # on recup. les informations sur le destinataire
        hedwige_email_receiver = hedwige_email_r_ba.get()

        # on recup. le mail 
        hedwige_email = hedwige_text_ba.get("0.0", "end")

        # on crée la connexion
        context = create_default_context()
        with SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            # connexion au compte
            server.login(hedwige_email_address, hedwige_email_password)
            # envoi du mail
            server.sendmail(hedwige_email_address, hedwige_email_receiver, hedwige_email)
    except:
        hedwige_text_ba.delete ("0.0", "end")
        hedwige_text_ba.insert(0.0, "ERREUR:\nvotre mail n'a pas peu être envoyer, merci de vérifier les adresses mails\nainsi que le mot de passe de votre messagerie. Si il sont bon,\nmerci de vérifier aussi vote connexion internet...")

def hedwige_d():
    global hedwige_open
    if hedwige_open == 1:
        hedwige_titre.destroy()
        hedwige_email_ba.destroy()
        hedwige_psw_ba.destroy()
        hedwige_info.destroy()
        hedwige_info2.destroy()
        hedwige_email_r_ba.destroy()
        hedwige_verif_b.destroy()
        hedwige_start_b.destroy()
        hedwige_text_ba.destroy()

        hedwige_open = 0

# 6 ########fin du setup d'hedwige######## 6 #
# 7 ########debut du setup de cytron exploreur######## 7 #

def ce_app():
    quitter_app()
    global ce_titre, ce_open, ce_label, ce_haut_b, ce_bas_b, ce_sel, ce_bas_go, ce_bas_ed, ce_go_pass
    ce_label = []
    ce_sel = 0
    ce_go_pass = cytron.path()
    
    ce_open = 1
    ce_titre = tk.Label(fenetre, text="Cytron Exploreur",bg=para_c_l, fg = para_t_l, font=('', 25))
    ce_titre.pack()
    ce_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    #fleches
    ce_haut_b = tk.Button(fenetre, text="⇧", font=('', 25),bg = gen_couleur,activebackground=gen_couleur,command = ce_haut)
    ce_haut_b.pack()
    ce_haut_b.place(x=largeur/2 + 100, y=150, width=40, height=40)

    ce_bas_b = tk.Button(fenetre, text="⇩", font=('', 25),bg = gen_couleur,activebackground=gen_couleur,command = ce_bas)
    ce_bas_b.pack()
    ce_bas_b.place(x=largeur/2 + 100, y=250, width=40, height=40)

    ce_bas_go = tk.Button(fenetre, text="⇨", font=('', 25),bg = gen_couleur,activebackground=gen_couleur,command = ce_go)
    ce_bas_go.pack()
    ce_bas_go.place(x=largeur/2 + 150, y=200, width=40, height=40)

    ce_bas_ed = tk.Button(fenetre, text="•", font=('', 35),bg = gen_couleur,activebackground=gen_couleur,command = ce_app)
    ce_bas_ed.pack()
    ce_bas_ed.place(x=largeur/2 + 100, y=200, width=40, height=40)

    ce_label_af(cytron.path())

def ce_label_af(x):
    global ce_len, ce_label_path, ce_sel, ce_listdir
    ce_label_path = x
    ce_listdir = os.listdir(ce_label_path)
    for ce_len in range(len(ce_listdir)):
        if ce_listdir[ce_len] == "__pycache__":
            del ce_listdir[ce_len]
            break
    if len(ce_listdir) != 0:
        for ce_len in range(len(ce_listdir)):
            ce_label.extend([tk.Label(fenetre, text=ce_listdir[ce_len],bg=para_c_l, fg = para_t_l, font=('', 12))])
            ce_label[ce_len].pack()
            ce_label[ce_len].place(x=largeur/2 -300, y= 140 + ce_len*40, width=200, height=30)
        ce_sel = 0
        if para_dark_o == 0: ce_label[0].configure(bg = gen_couleur)
        else: ce_label[0].configure(bg = gen_couleur, fg = para_dark_col)

def ce_haut():
    global ce_sel, ce_len
    ce_bgrest()
    ce_sel = ce_sel - 1
    if ce_sel == -1: ce_sel = ce_len
    try:
        if para_dark_o == 0: ce_label[ce_sel].configure(bg = gen_couleur)
        else: ce_label[ce_sel].configure(bg = gen_couleur, fg= para_dark_col)
    except: pass

def ce_bas():
    global ce_sel, ce_len
    ce_bgrest()
    ce_sel = ce_sel + 1
    if ce_sel > ce_len:
        ce_sel = 0
    try:
        if para_dark_o == 0: ce_label[ce_sel].configure(bg = gen_couleur)
        else: ce_label[ce_sel].configure(bg = gen_couleur, fg= para_dark_col)
    except: pass

def ce_go():
    global ce_sel, ce_go_pass, ce_label_path, ce_listdir
    try:
        ce_go_pass = ce_go_pass + "/" + ce_listdir[ce_sel]
        ce_go_fill = ce_listdir[ce_sel]
        
        try:
            ce_label_d()
            ce_label_af(ce_go_pass)
        except:
            try:
                edt_app()
                edt_ba.delete("0.0", "end")
                edt_ba.insert(0.0, cytron.rfil(ce_go_pass))

                edt_name_ba.delete("0", "end")
                edt_name_ba.insert(0, ce_go_fill)
            except:
                ce_app()
                dp_app("imposible d'ouvrir ce fichier avec l'edt","@07AA")
    except: pass

def ce_label_d():
    global ce_label
    try:
        for x in range(ce_len+1): ce_label[x].destroy()
    except: pass
    del ce_label
    ce_label = []

def ce_bgrest():
    global ce_label, ce_len
    try:
        for x in range(ce_len+1):
            if para_dark_o == 0: ce_label[x].configure(bg = para_c_l)
            else: ce_label[ce_sel].configure(bg= para_dark_col,fg = gen_couleur)

    except: pass

def ce_d():
    global ce_titre, ce_open, ce_label
    if ce_open == 1:
        ce_label_d()
        ce_titre.destroy()
        ce_haut_b.destroy()
        ce_bas_b.destroy()
        ce_bas_go.destroy()
        ce_bas_ed.destroy()
        ce_open = 0


# 7 ######## fin du setup de cytron exploreur######## 7 #
# 8 ###### debut du setup de la page de debug ####### 8 #

def dp_app(raison, code):
    quitter_app()

    global dp_titre, dp_open, dp_erreur, dp_version_id
    dp_open = 1
    dp_titre = tk.Label(fenetre, text="I-python",bg=para_c_l, fg = para_t_l, font=('', 25))
    dp_titre.pack()
    dp_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    #id de la version

    dp_version_id = tk.Label(fenetre, text=version_id +" -|- " + cytron.version(), bg=para_c_l, fg = para_t_l,font=('', 10))
    dp_version_id.pack()
    dp_version_id.place(x=largeur/2 -100, y=hauteur-20, width=200, height=20)

    msg = "oups une erreur s'est produite:\n "+ str(raison) + "\ncode: " + str(code)
    dp_erreur = tk.Label(fenetre, text=msg, bg=para_c_l, fg = para_t_l,font=('', 15))
    dp_erreur.pack()
    dp_erreur.place(x=largeur/2 -250, y=hauteur/2-40, width=500, height=80)

def dp_d():
    global dp_titre, dp_open, dp_erreur
    if dp_open == 1:
        dp_titre.destroy()
        dp_version_id.destroy()
        dp_erreur.destroy()
        dp_open = 0

# 8 ####### fin du setup de la page de debug ######## 8 #
# 9 ############ debut sutup ICA ############ 9 #

def ical_app():
    quitter_app()

    global ical_titre, ical_open, ical_label, ical_haut_b, ical_bas_b, ical_sel, ical_bas_go, ical_len, ical_label_path, ical_icaf
    ical_open = 1
    ical_titre = tk.Label(fenetre, text="lanceur d'app ICA",bg=para_c_l, fg = para_t_l, font=('', 25))
    ical_titre.pack()
    ical_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    ical_label = []
    ical_label_path = cytron.path() + "/cytron/sys/app"
    ical_sel = 0

    #fleches
    ical_haut_b = tk.Button(fenetre, text="⇧", font=('', 25),bg = gen_couleur,activebackground=gen_couleur,command = ical_haut)
    ical_haut_b.pack()
    ical_haut_b.place(x=largeur/2 + 100, y=150, width=40, height=40)

    ical_bas_b = tk.Button(fenetre, text="⇩", font=('', 25),bg = gen_couleur,activebackground=gen_couleur,command = ical_bas)
    ical_bas_b.pack()
    ical_bas_b.place(x=largeur/2 + 100, y=250, width=40, height=40)

    ical_bas_go = tk.Button(fenetre, text="⇨", font=('', 25),bg = gen_couleur,activebackground=gen_couleur,command = ical_go)
    ical_bas_go.pack()
    ical_bas_go.place(x=largeur/2 + 150, y=200, width=40, height=40)

    temp = os.listdir(cytron.path() + "/cytron/sys/app")
    ical_icaf = []
#rfil
    for x in range(len(temp)):
        try:
            if temp[x].split(".")[1] == "ica": ical_icaf.append(temp[x])
        except: pass

    ical_len = -2

    if len(ical_icaf) != 0:
        for ical_len in range(len(ical_icaf)):
            ical_label.extend([tk.Label(fenetre, text=ical_icaf[ical_len],bg=para_c_l, fg = para_t_l, font=('', 12))])
            ical_label[ical_len].pack()
            ical_label[ical_len].place(x=largeur/2 -300, y= 140 + ical_len*40, width=200, height=30)
        ical_sel = 0
        if para_dark_o == 0: ical_label[0].configure(bg = gen_couleur)
        else: ical_label[0].configure(bg = gen_couleur, fg = para_dark_col)

def ical_haut():
    global ical_sel, ical_len
    if ical_len != -2:
        ical_bgrest()
        ical_sel = ical_sel - 1
        if ical_sel == -1: ical_sel = ical_len
        try:
            if para_dark_o == 0: ical_label[ical_sel].configure(bg = gen_couleur)
            else: ical_label[ical_sel].configure(bg = gen_couleur, fg= para_dark_col)
        except: pass

def ical_bas():
    global ical_sel, ical_len
    if ical_len != -2:
        ical_bgrest()
        ical_sel = ical_sel + 1
        if ical_sel > ical_len:
            ical_sel = 0
        try:
            if para_dark_o == 0: ical_label[ical_sel].configure(bg = gen_couleur)
            else: ical_label[ical_sel].configure(bg = gen_couleur, fg= para_dark_col)
        except: pass

def ical_go():
    if ical_len != -2:
        global ical_sel, ical_icaf, ica_nom
        ica_nom = ical_icaf[ical_sel]
        icai(ical_label_path + "/" + ica_nom)
    

def ical_label_d():
    global ical_label
    try:
        for x in range(ical_len+1): ical_label[x].destroy()
    except: pass
    del ical_label
    ical_label = []

def ical_bgrest():
    global ical_label, ical_len
    try:
        for x in range(ical_len+1):
            if para_dark_o == 0: ical_label[x].configure(bg = para_c_l)
            else: ical_label[ical_sel].configure(bg= para_dark_col,fg = gen_couleur)
    except: pass

def ical_d():
    global ical_titre, ical_open
    if ical_open == 1:
        ical_titre.destroy()
        ical_haut_b.destroy()
        ical_bas_b.destroy()
        ical_bas_go.destroy()
        ical_label_d()
        ical_open = 0

def icai(chem):
    global icai_v, icai_link, icai_lcode
    global icai_nb_t, icai_t_nom, icai_t_x, icai_t_y, icai_t_lx, icai_t_ly
    global icai_nb_b, icai_b_nom, icai_b_x, icai_b_y, icai_b_lx, icai_b_c, icai_b_ly

    icai_init_p()
    cont = cytron.rfil(chem)
    ligne = cont.split("\n")
    nbligne = len(ligne)
    icai_log("STRAT! " + str(chem) + " -> " + str(nbligne) + " ligne(s)")      # on affiche des infos
    for nb in range(nbligne):                                                  # on traite les linge une par une
        l = ligne[nb]
        lpp = l.split(" ! ")[0]
        if lpp == "-t":                                               #si c'est une zone text
            icai_init_vt()                                            # on initialise les variables de verification text
            icai_log("zone texte ligne " + str(nb+1) + ": " + l)      # on affiche des infos
            arg = l.split(" ! ")[1].split(" , ")                      # on divise les arg.
            for nb2 in range(len(arg)):                               # on traite les arg. un par un
                div = arg[nb2].split("=")                             # on divise les arg. avec le "="
                dact = div[0]                                         # dact -> arg avent le "="
                dinf = div[1]                                         # dinf -> arg après le "="
                icai_log(str(dact) +"-> "+ str(dinf))                 # on affiche des infos
                if dact == "nom":
                    tnom = dinf
                    icai_v[0] = True
                elif dact == "x":
                    tx = dinf
                    icai_v[1] = True
                elif dact == "y":
                    ty = dinf
                    icai_v[2] = True
                elif dact == "lx":
                    tlx = dinf
                    icai_v[3] = True
                elif dact == "ly":
                    tly = dinf
                    icai_v[4] = True
                else:
                    icai_log("dact inconnu ici-> " + dact)
            if icai_v == [True, True, True, True, True]:
                icai_nb_t = icai_nb_t + 1
                icai_t_nom.append(tnom)
                icai_t_x.append(tx)
                icai_t_y.append(ty)
                icai_t_lx.append(tlx)
                icai_t_ly.append(tly)
                icai_log("ARGS ok")
            else:
                icai_log("ARGS manquant: [nom, x, y, lx, ly] statut: "+ str(icai_v))

        elif lpp == "-b":                                             #si c'est un bouton
            icai_init_vt()                                            # on initialise les variables de verification text
            icai_log("bouton ligne " + str(nb+1) + ": " + l)          # on affiche des infos
            arg = l.split(" ! ")[1].split(" , ")                      # on divise les arg.
            for nb2 in range(len(arg)):                               # on traite les arg. un par un
                div = arg[nb2].split("=")                             # on divise les arg. avec le "="
                dact = div[0]                                         # dact -> arg avent le "="
                dinf = div[1]                                         # dinf -> arg après le "="
                icai_log(str(dact) +"-> "+ str(dinf))                 # on affiche des infos
                if dact == "nom":
                    tnom = dinf
                    icai_v[0] = True
                elif dact == "x":
                    tx = dinf
                    icai_v[1] = True
                elif dact == "y":
                    ty = dinf
                    icai_v[2] = True
                elif dact == "lx":
                    tlx = dinf
                    icai_v[3] = True
                elif dact == "ly":
                    tly = dinf
                    icai_v[4] = True
                elif dact == "c":
                    tc = dinf
                else:
                    icai_log("dact inconnu ici-> " + dact)
            if icai_v == [True, True, True, True, True]:
                icai_nb_b = icai_nb_b + 1
                icai_b_nom.append(tnom)
                icai_b_x.append(tx)
                icai_b_y.append(ty)
                icai_b_lx.append(tlx)
                icai_b_ly.append(tly)
                try: icai_b_c.append(tc)
                except: icai_b_c.append(gen_couleur)
                
                icai_log("ARGS ok")
            else:
                icai_log("ARGS manquant: [nom, x, y, lx, ly] statut: "+ str(icai_v))

        elif lpp == "/link" or lpp == "/l":                             # si c'est un lien
            icai_log("lien ligne " + str(nb+1) + ": " + l)              # on affiche des infos
            try:
                cytron.rfil_rela("/cytron/sys/app/", l.split(" ! ")[1])     # on test le lien
                icai_link.append(l.split(" ! ")[1])                            # on save le lien

                icai_log("lien valide")                                 # on affiche des infos
            except:
                icai_log("lien invalide")                               # on affiche des infos
        elif lpp == "/d" or lpp == "/download":
            icai_log("download ligne " + str(nb+1) + ": " + l)          # on affiche des infos
            try:
                arg = l.split(" ! ")[1].split(" | ")                    # on divise les arg.
                if int(arg[2]) == 1:
                    icai_log("type de telechargement: force")
                    cytron.wget("/cytron/sys/app", str(arg[0]), str(arg[1]))
                else:
                    icai_log("type de telechargement: standard")
                    try:
                        cytron.rfil_rela("/cytron/sys/app/", str(arg[0]))
                        icai_log("-> fichier deja present")
                    except:
                        icai_log("-> ficher non pressent, telechargent")
                        cytron.wget("/cytron/sys/app", str(arg[0]), str(arg[1]))
                icai_log("fin de la commande de telechargement")
            except: icai_log("erreur telechargement!")
        elif l == "/go":                                                # si on a le signal /go
            icai_log("lancement de icai_go")                                 
            icai_go()                                                   # on lance la creation de bouton
            icai_log("fin de icai_go")
    icai_log("fin de icai\n")
    icai_log_print()

def icai_log(text):
    global log
    log = log + "\n" + datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3] + " | " + text

def icai_log_print():
    global log
    try:
        text = cytron.rfil_rela("/cytron/sys/log", "ica.log")
        cytron.mkfil("/cytron/sys/log", "ica.log", text + "\n" + log)
    except:
        cytron.mkfil("/cytron/sys/log", "ica.log", log)


def icai_init_p():
    global log, icai_link, icai_lcode
    global icai_nb_t, icai_t_nom, icai_t_x, icai_t_y, icai_t_lx, icai_t_ly, icai_t
    global icai_nb_b, icai_b_nom, icai_b_x, icai_b_y, icai_b_lx, icai_b_ly, icai_b_c, icai_b

    icai_nb_t = 0
    icai_t_nom = []
    icai_t_x = []
    icai_t_y = []
    icai_t_lx = []
    icai_t_ly = []
    icai_t = []

    icai_nb_b = 0
    icai_b_nom = []
    icai_b_x = []
    icai_b_y = []
    icai_b_lx = []
    icai_b_ly = []
    icai_b_c = []
    icai_b = []

    icai_link = []
    icai_lcode = []

    log = ""


def icai_init_vt():
    global icai_v
    icai_v = [False, False, False, False, False]

def icai_go():
    global ica_nom, icai_titre, icai_open, icai_link, icai_download_l, icai_download_f, icai_download_o
    global icai_nb_t, icai_t_nom, icai_t_x, icai_t_y, icai_t_lx, icai_t_ly, icai_t
    global icai_nb_b, icai_b_nom, icai_b_x, icai_b_y, icai_b_lx, icai_b_ly, icai_b_c, icai_b

    ical_d()
    icai_open = 1
    titre = ica_nom.split(".")[0]
    icai_titre = tk.Label(fenetre, text=titre,bg=para_c_l, fg = para_t_l, font=('', 25))
    icai_titre.pack()
    icai_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    for link in icai_link:
        try: exec(cytron.rfil_rela("/cytron/sys/app/", str(link)))
        except Exception as err:
            print("ERREUR EXECUTION DU LIEN '"+ str(link) + "': " , format_exc())
            dp_app(err, "@09AA")


    for nb in range(icai_nb_t):                 #placement de zone text
        icai_t.extend([tk.Label(fenetre, text=icai_t_nom[nb],bg=para_c_l, fg = para_t_l, font=('', 12))])
        icai_t[nb].pack()
        icai_t[nb].place(x=icai_t_x[nb], y= icai_t_y[nb], width= icai_t_lx[nb], height=icai_t_ly[nb])

    for nb in range(icai_nb_b):                 #placement des bouton
        icai_b.extend([tk.Button(fenetre, text=icai_b_nom[nb],bg = icai_b_c[nb], activebackground=icai_b_c[nb], font=('', 12))])
        icai_b[nb].pack()
        icai_b[nb].place(x=icai_b_x[nb], y= icai_b_y[nb], width= icai_b_lx[nb], height=icai_b_ly[nb])

def icai_d_t():
    for nb in range(icai_nb_t): icai_t[nb].destroy()
    for nb in range(icai_nb_b):icai_b[nb].destroy()
    
def icai_offs():
    global icai_off
    icai_off = True
    time.sleep(0.5)
    icai_off = False

def icai_d():
    global icai_open
    if icai_open == 1:
        icai_titre.destroy()
        icai_d_t()
        threading.Thread(target=icai_offs, args=(),name="icai off").start()
        icai_open = 0





##############################################
##############################################
###                                        ###
###                                        ###
###             SOUS SYSTEMES              ###
###                                        ###
###                                        ###
##############################################
##############################################




######## AUTO REB #########

def auto_reb():

    def c_coef():
        if fsf == 1: c = fenetre.winfo_width() * fenetre.winfo_height()
        else: c = fenetre.winfo_screenwidth() * fenetre.winfo_screenheight()
        return(c)

    actu = c_coef()

    while RUN:
        if c_coef() != actu:
            coef = c_coef()
            time.sleep(0.1)
            while coef != c_coef():
                coef = c_coef()
                time.sleep(0.5)
            essential_destroy()
            essential()
            actu = c_coef()
        time.sleep(0.4)
        

###### metronome de taches ######

def metronome():
    global RUN
    old = ""
    while RUN:
        # auto off

        if threading.enumerate()[0].is_alive() == False:
            print("\n█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █\n\
                    \nINFO: Le programme a mal été arrêter, il est possible que les paramètre ne soit pas sauvegardé, merci de quitter I-python via le bouton en haut a gauche.\
                \n\n█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █\n")
            quitter(False)
            print(".")

        # printer
        taches = ""
        for thread in threading.enumerate():
            taches += str(thread.name) + " -> " + str(thread.is_alive()) + " | " + str(thread.isDaemon()) + "\n"
        if taches != old:
            print("---TACHES---")
            print(taches)
            old = taches
        time.sleep(1)
    print("STOP metronome")

#### LANCEMENT DES THREAD #####
# metronome de tache
thr_metronome = threading.Thread(target=metronome, args=(),name="task metronome")
thr_metronome.start()
# auto reb
thr_autoreb = threading.Thread(target=auto_reb, args=(),name="auto reb")
thr_autoreb.daemon = True
thr_autoreb.start()

# init du full screen (on/off)
init_fs()

# boucle du programme
fenetre.mainloop()