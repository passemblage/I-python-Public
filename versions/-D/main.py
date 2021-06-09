######### notes #########

#path = os.getcwd()
#path = path
#print(path)

######### importations #########
import tkinter as tk
import time, os, smtplib, ssl
from webbrowser import open as webopen

######### inisialisation des variables #########
    #global
global gen_couleur, console_open, menu_col_o, fsf, version_info, info_para

    # A CHANGER A CHAQUE VERSION:
version_info = "VERSION: -D 05 \n\n - NEWS - \n-APO \n\nmerci d'aller dans les paramètres pour plus d'info"
info_para = "- COPYRIGHT -\n©2020-2021, I-python tout droit réservé à la PASSEMBLAGE.\nNous ne sommes pas affiliés avec Python.\n\n- DEVLOPPEURS -\nlolo11: développement, programmation et tests\npf4: développement, programmation et debug\n\n- CONTACT -\nemail: passemblage@gmail.com\ndiscord: wHwZNkdRB7"

    #definition couleur
gen_couleur= "#00FF00"
para_c_l = "#f0f0f0"
para_t_l = "black"

    #definition des open
menu_app_ouvert = "non"
para_app_o = 0
para_dark_o = 0
edt_open = 0
mda_open = 0
addtest_open = 0
hedwige_open = 0
console_open = 0
apo_open = 0
menu_col_o = 0

fsf = 0

    #inisialisation de TIP
dev = 0
color_yn = 0
sortie_ = ""

######### generation de la fenetre #########
fenetre = tk.Tk()
    #fenetre plein ecran
fenetre.attributes('-fullscreen', True)
    #nom de la fenetre
fenetre.title("I-python")

# theme c
def theme_c():
    if para_dark_o == 1:
        para_lite()
    else:
        para_dark()
    quitter_app()

#definition sortie TIP
def message_bvn_():
    if console_open == 0:
        message_bvn.config(text="")
        global dev
        dev = 0
    else:
        message_bvn.config(text=None)
    message_bvn.after(10, message_bvn_)

#fonction pour quitter n'importe quelle app
def quitter_app():
    global console_open
    console_open = 0
    destroy_menu()
    addtest_app_d()
    para_app_d()
    edt_d()
    mda_d()
    hedwige_d()
    para_info_q()
    apo_app_d()

def menu_app2():
    global menu_app_b
    menu_app_b = tk.Button(fenetre, font=('', 13), bg = gen_couleur, activebackground= gen_couleur, text = "MENU\n@ APP @", command =menu_app)
    menu_app_b.pack()
    menu_app_b.place(x=0,y=hauteur - 80 ,width=120,height=80)

def retour_app():
    app_retour_b.destroy()
    console.destroy()
    taches_gestion.destroy()
    addtest_b.destroy()
    para_b.destroy()
    edt_b.destroy()
    hedwige_b.destroy()
    apo_b.destroy()
    menu_app2()
    global menu_app_ouvert
    menu_app_ouvert = "non"

def menu_app():
    menu_app_b.destroy()
    global app_retour_b, menu_app_ouvert
    menu_app_ouvert = "oui"
    app_retour_b = tk.Button(fenetre,
                       font=('', 13),
                       bg = gen_couleur,
                       activebackground=gen_couleur,
                       text = "Retour",
                       command =retour_app)
    app_retour_b.pack()
    app_retour_b.place(x=0,y=hauteur - 80,width=120,height=80)

    #bouton terminal d interpretation personalisé
    global console
    console = tk.Button(fenetre, text='Terminal\nd\'interpretation\npersonalisé', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command =console_)
    console.pack()
    console.place(x=0, y=52, width=120, height=70)

    #bouton gestionaire des taches
    global taches_gestion
    taches_gestion = tk.Button(fenetre, text='Gestionnaire\ndes\ntaches', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command =taches_gestion_)
    taches_gestion.pack()
    taches_gestion.place(x=0, y=122, width=120, height=70)

    #bouton addtest
    global addtest_b
    addtest_b = tk.Button(fenetre, text='ADD\nTEST', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command =addtest_app)
    addtest_b.pack()
    addtest_b.place(x=0, y=192, width=120, height=70)

    #bouton paramètres
    global para_b
    para_b = tk.Button(fenetre, text='paramètres', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command =para_app)
    para_b.pack()
    para_b.place(x=0, y=262, width=120, height=70)

    #bouton edt
    global edt_b
    edt_b = tk.Button(fenetre, text='Editeur\n de text', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = edt_app)
    edt_b.pack()
    edt_b.place(x=0, y=332, width=120, height=70)

    #bouton hedwige
    global hedwige_b
    hedwige_b = tk.Button(fenetre, text='Hedwige', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = hedwige_app)
    hedwige_b.pack()
    hedwige_b.place(x=0, y=402, width=120, height=70)

    #bouton APO
    global apo_b
    apo_b = tk.Button(fenetre, text='APO', font=('', 12), bg = gen_couleur,activebackground=gen_couleur,command = apo_app)
    apo_b.pack()
    apo_b.place(x=0, y=472, width=120, height=70)


def essential_destroy():
    global menu_col_o, menu_app_ouvert
    quitter_app()
    quitter_app_b.destroy()
    ligne_menu_outil_d.destroy()
    ligne_menu_outil_g.destroy()
    message_bvn.destroy()

    if menu_col_o == 0:
        menu_col()
        retour()
        menu_color.destroy()
    else:
        retour()
        menu_color.destroy()

    if menu_app_ouvert == "oui":
        retour_app()
    #app_retour_b.destroy()
    menu_app_b.destroy()
    Label_Heure.destroy()
    

