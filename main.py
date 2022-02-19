from tkinter import *
import time
from tkinter.messagebox import *

f = Tk()
p = PanedWindow(f, orient=HORIZONTAL)

canvas = Canvas(width=400, height=300, bg='deep sky blue')

canvas.create_oval(120,120,150,150,width=5,fill='red')
canvas.create_oval(145,120,175,150,width=5,fill='red')
canvas.create_oval(170,120,200,150,width=5,fill='red')
canvas.create_oval(195,120,225,150,width=5,fill='red')

canvas.create_text(200,80,fill="darkorange",font=('Comic Sans MS',25),text="Puissance 4")
canvas.create_text(180,200,fill="darkblue",font=('Comic Sans MS',15),text="Developpé par : \n allagui abdessalem")

p.add(canvas)

mg= [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
# mg : matrice graphique
ms=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#ms : matrice statique

sj=False    #sortir de jeux
joueur='2'  #identification de joueur debut par joueur 1

#les scores
s1=0
s2=0
sm=0

def mscore():
    showinfo("Meilleur Score","Meilleur Score : "+str(sm)+" ! \n ⚪⚪⚪⚪ ")

def aide():
    showinfo("Comment joueur","Le joueur qui gangne celui le premier qui \n"
            "aligne 4 points Horizontalement ou \n verticalemnt  ou diagonal")


def apropos():
    showinfo("A propos de jeux","Puissance 4 ⚪⚪⚪⚪ \n "
        " Cette jeux est developpé par \n Allagui abdessalem FIA1-01 \n "
        "en tantque projet de tp paradigmes \n © 2020-2021 ")

#une methode qui fait le mise a jour de score
def score():
    global sm
    global s1
    sm=s1
    f = open("score.txt", "rt")
    ch=int(f.readline())
    f.close()
    if sm>ch:
        f = open("score.txt", "wt")
        f.write(str(sm))
        f.close()
    else:
        sm=ch
        f.close()
    c.configure(text="Meilleur Score :" + str(sm), bg="light blue")
    f.close()



#une methode pour verifir chaque tour s'il y'a 4 cercles horizontale  vertical ou diagonale
def verifier(x):
    global mg
    global ms
    global sj


    for i in range(6):
        for j in range(4):
            if ms[i][j]==ms[i][j+1]==ms[i][j+2]==ms[i][j+3]==x:
                mg[i][j].configure(bg="red")
                mg[i][j + 1].configure(bg="red")
                mg[i][j + 2].configure(bg="red")
                mg[i][j + 3].configure(bg="red")
                return True
    for j in range(7):
        for i in range(3):
            if ms[i][j]==ms[i+1][j]==ms[i+2][j]==ms[i+3][j]==x:
                mg[i][j].configure(bg="red")
                mg[i+1][j].configure(bg="red")
                mg[i+2][j].configure(bg="red")
                mg[i+3][j].configure(bg="red")
                return True

    for i in range(3):
        if ms[0+i][0+i] == ms[1+i][1+i] == ms[2+i][2+i] == ms[3+i][3+i] == x:
            mg[0+i][0+i].configure(bg="red")
            mg[1+i][1+i].configure(bg="red")
            mg[2+i][2+i].configure(bg="red")
            mg[3+i][3+i].configure(bg="red")
            return True
        if ms[0+i][i+1] == ms[1+i][2+i] == ms[2+i][3+i] == ms[3+i][4+i] == x:
            mg[0+i][1+i].configure(bg="red")
            mg[1+i][2+i].configure(bg="red")
            mg[2+i][3+i].configure(bg="red")
            mg[3+i][4+i].configure(bg="red")
            return True
    for i in range(3):
        if ms[0+i][6-i] == ms[1+i][5-i] == ms[2+i][4-i] == ms[3+i][3-i] == x:
            mg[0+i][6-i].configure(bg="red")
            mg[1+i][5-i].configure(bg="red")
            mg[2+i][4-i].configure(bg="red")
            mg[3+i][3-i].configure(bg="red")
            return True
        if ms[0 + i][5 - i] == ms[1 + i][4 - i] == ms[2 + i][3 - i] == ms[3 + i][2 - i] == x:
            mg[0 + i][5 - i].configure(bg="red")
            mg[1 + i][4 - i].configure(bg="red")
            mg[2 + i][3 - i].configure(bg="red")
            mg[3 + i][2 - i].configure(bg="red")
            return True
    for i in range(2):
        if ms[0+i][4-i] == ms[1+i][3-i] == ms[2+i][2-i] == ms[3+i][1-i] == x:
            mg[0+i][4-i].configure(bg="red")
            mg[1+i][3-i].configure(bg="red")
            mg[2+i][2-i].configure(bg="red")
            mg[3+i][1-i].configure(bg="red")
            return True
        if ms[1+i][6-i] == ms[2+i][5-i] == ms[3+i][4-i] == ms[4+i][3-i] == x:
            mg[1+i][6-i].configure(bg="red")
            mg[2+i][5-i].configure(bg="red")
            mg[3+i][4-i].configure(bg="red")
            mg[4+i][3-i].configure(bg="red")
            return True
        if ms[2][0]==ms[3][1]==ms[4][2]==ms[5][3]==x:
            mg[2][0].configure(bg="red")
            mg[3][1].configure(bg="red")
            mg[4][2].configure(bg="red")
            mg[5][3].configure(bg="red")
            return True
        if ms[0+i][2+i]==ms[1+i][3+i]==ms[2+i][4+i]==ms[3+i][5+i]==x:
            mg[i][2+i].configure(bg="red")
            mg[1+i][3+i].configure(bg="red")
            mg[2+i][4+i].configure(bg="red")
            mg[3+i][5+i].configure(bg="red")
            return True
        if ms[1+i][0+i]==ms[2+i][i+1]==ms[3+i][i+2]==ms[4+i][i+3]==x:
            mg[1+i][i].configure(bg="red")
            mg[2+i][i+1].configure(bg="red")
            mg[3+i][2+i].configure(bg="red")
            mg[4+i][3+i].configure(bg="red")
            return True
        if ms[0][3] == ms[1][4] == ms[2][5] == ms[3][6] == x:
            mg[0][3].configure(bg="red")
            mg[1][4].configure(bg="red")
            mg[2][5].configure(bg="red")
            mg[3][6].configure(bg="red")
            return True
        if ms[0][3] == ms[1][2] == ms[2][1] == ms[3][0] == x:
            mg[0][3].configure(bg="red")
            mg[1][2].configure(bg="red")
            mg[2][1].configure(bg="red")
            mg[3][0].configure(bg="red")
            return True
        if ms[2][6] == ms[3][5] == ms[4][4] == ms[5][3] == x:
            mg[2][6].configure(bg="red")
            mg[3][5].configure(bg="red")
            mg[4][4].configure(bg="red")
            mg[5][3].configure(bg="red")
            return True

    finJeux()
    return False


def jouer(r,c): # r,c les cordonnes de case joué
    global joueur
    global sj
    global mg
    global ms
    global s1
    global s2
    if joueur=="1" and ms[r][c]==0 and sj==False : # si cette case est vide
        z.configure(text="⚫ joueur " + str(joueur), bg="dark orange") # on cauche la case
        mg[r][c].configure(text='⚪',bg='white')
        ms[r][c]=1
        s1=s1+7 # augmentation de variable de score
        d.configure(text="Score :" + str(s1), bg="cyan")  # mise a jour le la score grphiquement

        joueur="2"   # on laisse le tour pour le deuxieme joueur  2 prochaine tour
        sj=verifier(1) # verifier s'il y a un gangnant
        finJeux()      # finir le jeux au cas de gangnant ou null
    if joueur=="2" and ms[r][c]==0 and sj==False :
        z.configure(text="⚪ joueur " + str(joueur), bg="yellow")
        mg[r][c].configure(text='⚫',bg='white')
        ms[r][c] =2
        s2=s2+7
        joueur= "1" # on laisse le tour pour le deuxieme joueur 1 prochaine tour
        sj = verifier(2) # verifier s'il y a un gangnant
        finJeux()     # finir le jeux au cas de gangnant ou null

def init():
    # cette mathode consiste a initialiser les variables a chaque nouvelle partie
    global sj
    global joueur
    global mg
    global ms
    global s1
    global s2
    d.configure(text="Score :" + str(0), bg="light blue")
    z.configure(text="premier tour :\n ⚪ joueur " + str(joueur), bg="gray")
    s1,s2=0,0
    score()
    sj = False
    joueur = '1'
    for i in range(6):
        for j in range(7):
            mg[i][j]=Button(Frame2,font=('Arial',15),bg='cornsilk2',command=lambda r=i , c=j :jouer(r,c),height=1,width=3)
            mg[i][j].grid(row=i,column=j)
            ms[i][j]=0



def finJeux():
    #cette methode sera invoque a la fin de jeux pour afficher le resultat et commencer une nouvelle partie
    global ms
    global sj
    if sj:
        showinfo('Fin de jeux', 'joueur '+str(joueur)+" gagné  !\nScore :"+str(s1) )
        if askyesno('Nouvelle partie', 'Commencer une nouvelle partie?'):
            score()
            init()
    else:
        for i in range(6):
            for j in range(7):
                if ms[i][j]==0:
                   return False
        showinfo('Fin de jeux', 'fin de jeux !  \n  ni joueur1 ni joueur 2 gagné \n Partie null' )
        if askyesno('Nouvelle partie', 'Commencer une nouvelle partie?'):
            score()
            init()



def ajoutFrame():
    #cette methode pour supprimer le canavas d'intro au jeux et afficher le jeux lui meme
    global p
    global Frame1
    global Frame2
    global menubar
    canvas.destroy()
    f.config(menu=menubar)
    p.add(Frame1)
    p.add(Frame2)
#-----------fin les methodes


#---------------configuration de menu----------------
menubar = Menu(f)

menu1 = Menu(menubar, tearoff=0,font=('Comic Sans MS',8))
menu1.add_command(label="Nouvelle Partie", command=init,font=('Comic Sans MS',8))
menu1.add_command(label="Meilleur Score", command=mscore,font=('Comic Sans MS',8))
menu1.add_separator()
menu1.add_command(label="Quitter", command=f.quit,font=('Comic Sans MS',8))
menubar.add_cascade(label="Options de jeux", menu=menu1,font=('Comic Sans MS',8))

menu2 = Menu(menubar, tearoff=0,font=('Comic Sans MS',8))
menu2.add_command(label="A propos",command=apropos,font=('Comic Sans MS',8))
menubar.add_cascade(label="A propos",command=apropos, menu=menu2,font=('Comic Sans MS',8))

menu3 = Menu(menubar, tearoff=0,font=('Comic Sans MS',8))
menu3.add_command(label="Aide",command=aide,font=('Comic Sans MS',8))
menubar.add_cascade(label="Aide", menu=menu3 ,font=('Comic Sans MS',8))


#---------------fin de configuration de menu----------------
f['bg'] = 'black'
p.pack(side=TOP, expand=Y, pady=2, padx=2)

#configuaration des frames

# frame 1

Frame1 = Frame(f, borderwidth=1, relief=GROOVE,background='light blue',width=250,height=250)

Frame2 = Frame(f, borderwidth=1, relief=GROOVE,background='cornsilk2',width=400,height=380)
z=Label(Frame1,font=('Comic Sans MS',10),bg='cornsilk2',height=3,width=12)
a=Label(Frame1,font=('Comic Sans MS',10),bg='cornsilk2',height=3,width=12)
a.grid(row=5,column=5)
a.configure(text="joueur courant :",bg="light blue")
z.grid(row=10,column=5)
c=Label(Frame1,font=('Comic Sans MS',8),bg='cornsilk2',height=3,width=15)
c.grid(row=20,column=5)
score()
c.configure(text="Meilleur Score :"+str(sm),bg="light blue")
d=Label(Frame1,font=('Comic Sans MS',8),bg='cornsilk2',height=3,width=15)
d.configure(text="Score :"+str(s1),bg="light blue")
d.grid(row=25,column=5)
p.after(3000,ajoutFrame)



#fin configuaration des frames
f['bg']='black'
f.title('Puissance 4') #titre de la fenetre
f.wm_iconbitmap('icon.ico') # icon de la fenetre




init() # initalisation  de jeux


f.mainloop() # affichage de la fenetre
