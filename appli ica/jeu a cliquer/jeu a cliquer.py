
import cytron

global nb
nb = 0

cytron.cy_mkdir("/cytron/sys/app/", "sauvegardes_jeu_a_cliquer")

try:
    nb = int(cytron.cy_rfil_rela("/cytron/sys/app/sauvegardes_jeu_a_cliquer/", "save.txt"))
except:
    cytron.cy_mkfil("/cytron/sys/app/sauvegardes_jeu_a_cliquer/", "save.txt", nb)

def func():
    global nb
    nb += 1
    bouton.config(text=nb)

global bouton
bouton = tk.Button(fenetre, text=nb,font=('', 30), bg = "gray", activebackground="gray", command=func)
bouton.pack()
bouton.place(x=largeur/2-200, y=300 , width=400, height=70)

def off():
    def stop():
        global bouton
        bouton.destroy()
        global nb
        cytron.cy_mkfil("/cytron/sys/app/sauvegardes_jeu_a_cliquer/", "save.txt", nb)

    while True:
        if icai_off == True:
            try:
                stop()
            except:
                pass
        else:
            time.sleep(0.2)
start_new_thread( off,())