def retour():
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
    color_gris.destroy()
    color_argent.destroy()
    color_charbon.destroy()
    color_citron.destroy()
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
                       command =retour)
    color_retour.pack()

    color_retour.place(x=largeur - 120, y= hauteur - 80, width=120, height=35)

    global color_rose_clair,color_yellow,color_magenta,color_bleu_fonce,color_red
    global color_orange,color_green,color_blue,color_bleu,color_cyan,color_lime
    global color_violet,color_kaki,color_eme,color_blanc,color_rose,color_aubergine
    global color_bordeau,color_gris,color_argent,color_charbon,color_citron,color_printemps

    #bordeau
    def bordeau():
        modif_color('#6d071a')
    color_bordeau = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#6d071a",
                       activebackground='#6d071a',
                       text = "BORDEAU",
                       command = bordeau)
    color_bordeau.pack()
    color_bordeau.place(x=largeur - 120, y=cplr_hauteur/23*0, width=120, height=cplr_hauteur/23 +1)

    #red
    def red():
        modif_color('red')
    color_red = tk.Button(fenetre,
                       font=('', 12),
                       bg = "red",
                       activebackground='red',
                       text = "ROUGE",
                       command = red)
    color_red.pack()
    color_red.place(x=largeur - 120, y=cplr_hauteur/23*1, width=120, height=cplr_hauteur/23 +1)

    #orange
    def orange():
        modif_color('#FF6100')
    color_orange = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#FF6100",
                       activebackground='#FF6100',
                       text = "ORANGE",
                       command = orange)
    color_orange.pack()
    color_orange.place(x=largeur - 120, y=cplr_hauteur/23*2, width=120, height=cplr_hauteur/23 +1)

    #kaki / or
    def kaki():
        modif_color('#CC9729')
    color_kaki = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#CC9729",
                       activebackground='#CC9729',
                       text = "OR",
                       command = kaki)
    color_kaki.pack()
    color_kaki.place(x=largeur - 120, y=cplr_hauteur/23*3, width=120, height=cplr_hauteur/23 +1)

    #moon
    def aubergine():
        modif_color('#f2e9a7')
    color_aubergine = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#f2e9a7",
                       activebackground='#f2e9a7',
                       text = "MOON (dracula)",
                       command = aubergine)
    color_aubergine.pack()
    color_aubergine.place(x=largeur - 120, y=cplr_hauteur/23*4, width=120, height=cplr_hauteur/23 +1)

    #jaune
    def yellow():
        modif_color('yellow')
    color_yellow = tk.Button(fenetre,
                       font=('', 12),
                       bg = "yellow",
                       activebackground='yellow',
                       text = "JAUNE",
                       command = yellow)
    color_yellow.pack()

    color_yellow.place(x=largeur - 120, y=cplr_hauteur/23*5, width=120, height=cplr_hauteur/23 +1)

    #citron
    def citron():
        modif_color('#d0ff00')
    color_citron = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#d0ff00",
                       activebackground='#d0ff00',
                       text = "CITRON",
                       command = citron)
    color_citron.pack()
    color_citron.place(x=largeur - 120, y=cplr_hauteur/23*6, width=120, height=cplr_hauteur/23 +1)

    #lime
    def lime():
        modif_color('#00FF00')
    color_lime = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#00FF00",
                       activebackground='#00FF00',
                       text = "LIME",
                       command = lime)
    color_lime.pack()
    color_lime.place(x=largeur - 120, y=cplr_hauteur/23*7, width=120, height=cplr_hauteur/23 +1)

    #printemps
    def printemps():
        modif_color('#10c342')
    color_printemps = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#10c342",
                       activebackground='#10c342',
                       text = "PRINTEMPS",
                       command = printemps)
    color_printemps.pack()
    color_printemps.place(x=largeur - 120, y=cplr_hauteur/23*8, width=120, height=cplr_hauteur/23 +1)

    #green
    def green():
        modif_color('green')
    color_green = tk.Button(fenetre,
                       font=('', 12),
                       bg = "green",
                       activebackground='green',
                       text = "VERT",
                       command = green)
    color_green.pack()
    color_green.place(x=largeur - 120,y=cplr_hauteur/23*9,width=120,height=cplr_hauteur/23 +1)

    #eme
    def eme():
        modif_color('#006666')
    color_eme = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#006666",
                       activebackground='#006666',
                       text = "-EME-",
                       command = eme)
    color_eme.pack()
    color_eme.place(x=largeur - 120,y=cplr_hauteur/23*10, width=120,height=cplr_hauteur/23 +1)

    #cyan
    def cyan():
        modif_color('#44FCCA')
    color_cyan = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#44FCCA",
                       activebackground='#44FCCA',
                       text = "CYAN",
                       command = cyan)
    color_cyan.pack()
    color_cyan.place(x=largeur - 120, y=cplr_hauteur/23*11, width=120, height=cplr_hauteur/23 +1)

    #bleu claire
    def bleu():
        modif_color('#00acff')
    color_bleu = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#00acff",
                       activebackground='#00acff',
                       text = "BLEU CLAIRE",
                       command = bleu)
    color_bleu.pack()
    color_bleu.place(x=largeur - 120, y=cplr_hauteur/23*12, width=120, height=cplr_hauteur/23 +1)

    #blue
    def blue():
        modif_color('blue')
    color_blue = tk.Button(fenetre,
                       font=('', 12),
                       bg = "blue",
                       activebackground='blue',
                       text = "BLEU",
                       command = blue)
    color_blue.pack()
    color_blue.place(x=largeur - 120,y=cplr_hauteur/23*13, width=120,height=cplr_hauteur/23 +1)

    #bleu_fonce
    def bleu_fonce():
        modif_color('#001589')
    color_bleu_fonce = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#001589",
                       activebackground='#001589',
                       text = "BLEU FONCE",
                       command = bleu_fonce)
    color_bleu_fonce.pack()
    color_bleu_fonce.place(x=largeur - 120, y=cplr_hauteur/23*14, width=120, height=cplr_hauteur/23 +1)

    #violet
    def violet():
        modif_color('#8A06C8')
    color_violet = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#8A06C8",
                       activebackground='#8A06C8',
                       text = "VIOLET",
                       command = violet)
    color_violet.pack()
    color_violet.place(x=largeur - 120, y=cplr_hauteur/23*15, width=120, height=cplr_hauteur/23 +1)

    #rose
    def rose():
        modif_color('#EF00A7')
    color_rose = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#EF00A7",
                       activebackground='#EF00A7',
                       text = "ROSE",
                       command = rose)
    color_rose.pack()
    color_rose.place(x=largeur - 120, y=cplr_hauteur/23*16, width=120, height=cplr_hauteur/23 +1)

    #magenta
    def magenta():
        modif_color('magenta')
    color_magenta = tk.Button(fenetre,
                       font=('', 12),
                       bg = "magenta",
                       activebackground='magenta',
                       text = "MAGENTA",
                       command = magenta)
    color_magenta.pack()
    color_magenta.place(x=largeur - 120, y=cplr_hauteur/23*17, width=120, height=cplr_hauteur/23 +1)

    #rose_clair
    def rose_clair():
        modif_color('#FFAADD')
    color_rose_clair = tk.Button(fenetre,font=('', 12),
                       bg = "#FFAADD",
                       activebackground='#FFAADD',
                       text = "ROSE CLAIR",
                       command = rose_clair)
    color_rose_clair.pack()
    color_rose_clair.place(x=largeur - 120, y=cplr_hauteur/23*18, width=120, height=cplr_hauteur/23 +1)

    #blanc
    def blanc():
        modif_color('#FFFFFF')
    color_blanc = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#FFFFFF",
                       activebackground='#FFFFFF',
                       text = "BLANC",
                       command = blanc)
    color_blanc.pack()
    color_blanc.place(x=largeur - 120, y=cplr_hauteur/23*19, width=120, height=cplr_hauteur/23 +1)

    #argent
    def argent():
        modif_color('#c8c8c8')
    color_argent = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#c8c8c8",
                       activebackground='#c8c8c8',
                       text = "ARGENT",
                       command = argent)
    color_argent.pack()
    color_argent.place(x=largeur - 120, y=cplr_hauteur/23*20, width=120, height=cplr_hauteur/23 +1)

    #gris
    def gris():
        modif_color('#808080')
    color_gris = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#808080",
                       activebackground='#808080',
                       text = "GRIS",
                       command = gris)
    color_gris.pack()
    color_gris.place(x=largeur - 120, y=cplr_hauteur/23*21, width=120, height=cplr_hauteur/23 +1)

    #charbon
    def charbon():
        modif_color('#424242')
    color_charbon = tk.Button(fenetre,
                       font=('', 12),
                       bg = "#424242",
                       activebackground='#424242',
                       text = "CHARBON",
                       command = charbon)
    color_charbon.pack()
    color_charbon.place(x=largeur - 120, y=cplr_hauteur/23*22, width=120, height=cplr_hauteur/23 +1)


