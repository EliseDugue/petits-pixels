
from tkinter import * #on importe tkinter

nbps=5 # nombre de cases (grille carree)
c=70 # dimension d'une case supposee carree
x0,y0=20,20 #coordonnees du point en haut a gauche
x1,y1=400,20 #coordonnees du point en haut a gauche de la 2nde grille
couleur=["#99CCCC","#505050"] #bleu;gris
M_sol = [] #initialisation de la grille


#initialisation des variables
test=0
nb_victoires=0
exe=0

##zones bleues et blanches##

dessin=Tk()
dessin.title("Petits pixels")

can= Canvas(dessin,height=500,width=800,bg="#99CCCC")
can.pack(side=LEFT,fill=BOTH)

frame1=Frame(dessin,bg="#FEFEFE",width=500,height=200)
frame1.pack(side=TOP)

frame2=Frame(dessin,bg="#FEFEFE",width=500,height=1000)
frame2.pack(side=BOTTOM)

#on importe les photos&smileys##

smileyvert=PhotoImage(file="smiley2.gif")
smileyrouge=PhotoImage(file="smiley.gif")

croix=PhotoImage(file="gif_croix.gif")
quitter=PhotoImage(file='quitter.gif')
recommencer=PhotoImage(file='recommencer.gif')
arrow=PhotoImage(file='arrow.gif')

niveau1=PhotoImage(file='niveau1.gif')
niveau2=PhotoImage(file='niveau2.gif')
niveau3=PhotoImage(file='niveau3.gif')
niveau4=PhotoImage(file='niveau4.gif')
niveau5=PhotoImage(file='niveau5.gif')
niveau6=PhotoImage(file='niveau6.gif')
niveau7=PhotoImage(file='niveau7.gif')
niveau8=PhotoImage(file='niveau8.gif')
niveau9=PhotoImage(file='niveau9.gif')
niveau10=PhotoImage(file='niveau10.gif')
niveau11=PhotoImage(file='niveau11.gif')
niveau12=PhotoImage(file='niveau12.gif')


v=PhotoImage(file='victoire.gif')
pluie=PhotoImage(file='pluie.gif')

#on place les smileys dans leur cadre

labsmileyr=Label(frame1, image=smileyrouge)
labsmileyr.grid(row=0, column=0)
labsmileyr2=Label(frame1, image=smileyrouge)
labsmileyr2.grid(row=0, column=1)
labsmileyr3=Label(frame1, image=smileyrouge)
labsmileyr3.grid(row=0, column=2)

labsmiley=Label(frame1, image=smileyvert)
labsmiley.grid(row=0, column=0)
labsmiley2=Label(frame1, image=smileyvert)
labsmiley2.grid(row=0, column=1)
labsmiley3=Label(frame1, image=smileyvert)
labsmiley3.grid(row=0, column=2)

fleche=can.create_image(650,300,image=arrow)

#fonctions diverses et variees##

### creation des niveaux 5*5 de 1 à 12 ###

def debut_niveau():
    global M
    global fleche
    
    can.delete(fleche)
    
    for i in range(nbps+1):
        can.create_rectangle(20,20,370,370,fill="#99CCCC")
        can.create_rectangle(400,20,750,370,fill="#99CCCC")

    for i in range(nbps+1):
        can.create_line(x1+c*i, y1,x1+c*i,y1 + nbps*c)
        can.create_line(x1, y1+c*i,x1+nbps*c ,y1+c*i)

    M = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

def grille_niv1():

    debut_niveau()

    global M_sol
    global exe

    exe=1


    M_sol = [[1,0,0,0,1],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [1,0,0,0,1]]
    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])