def menu_col2():
    global menu_color
    menu_color = tk.Button(fenetre,
                           font=('', 12),
                           bg = gen_couleur,
                           activebackground= gen_couleur,
                           text = "Theme",
                           command = menu_col)
    menu_color.pack()
    menu_color.place(x=largeur - 120,y= hauteur - 80,width=120,height=35)

def modif_color(rgb):
    global para_dark_o, para_t_l, addtest_open, gen_couleur
    Label_Heure.configure(bg=rgb,activebackground=rgb)
    ligne_menu_outil_g.configure(bg=rgb,activebackground=rgb)
    ligne_menu_outil_d.configure(bg=rgb,activebackground=rgb)
    quitter_app_b.configure(bg=rgb,activebackground=rgb)
    gen_couleur = rgb
    if menu_app_ouvert == "oui":
        retour_app()
        menu_app()
    try: #reboot
        lancer_code.configure(bg=rgb,activebackground=rgb)
        if para_dark_o == 1:
            terminal_code.configure(fg = "black", bg=gen_couleur)
        else:
            terminal_code.configure( fg = "#000000")
            terminal_code.configure(fg = "#000000", bg="#ffffff")
    except:
        pass
    try:
        menu_app_b.configure(bg=rgb,activebackground=rgb)
    except:
        pass
    try:
        app_retour_b.configure(bg=rgb,activebackground=rgb)
    except:
        pass
    try:
        exit_fenetre.configure(bg=rgb,activebackground=rgb)
    except:
        pass
    try:
        main_.configure(bg=rgb,activebackground=rgb)
    except:
        pass
    try:
        para_info_q_b.configure(bg=rgb,activebackground=rgb)
    except:
        pass
    try:
        color_retour.configure(bg=rgb,activebackground=rgb)
    except:
        menu_color.configure(bg=rgb,activebackground=rgb)
    if para_app_o == 1:
        para_color_ap_b.configure(bg=rgb,activebackground=rgb)
        para_lite_b.configure(bg="gray",activebackground="gray")
        para_dark_b.configure(bg=rgb,activebackground=rgb)
        para_info_ex.configure(bg=rgb,activebackground=rgb)


    message_bvn.configure(fg= "black" )
    para_t_l = "black"
    
    try:
        if para_dark_o == 1:
            try:
                terminal__.configure(fg = rgb)
            except:
                pass
            try:
                taches__.configure(fg = rgb)
            except:
                pass
            try:
                para_titre.configure(fg = rgb)
                para_info_f.configure(fg = rgb)
            except:
                pass
            message_bvn.configure(fg= rgb )
            para_t_l = rgb
            para_lite_b.configure(bg=rgb,activebackground=rgb)
            para_dark_b.configure(bg="gray",activebackground="gray")
            para_info.configure(fg= rgb)
            para_color_ex.configure(fg = rgb)
            para_theme_ex.configure(fg = rgb)
            para_color_ba.configure(fg = gen_couleur)
            para_color_ba.configure(fg = "black", bg=gen_couleur)
        else:
            try:
                terminal__.configure(fg = "black")
            except:
                pass
            try:
                taches__.configure(fg = "black")
            except:
                pass
            para_color_ba.configure( fg = "#000000")
            para_color_ba.configure(fg = "#000000", bg="#ffffff")
    except:
        pass

        
    if addtest_open == 1:
        addtest_app_d()
        addtest_app()
    if edt_open == 1:
        edt_save_b.configure(bg=rgb,activebackground=rgb)
        edt_open_b.configure(bg=rgb,activebackground=rgb)
        if para_dark_o == 1:
            edt_titre.configure(fg = rgb)
            edt_ba.configure(fg = "black", bg=gen_couleur)
            edt_name_ba.configure(fg = "black", bg=gen_couleur)
            edt_name_ba2.configure(fg = "#000000", bg=gen_couleur)
        else:
            edt_titre.configure( fg = "#000000")
            edt_ba.configure(fg = "#000000", bg="#ffffff")
            edt_name_ba.configure(fg = "#000000", bg="#ffffff")
            edt_name_ba2.configure(fg = "#000000", bg="#ffffff")
    if mda_open == 1:
        mda_stop_b.configure(bg=rgb,activebackground=rgb)
        mda_anul_b.configure(bg=rgb,activebackground=rgb)
        mda_reboot_b.configure(bg=rgb,activebackground=rgb)
        if para_dark_o == 1:
            mda_titre.configure(fg = rgb)
        else:
            mda_titre.configure(fg = "#000000")
    if hedwige_open == 1:
        hedwige_verif_b.configure(bg=rgb,activebackground=rgb)
        hedwige_start_b.configure(bg=rgb,activebackground="gray")
        if para_dark_o == 1:
            hedwige_titre.configure(fg = rgb)
            hedwige_info.configure(fg = rgb)
            hedwige_info2.configure(fg = rgb)
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

def destroy_menu():
    try: #console
        terminal_code.destroy()
        terminal__.destroy()
        lancer_code.destroy()
    except:
        pass
    try:
        taches__.destroy()
        main_.destroy()
    except:
        pass


            #### ESSENTIAL EXPLICATION ####
            # essential est une fonction  #
            # pour placer les boutons et  #
            # lancer les fonctionalité de #
            # base de I-python, c'est une #
            # fonction car ainsi on peut  #
            # la relancer pour ne pas     #
            # avoir a reboot I-python -pf4#

def essential():
    global Label_Heure, ligne_menu_outil_g, ligne_menu_outil_d, quitter_app_b, largeur, hauteur, message_bvn, cplr_hauteur, cplr_taille, exit_fenetre, fsf

    if fsf == 1:
        largeur = fenetre.winfo_width()
        hauteur = fenetre.winfo_height()
    else:
        largeur = fenetre.winfo_screenwidth()
        hauteur = fenetre.winfo_screenheight()

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

    ligne_menu_outil_g.place(x=118,
                    y=0,
                    width=2,
                    height=hauteur)

    quitter_app_b = tk.Button(fenetre, text="quitter l'app", font=('', 12), bg = gen_couleur, activebackground=gen_couleur, command = quitter_app)
    quitter_app_b.place(x=0, y=26, width=120, height=26)

    message_bvn = tk.Label(fenetre,bg=para_c_l, fg = para_t_l, font=('', 12))
    message_bvn.pack()
    message_bvn.place(x=largeur/2 -250, y=90, width=500, height=200)
    message_bvn_()

    # caluculs pour le relatif #
    cplr_hauteur = hauteur - 80
    cplr_taille = cplr_hauteur / 23

    menu_app2()

essential()

def ressential():
    essential_destroy()
    essential()

##### TIP ######
#definition fonction de l'interpreteur
def interpreter(code):
    global dev, fsf

    if dev == 0:
        if code == "clear" or code == "CLEAR":
            sortie_ = ""
            message_bvn.config(text=sortie_)

        elif code == "news" or code == "NEWS" or code == "new" or code == "NEW" or code == "info" or code == "INFO":
            #on dit les infos
            sortie_ = version_info
            #on affiche la sortie
            message_bvn.config(text=sortie_)

        elif code == "dev 7485" or code == "DEV 7485":
            sortie_ = "Bienvenue sur le mode developpeur \n\n\n"
            message_bvn.config(text=sortie_)
            dev = 1

        elif code == "aide":
            sortie_ = "aide = afficher l'aide \n dim = affiche les dimentions de I-python \n dev **** (mdp) = mode dev \n clear = clear \n news = affiche les infos sur la version"
            message_bvn.config(text=sortie_)

        elif code == "dim" or code == "DIM":
            sortie_ = largeur,"x", hauteur
            message_bvn.config(text=sortie_)


        #si pas de commande valide
        else:
            sortie_ = "ERREUR : COMMANDE INCONNUE"
            message_bvn.config(text=sortie_)

    elif dev == 1:
        if code == "clear":
            sortie_ = "MODE DEVLOPEUR"
            message_bvn.config(text=sortie_)

        elif code == "fsf":
            fsf = 1
            fenetre.attributes('-fullscreen', False)
            sortie_ = "MODE DEVLOPEUR\nfullscreen = False"
            message_bvn.config(text=sortie_)

        elif code == "fst":
            fsf = 0
            fenetre.attributes('-fullscreen', True)
            sortie_ = "MODE DEVLOPEUR\nfullscreen = True"
            message_bvn.config(text=sortie_)

        elif code == "reb" or code == "reb 0":
            essential_destroy()
            essential()

        elif code == "reb 1":
            essential_destroy()

        elif code == "reb 2":
            essential()

        elif code == "exit":
            dev = 0
            sortie_ = "sortie du mode developpeur"
            message_bvn.config(text=sortie_)

        elif code == "aide" or code == "AIDE":
            sortie_ = "MODE DEVLOPEUR\naide = affichage de l'aide \n \n fst =fullscreen True \n fsf =fullscreen False \n exit / x = quitter le mode dev \n clear = clear l'ecran \n reb + *ARG* = reboot"
            message_bvn.config(text=sortie_)

        #si pas de commande valide
        else:
            sortie_ = "MODE DEVLOPEUR\n ERREUR : COMMANDE INCONNUE"
            message_bvn.config(text=sortie_)

### app tip #####
def console_():
    quitter_app()

    global console_open, terminal_code, terminal__, lancer_code
    #si console fermee
    if console_open == 0:
        console_open = 1

        terminal_code = tk.Entry(fenetre, width=30)
        terminal_code.insert(0, "entrez votre commande ici (taper AIDE pour commencer)")
        terminal_code.pack()
        terminal_code.place(x= 150 ,y=50,width=largeur - 300,height=20)

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

###### FIN DE TIP ######
######   GESTIONAIRE DES TACHES   ######

global ttaches
ttaches = 0

def taches_gestion_():
    destroy_menu()
    quitter_app()
    global taches__ , main_ , ttaches
    taches_gestion_
    taches__ = tk.Label(fenetre, text="Gestionnaire des taches",bg=para_c_l, fg = para_t_l, font=('', 25))

    taches__.pack()

    taches__.place(x=largeur/2 - 256,
                        y=2,
                        width=515,
                        height=40)

    main_ = tk.Button(fenetre, text="Main.py (en cours)", bg = gen_couleur, activebackground= gen_couleur, command=fenetre.destroy)

    main_.pack()

    main_.place(x=largeur/2 - 55,
                y=40,
                width=110,
                height=20)
    ttaches = 1

                ######   addtest   ######