def grille_niv2():

    debut_niveau()

    global M_sol
    global exe

    exe=2

    M_sol = [[0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv3():
    
    debut_niveau()

    global M_sol
    global exe

    exe=3

    M_sol = [[0,1,0,1,0],
            [1,0,1,0,1],
            [0,1,0,1,0],
            [1,0,1,0,1],
            [0,1,0,1,0]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv4():
    
    debut_niveau()

    global M_sol
    global exe

    exe=4

    M_sol = [[1,0,0,0,1],
            [1,1,0,0,1],
            [1,0,1,0,1],
            [1,0,0,1,1],
            [1,0,0,0,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv5():
    
    debut_niveau()

    global M_sol
    global exe

    exe=5
    
    M_sol = [[1,1,1,1,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv6():
    
    debut_niveau()

    global M_sol
    global exe

    exe=6

    M_sol = [[1,1,1,1,1],
            [1,0,0,0,0],
            [1,1,1,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv7():
    
    debut_niveau()

    global M_sol
    global exe

    exe=7

    M_sol = [[1,1,1,1,1],
            [1,0,0,0,0],
            [1,1,1,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv8():
    
    debut_niveau()
    
    global M_sol
    global exe

    exe=8

    M_sol = [[1,1,1,1,1],
            [1,0,0,0,0],
            [1,0,1,1,1],
            [1,0,0,0,1],
            [1,1,1,1,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv9():
    
    debut_niveau()
    
    global M_sol
    global exe

    exe=9

    M_sol = [[1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv10():
    

    debut_niveau()
    
    global M_sol
    global exe
    
    exe=10

    M_sol = [[1,1,1,1,1],
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,0,0,1,0],
            [1,1,1,1,0]]
    
    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv11():
    
    debut_niveau()
    
    global M_sol
    global exe

    exe=11

    M_sol = [[0,1,0,0,1],
            [0,1,0,1,0],
            [0,1,1,0,0],
            [0,1,0,1,0],
            [0,1,0,0,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])

def grille_niv12():
    
    debut_niveau()
    
    global M_sol
    global exe

    exe=12

    M_sol = [[1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1]]

    print("M_sol = " ,M_sol, "\n")
    for i in range (nbps):
        for j in range (nbps):
            can.create_rectangle(x0+c*j,y0+c*i,x0+(j+1)*c,y0+(i+1)*c, fill=couleur[M_sol[i][j]])


def tester(): #sert à définir une erreur, à la montrer puis à retirer une vie
    
    global test
    global gameover
    global gm

    gameover=Label(frame1,text="Fin de la partie",font=("comic",14,))

    if test==0:
        victoire()
    
    if test==1:
        labsmiley.configure(image=smileyrouge)
        print ("une vie en moins", "\n")
        victoire()

    elif test==2:
        labsmiley2.configure(image=smileyrouge)
        print("2 vies en moins", "\n")
        victoire()
 
    elif test==3:
        labsmiley3.configure(image=smileyrouge)
        gameover.grid(row=2, column=1)
        print("3 vies en moins")
        print("game over", "\n")

        gm=can.create_image(400,325,image=pluie)
        
        dessin.after(1000, reset)
        
    else:
        print("ne pas perdre de vie", "\n")

def victoire(): #sert à montrer à l'utilisateur qu'il a réussi le niveau et execute le niveau suivant

    global gg
    global nb_victoires
    
    if M==M_sol:

        nb_victoires=nb_victoires+1
        
        print("et c'est le GG")
        gameover.configure(text="Tu as gagné!!")
        gameover.grid(row=2, column=1)

        gg=can.create_image(400,325,image=v)

        if nb_victoires==exe==1 :
            b3.configure(state=NORMAL)
            
        if nb_victoires>=2 and exe==2 :
            b4.configure(state=NORMAL)
            
        if nb_victoires>=3 and exe==3:
            b5.configure(state=NORMAL)
            
        if nb_victoires>=4 and exe==4:
            b6.configure(state=NORMAL)
            
        if nb_victoires>=5 and exe==5:
            b7.configure(state=NORMAL)
            
        if nb_victoires>=6 and exe==6:
            b8.configure(state=NORMAL)
            
        if nb_victoires>=7 and exe==7:
            b9.configure(state=NORMAL)
            
        if nb_victoires>=8 and exe==8:
            b10.configure(state=NORMAL)
            
        if nb_victoires>=9 and exe==9:
            b11.configure(state=NORMAL)
            
        if nb_victoires>=10 and exe==10:
            b12.configure(state=NORMAL)
            
        if nb_victoires>=11 and exe==11:
            b13.configure(state=NORMAL)

        if nb_victoires>=12 and exe==12:
            print("t'as fini le jeu bg!")
            
        
        dessin.after(1000, reset)

def monquitter(): #sert à quitter le jeu
    dessin.quit()
    dessin.destroy()

def reset(): #sert à vider les grilles pour recommencer et choisir un niveau

    global test
    global exe
    global fleche

    gameover.destroy()

    if M==M_sol:
        can.delete(gg)
    else:
        can.delete(gm)
    
    
    test=0
    exe=0

    print("test=",test,)
    print("niveau joué=",exe, "\n")
    
    labsmiley.configure(image=smileyvert)
    labsmiley2.configure(image=smileyvert)
    labsmiley3.configure(image=smileyvert)
    

    for i in range(nbps+1):
        can.create_rectangle(20,20,370,370,fill="#99CCCC")
        can.create_rectangle(400,20,750,370,fill="#99CCCC")

    fleche=can.create_image(600,470,image=arrow)


# programme principal : s'execute à chaque clic dans le canveas bleu

### fonction de correspondance

def correspond(x,y):
    return ((y-y1)//c,(x-x1)//c)

def programme_principal(event):

    global test
    global exe
    global M

    (i,j)=correspond(event.x,event.y)

    if i in range(nbps) and j in range (nbps):

        if M_sol[i][j]==1:
            can.create_rectangle(x1+j*c,y1+i*c,x1+j*c+c,y1+i*c+c,fill="#505050")

            M[i][j]=1

        else:
            can.create_image(x1+j*c+c/2,y1+i*c+c/2,image=croix)
            test=test+1

        print ("test=",test,)
        print ("niveau joué=",exe,)
        print('M=',M, "\n")

    tester()


#boutons##
b1=Button(frame2,image=quitter,command=monquitter)
b2=Button(frame2,image=niveau1,command=grille_niv1)
b3=Button(frame2,image=niveau2,command=grille_niv2)
b4=Button(frame2,image=niveau3,command=grille_niv3)
b5=Button(frame2,image=niveau4,command=grille_niv4)
b6=Button(frame2,image=niveau5,command=grille_niv5)
b7=Button(frame2,image=niveau6,command=grille_niv6)
b8=Button(frame2,image=niveau7,command=grille_niv7)
b9=Button(frame2,image=niveau8,command=grille_niv8)
b10=Button(frame2,image=niveau9,command=grille_niv9)
b11=Button(frame2,image=niveau10,command=grille_niv10)
b12=Button(frame2,image=niveau11,command=grille_niv11)
b13=Button(frame2,image=niveau12,command=grille_niv12)
b14=Button(frame2,image=recommencer,command=reset)

#placement des boutons
b1.grid(row=5,column=2)
b2.grid(row=0,column=0)
b3.grid(row=0,column=1)
b4.grid(row=0,column=2)
b5.grid(row=1,column=0)
b6.grid(row=1,column=1)
b7.grid(row=1,column=2)
b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=3,column=0)
b12.grid(row=3,column=1)
b13.grid(row=3,column=2)
b14.grid(row=5,column=1)

b3.configure(state=DISABLED)
b4.configure(state=DISABLED)
b5.configure(state=DISABLED)
b6.configure(state=DISABLED)
b7.configure(state=DISABLED)
b8.configure(state=DISABLED)
b9.configure(state=DISABLED)
b10.configure(state=DISABLED)
b11.configure(state=DISABLED)
b12.configure(state=DISABLED)
b13.configure(state=DISABLED)

#execution
can.bind("<Button-1>",programme_principal)

dessin.mainloop()