####### ADD TEST LISTE DES VARIABLES & FONCTIONS ########
##                                                     ##
## addtest_titre -> affichage du titre de l'appli      ##
## addtest_start_b -> bonton de demarage du test       ##
## addtest_app -> fonction qui fait apparettre l'appli ##
## addtest_b -> bouton qui fait apparettre l'appli     ##
## addtest_open -> 0 = fermer / 1 = ouvert             ##
## addtest_app_d -> fonction qui detruit addtest       ##
## addtest_test -> fonction qui lance le test          ##
##                 et affiche les résultats            ##
## addtest_sc -> variable servant au calcul du test    ##
## addtest_s -> variable egal au score du pc           ##
## addtest_debut -> variable servant au calcul du test ##
## addtest_explication -> texte d'explication          ##
## addtest_result -> texte de résultat                 ##
## addtest_score -> forme le résultat en une variable  ##
## addtest_destroy -> détruit result && explication    ##
## addtest_inter -> texte d'interprétation du score    ##
##                                                     ##
#########################-pf4-###########################

def addtest_test():
    global addtest_explication, addtest_result, addtest_inter
    # le test en lui meme
    addtest_sc = 0
    addtest_debut = time.time()
    while time.time() - addtest_debut < 2:
        addtest_sc = addtest_sc + 1
    addtest_s = round(addtest_sc / 500000,1)
    # l'affichage des résultat
    addtest_destroy()
    addtest_score = "score:", addtest_s,
    addtest_result = tk.Label(fenetre, text=addtest_score,bg=para_c_l, fg = para_t_l , font=('', 12))
    addtest_result.pack()
    addtest_result.place(x=largeur/2 -256, y=100, width=515, height=40)

    addtest_inter = tk.Label(fenetre, text="moins de 5: la réactivité de votre pc est très basse\nentre 5 et 10: la réactivité de votre pc est basse\nentre 10 et 20: la réactivité de votre pc est moyenne\nentre 20 et 30: la réactivité de votre pc est bonne\nplus de 30: la réactivité de votre pc est excellente!" ,bg=para_c_l, fg = para_t_l, font=('', 12))
    addtest_inter.pack()
    addtest_inter.place(x=largeur/2 -256 , y=140, width=515, height=95)

def addtest_destroy():    # si tu tu dis que sa sert a rien d'avoir fait une fonction pour sa (se qui est logique),
    try:                  # c'est pour eviter le message d'erreur de VSC qui ne gere pas tres bien TKINTER       -pf4
        addtest_explication.destroy()
    except:
        pass
    try:
        addtest_result.destroy()
    except:
        pass
    try:
        addtest_inter.destroy()
    except:
        pass

def addtest_app():
    quitter_app()

    global addtest_titre, addtest_start_b, addtest_open, addtest_explication
    addtest_open = 1
    addtest_titre = tk.Label(fenetre, text="Add Test",bg=para_c_l, fg = para_t_l, font=('', 25))
    addtest_titre.pack()
    addtest_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    addtest_explication = tk.Label(fenetre, text="commencer par appuyer sur le bouton start\npour tester la réactivité de I-python sur votre pc",bg=para_c_l, fg = para_t_l, font=('', 12))
    addtest_explication.pack()
    addtest_explication.place(x=largeur/2 -256, y=100, width=515, height=40)

    addtest_start_b = tk.Button(fenetre, text="START", font=('', 20) , bg = gen_couleur, activebackground= "gray" , command=addtest_test)
    addtest_start_b.pack()
    addtest_start_b.place(x=largeur/2 -55, y=45, width=110, height=40)

def addtest_app_d():
    global addtest_open
    if addtest_open == 1:
        addtest_start_b.destroy()
        addtest_titre.destroy()
        addtest_destroy()
        addtest_open = 0

                ######   PARAMETRES   ######

######  PARAMETRES LISTE DES VARIABLES & FONCTIONS ######
##                                                     ##
## para_titre -> affichage du titre de l'appli         ##
## para_app -> fonction qui fait apparettre l'appli    ##
## para_b -> bouton qui fait apparettre l'appli        ##
## para_app_d -> fonction qui detruit addtest          ##
## para_color_ex -> texte pour changer couleur         ##
## para_color_ba -> barre pour taper la couleur        ##
## para_color_ap -> fonction qui applique la coulleur  ##
## para_color_ap_b -> bouton qui appel para_color_ap   ##
## para_color_er -> texte d'erreur (coulleur invalide) ##
## para_theme_ex -> texte pour changer couleur         ##
## para_lite_b -> bouton pour le theme claire          ##
## para_dark_b -> bouton pour le theme sombre          ##
## para_lite ->  fonction activer par para_lite_b      ##
## para_dark -> fonction activer par para_dark_b       ##
## para_c_l -> variable: coulleur de font des label    ##
## para_t_l -> variable: coulleur de texte des label   ##
## para_dark_o -> 0 = désactivé / 1 = activé           ##
## para_app_o -> 0 = fermer / 1 = ouvert               ##
##                                                     ##
##########################-pf4-##########################

def para_app():
    quitter_app()
    global para_color_ex, para_color_ba, para_color_ap_b, para_theme_ex, para_dark_b, para_lite_b, para_app_o, para_info, para_info_ex
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
        if rgb == "cclebug":
            for loop in range(0, 100000):
                print(loop)
            para_color_er_d()
            para_color_er = tk.Label(fenetre, text="ramener la coupe à la maison", bg=para_c_l, fg = para_t_l,font=('', 12))
            para_color_er.pack()
            para_color_er.place(x=largeur/2 -150, y=80, width=300, height=25)
        else:
            try:
                modif_color(rgb)
            except:
                para_color_er_d()
                para_color_er = tk.Label(fenetre, text="couleur invalide", bg=para_c_l, fg = para_t_l,font=('', 12))
                para_color_er.pack()
                para_color_er.place(x=largeur/2 -75, y=80, width=150, height=25)
                
    para_color_ap_b = tk.Button(fenetre, text="appliquer", bg = gen_couleur, activebackground= gen_couleur, command=para_color_ap)
    para_color_ap_b.pack()
    para_color_ap_b.place(x=largeur/2 + 137, y=60, width=70, height=20)

    para_theme_ex = tk.Label(fenetre, text="Theme:",bg=para_c_l, fg = para_t_l, font=('', 12))
    para_theme_ex.pack()
    para_theme_ex.place(x=largeur/2 - 221, y=142, width=100, height=40)

    para_lite_b = tk.Button(fenetre, text="paradise's dream",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=para_lite)
    para_lite_b.pack()
    para_lite_b.place(x=largeur/2 - 135, y=150, width=135, height=25)

    para_dark_b = tk.Button(fenetre, text="dracula night", font=('', 13) , bg = gen_couleur, activebackground=gen_couleur, command=para_dark)
    para_dark_b.pack()
    para_dark_b.place(x=largeur/2 + 15, y=150, width=115, height=25)

    para_info = tk.Label(fenetre, text="information:",bg=para_c_l, fg = para_t_l, font=('', 12))
    para_info.pack()
    para_info.place(x=largeur/2 - 140, y=234, width=100, height=40)

    para_info_ex = tk.Button(fenetre, text="afficher",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=para_info_aff)
    para_info_ex.pack()
    para_info_ex.place(x=largeur/2 - 40, y=242, width=100, height=25)

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

def para_lite():
    global para_dark_o
    theme_chang("#f0f0f0", "black")
    para_dark_o = 0
    modif_color(gen_couleur)
    if para_app_o == 1:
        para_color_ba.configure( fg = "#000000")
        para_color_ba.configure(fg = "#000000", bg="#ffffff")

def para_dark():
    global para_dark_o
    theme_chang("#171c2b", "#f2e9a7")
    para_dark_o = 1
    modif_color(gen_couleur)

def theme_chang(color, text):
    global para_c_l, para_t_l, para_app_o
    fenetre.configure(bg=color)
    message_bvn.configure(bg=color,fg= text )
    para_c_l = color
    para_t_l = text
    if para_app_o == 1:
        para_app_d()
        para_app()

def para_titre_aff():
    global para_titre
    para_titre = tk.Label(fenetre, text="Paramètres",bg=para_c_l, fg = para_t_l, font=('', 25))
    para_titre.pack()
    para_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

def para_info_q():
    try:
        para_info_f.destroy()
        para_info_q_b.destroy()
        para_titre.destroy()
    except:
        pass

def para_info_r():
    para_info_q()
    para_app()


def para_info_aff():
    global para_info_f, para_info_q_b
    para_app_d()
    para_titre_aff()

    para_info_f = tk.Label(fenetre, text=info_para,bg=para_c_l, fg = para_t_l, font=('', 12))
    para_info_f.pack()
    para_info_f.place(x=largeur/2 -250, y=90, width=500, height=200)

    para_info_q_b = tk.Button(fenetre, text="quitter",font=('', 12), bg = gen_couleur, activebackground=gen_couleur, command=para_info_r)
    para_info_q_b.pack()
    para_info_q_b.place(x=largeur/2 -255, y=hauteur - 100 , width=510, height=25)

def para_color_er_d():
    try:
        para_color_er.destroy()
    except:
        pass
def para_app_d():
    try:
        global para_app_o
        para_app_o = 0
        para_titre.destroy()
        para_color_ex.destroy()
        para_color_ba.destroy()
        para_color_ap_b.destroy()
        para_theme_ex.destroy()
        para_color_er_d()
        para_lite_b.destroy()
        para_dark_b.destroy()
        para_info_ex.destroy()
        para_info.destroy()
    except:
        pass
                ######  paramètres - FIN   ######

# lingne pour les systemes linux pour acorder les couleurs du theme
para_lite()

###################DEBUT EDITEUR DE TEXTE###################

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
# open #
    edt_open_b = tk.Button(fenetre, text="ouvrir",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=edt_open_f)
    edt_open_b.pack()
    edt_open_b.place(x=largeur/2 +20, y=hauteur - 110, width=100, height=25)

    edt_name_ba2 = tk.Entry(fenetre, width=30)
    edt_name_ba2.insert(0, "nom.extension")
    edt_name_ba2.pack()
    edt_name_ba2.place(x=largeur/2 -95, y=hauteur - 110, width=100, height=25)
# couleur #
    if para_dark_o == 1:
        edt_titre.configure(fg = gen_couleur)
        edt_ba.configure(fg = "black", bg=gen_couleur)
        edt_name_ba.configure(fg = "black", bg=gen_couleur)
        edt_name_ba2.configure(fg = "black", bg=gen_couleur)
    else:
        edt_titre.configure( fg = "#000000")
        edt_ba.configure(fg = "#000000", bg="#ffffff")
        edt_name_ba.configure(fg = "#000000", bg="#ffffff")
        edt_name_ba2.configure(fg = "#000000", bg="#ffffff")

def edt_save():
    global edt_name_ba, edt_ba
    pos1 = "0.0"
    pos2 = "end"
    nom = edt_name_ba.get()
    path = "C:\\Users\\Public\\Documents\\" + str(nom) 
    fichier_data2 = open(path, "w")
    text = edt_ba.get(pos1, pos2)
    fichier_data2.write(text)
    fichier_data2.close()

def edt_open_f():
    global edt_name_ba2, edt_ba
    try:
        nom = edt_name_ba2.get()
        path = "C:\\Users\\Public\\Documents\\" + str(nom) 
        fichier_data = open(path, "r")
        edt_ba.delete ("0.0", "end")
        edt_ba.insert(0.0, fichier_data.read())
    except:
        edt_ba.delete ("0.0", "end")
        edt_ba.insert(0.0, "pas de ficher de ce nom, réessayez (nom.extension)")

def edt_d():
    global edt_open, edt_titre
    if edt_open == 1:
        edt_titre.destroy()
        edt_ba.destroy()
        edt_save_b.destroy()
        edt_name_ba.destroy()
        edt_name_ba2.destroy()
        edt_open_b.destroy()
        edt_open = 0

###################FIN EDITEUR DE TEXTE###################

##################### MENU D'ARRET #######################

def mda_app():
    quitter_app()

    global mda_titre, mda_open, mda_stop_b, mda_anul_b, mda_reboot_b
    mda_open = 1
    mda_titre = tk.Label(fenetre, text="Menu d'arret",bg=para_c_l, fg = para_t_l, font=('', 25))
    mda_titre.pack()
    mda_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

#boutons

    mda_stop_b = tk.Button(fenetre, text="arret\nde I-python",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=quitter)
    mda_stop_b.pack()
    mda_stop_b.place(x=largeur/2 -50, y=hauteur/2 -130 , width=100, height=80)

    mda_anul_b = tk.Button(fenetre, text="annuler",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=quitter_app)
    mda_anul_b.pack()
    mda_anul_b.place(x=largeur/2 -50, y=hauteur/2 -40 , width=100, height=80)

    mda_reboot_b = tk.Button(fenetre, text="reb de\nI-python",font=('', 13), bg = gen_couleur, activebackground=gen_couleur, command=ressential)
    mda_reboot_b.pack()
    mda_reboot_b.place(x=largeur/2 -50, y=hauteur/2 +50 , width=100, height=80)

def quitter():
    fenetre.destroy()

def mda_d():
    global mda_titre, mda_open, mda_stop_b, mda_anul_b, mda_reboot_b
    if mda_open == 1:
        mda_titre.destroy()
        mda_stop_b.destroy()
        mda_reboot_b.destroy()
        mda_anul_b.destroy()
        mda_open = 0

#bouton pour quitter
exit_fenetre = tk.Button(fenetre, text='Quitter',font=('', 12),bg = gen_couleur,activebackground=gen_couleur,command = mda_app)
exit_fenetre.pack()
exit_fenetre.place(x=0,y=0,width=120,height=26)

################# fin MENU D'ARRET fin ###################
######################## hedwige #########################

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
    hedwige_text_ba.insert(0.0, "tapez ici votre mail avec uniquement des chiffre et des lettre, pas de lettre accentuées ou de charter spécieux merci")
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
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            # connexion au compte
            server.login(hedwige_email_address, hedwige_email_password)
            # envoi du mail
            server.sendmail(hedwige_email_address, hedwige_email_receiver, hedwige_email)
    except:
        pass
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

#### HEDWIGE FIN ####
#### APO #####

def apo_pt(nb):
    global apo_pt_li
    apo_pt_li[nb] = apo_pt_li[nb] + 1
    if apo_pt_li[nb] == 1:
        apo_res = "#003D2F"
    elif apo_pt_li[nb] == 2:
        apo_res = "#0ED145"
    elif apo_pt_li[nb] == 3:
        apo_res = "#C4FF0E"
    elif apo_pt_li[nb] == 4:
        apo_res = "#FFF200"
    elif apo_pt_li[nb] == 5:
        apo_res = "#FFCA18"
    elif apo_pt_li[nb] == 6:
        apo_res = "#FF9F22"
    elif apo_pt_li[nb] <= 8:
        apo_res = "#FF7F27"
    else:
        apo_res = "#EC1C24"
    return(apo_res)
   

def apo_tabl():
    global apo_tabl_1, apo_tabl_2, apo_tabl_3, apo_tabl_4, apo_tabl_5, apo_tabl_6, apo_tabl_7
    global apo_tabl_8, apo_tabl_9, apo_tabl_10, apo_tabl_11, apo_tabl_12, apo_tabl_13, apo_tabl_14
    global apo_tabl_15, apo_tabl_16, apo_tabl_17, apo_tabl_18, apo_tabl_19, apo_tabl_20, apo_tabl_21
    global apo_tabl_22, apo_tabl_23, apo_tabl_24, apo_tabl_25, apo_tabl_26, apo_tabl_27, apo_tabl_28

    def apo_menu_1():
        apo_rgb = apo_pt(1)
        apo_tabl_1.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_2():
        apo_rgb = apo_pt(2)
        apo_tabl_2.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_3():
        apo_rgb = apo_pt(3)
        apo_tabl_3.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_4():
        apo_rgb = apo_pt(4)
        apo_tabl_4.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_5():
        apo_rgb = apo_pt(5)
        apo_tabl_5.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_6():
        apo_rgb = apo_pt(6)
        apo_tabl_6.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_7():
        apo_rgb = apo_pt(7)
        apo_tabl_7.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_8():
        apo_rgb = apo_pt(8)
        apo_tabl_8.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_9():
        apo_rgb = apo_pt(9)
        apo_tabl_9.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_10():
        apo_rgb = apo_pt(10)
        apo_tabl_10.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_11():
        apo_rgb = apo_pt(11)
        apo_tabl_11.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_12():
        apo_rgb = apo_pt(12)
        apo_tabl_12.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_13():
        apo_rgb = apo_pt(13)
        apo_tabl_13.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_14():
        apo_rgb = apo_pt(14)
        apo_tabl_14.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_15():
        apo_rgb = apo_pt(15)
        apo_tabl_15.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_16():
        apo_rgb = apo_pt(16)
        apo_tabl_16.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_17():
        apo_rgb = apo_pt(17)
        apo_tabl_17.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_18():
        apo_rgb = apo_pt(18)
        apo_tabl_18.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_19():
        apo_rgb = apo_pt(19)
        apo_tabl_19.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_20():
        apo_rgb = apo_pt(20)
        apo_tabl_20.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_21():
        apo_rgb = apo_pt(21)
        apo_tabl_21.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_22():
        apo_rgb = apo_pt(22)
        apo_tabl_22.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_23():
        apo_rgb = apo_pt(23)
        apo_tabl_23.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_24():
        apo_rgb = apo_pt(24)
        apo_tabl_24.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_25():
        apo_rgb = apo_pt(25)
        apo_tabl_25.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_26():
        apo_rgb = apo_pt(26)
        apo_tabl_26.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_27():
        apo_rgb = apo_pt(27)
        apo_tabl_27.configure(bg=apo_rgb,activebackground=apo_rgb)
    def apo_menu_28():
        apo_rgb = apo_pt(28)
        apo_tabl_28.configure(bg=apo_rgb,activebackground=apo_rgb)

    apo_tabl_1 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_1)
    apo_tabl_1.pack()
    apo_tabl_1.place(x=largeur/2 - 405, y=135 , width=100, height=70)

    apo_tabl_2 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_2)
    apo_tabl_2.pack()
    apo_tabl_2.place(x=largeur/2 - 300, y=135 , width=100, height=70)

    apo_tabl_3 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_3)
    apo_tabl_3.pack()
    apo_tabl_3.place(x=largeur/2 - 155, y=135 , width=100, height=70)

    apo_tabl_4 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_4)
    apo_tabl_4.pack()
    apo_tabl_4.place(x=largeur/2 - 50, y=135 , width=100, height=70)

    apo_tabl_5 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_5)
    apo_tabl_5.pack()
    apo_tabl_5.place(x=largeur/2 + 55, y=135 , width=100, height=70)

    apo_tabl_6 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_6)
    apo_tabl_6.pack()
    apo_tabl_6.place(x=largeur/2 + 200, y=135 , width=100, height=70)

    apo_tabl_7 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_7)
    apo_tabl_7.pack()
    apo_tabl_7.place(x=largeur/2 + 305, y=135 , width=100, height=70)

    apo_tabl_8 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_8)
    apo_tabl_8.pack()
    apo_tabl_8.place(x=largeur/2 - 405, y=225 , width=100, height=70)

    apo_tabl_9 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_9)
    apo_tabl_9.pack()
    apo_tabl_9.place(x=largeur/2 - 300, y=225 , width=100, height=70)

    apo_tabl_10 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_10)
    apo_tabl_10.pack()
    apo_tabl_10.place(x=largeur/2 - 155, y=225 , width=100, height=70)

    apo_tabl_11 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_11)
    apo_tabl_11.pack()
    apo_tabl_11.place(x=largeur/2 - 50, y=225 , width=100, height=70)

    apo_tabl_12 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_12)
    apo_tabl_12.pack()
    apo_tabl_12.place(x=largeur/2 + 55, y=225 , width=100, height=70)

    apo_tabl_13 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_13)
    apo_tabl_13.pack()
    apo_tabl_13.place(x=largeur/2 + 200, y=225 , width=100, height=70)

    apo_tabl_14 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_14)
    apo_tabl_14.pack()
    apo_tabl_14.place(x=largeur/2 + 305, y=225 , width=100, height=70)

    apo_tabl_15 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_15)
    apo_tabl_15.pack()
    apo_tabl_15.place(x=largeur/2 - 405, y=315 , width=100, height=70)

    apo_tabl_16 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_16)
    apo_tabl_16.pack()
    apo_tabl_16.place(x=largeur/2 - 300, y=315 , width=100, height=70)

    apo_tabl_17 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_17)
    apo_tabl_17.pack()
    apo_tabl_17.place(x=largeur/2 - 155, y=315 , width=100, height=70)

    apo_tabl_18 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_18)
    apo_tabl_18.pack()
    apo_tabl_18.place(x=largeur/2 - 50, y=315 , width=100, height=70)

    apo_tabl_19 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_19)
    apo_tabl_19.pack()
    apo_tabl_19.place(x=largeur/2 + 55, y=315 , width=100, height=70)

    apo_tabl_20 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_20)
    apo_tabl_20.pack()
    apo_tabl_20.place(x=largeur/2 + 200, y=315 , width=100, height=70)

    apo_tabl_21 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_21)
    apo_tabl_21.pack()
    apo_tabl_21.place(x=largeur/2 + 305, y=315 , width=100, height=70)

    apo_tabl_22 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_22)
    apo_tabl_22.pack()
    apo_tabl_22.place(x=largeur/2 - 405, y=405 , width=100, height=70)

    apo_tabl_23 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_23)
    apo_tabl_23.pack()
    apo_tabl_23.place(x=largeur/2 - 300, y=405 , width=100, height=70)

    apo_tabl_24 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_24)
    apo_tabl_24.pack()
    apo_tabl_24.place(x=largeur/2 - 155, y=405 , width=100, height=70)

    apo_tabl_25 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_25)
    apo_tabl_25.pack()
    apo_tabl_25.place(x=largeur/2 - 50, y=405 , width=100, height=70)

    apo_tabl_26 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_26)
    apo_tabl_26.pack()
    apo_tabl_26.place(x=largeur/2 + 55, y=405 , width=100, height=70)

    apo_tabl_27 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_27)
    apo_tabl_27.pack()
    apo_tabl_27.place(x=largeur/2 + 200, y=405 , width=100, height=70)

    apo_tabl_28 = tk.Button(fenetre, text=" ",font=('', 11), bg = "gray", activebackground="gray", command=apo_menu_28)
    apo_tabl_28.pack()
    apo_tabl_28.place(x=largeur/2 + 305, y=405 , width=100, height=70)

    

def apo_app():
    quitter_app()

    global apo_titre, apo_open, apo_pt_li
    apo_open = 1

    apo_titre = tk.Label(fenetre, text="aide à la participation",bg=para_c_l, fg = para_t_l, font=('', 25))
    apo_titre.pack()
    apo_titre.place(x=largeur/2 -256, y=2, width=515, height=40)

    apo_pt_li= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    apo_tabl()

def apo_tabl_d():
    try:
        apo_tabl_1.destroy()
        apo_tabl_2.destroy()
        apo_tabl_3.destroy()
        apo_tabl_4.destroy()
        apo_tabl_5.destroy()
        apo_tabl_6.destroy()
        apo_tabl_7.destroy()
        apo_tabl_8.destroy()
        apo_tabl_9.destroy()
        apo_tabl_10.destroy()
        apo_tabl_11.destroy()
        apo_tabl_12.destroy()
        apo_tabl_13.destroy()
        apo_tabl_14.destroy()
        apo_tabl_15.destroy()
        apo_tabl_16.destroy()
        apo_tabl_17.destroy()
        apo_tabl_18.destroy()
        apo_tabl_19.destroy()
        apo_tabl_20.destroy()
        apo_tabl_21.destroy()
        apo_tabl_22.destroy()
        apo_tabl_23.destroy()
        apo_tabl_24.destroy()
        apo_tabl_25.destroy()
        apo_tabl_26.destroy()
        apo_tabl_27.destroy()
        apo_tabl_28.destroy()
    except:
        pass

def apo_app_d():
    global apo_open
    if apo_open == 1:
        apo_titre.destroy()
        apo_tabl_d()
        apo_open = 0

#### APO FIN ###
fenetre.mainloop()