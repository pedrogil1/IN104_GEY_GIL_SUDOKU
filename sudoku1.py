import numpy as np
from random import *
from time import *

#on stocke les grillles sous forme de matrice.

ludo=np.array([\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,3,0,8,5],\
[0,0,1,0,2,0,0,0,0],\
[0,0,0,5,0,7,0,0,0],\
[0,0,4,0,0,0,1,0,0],\
[0,9,0,0,0,0,0,0,0],\
[5,0,0,0,0,0,0,7,3],\
[0,0,2,0,1,0,0,0,0],\
[0,0,0,0,4,0,0,0,9]])

grille=np.array([\
[9,0,0,1,0,0,0,0,5],\
[0,0,5,0,9,0,2,0,1],\
[8,0,0,0,4,0,0,0,0],\
[0,0,0,0,8,0,0,0,0],\
[0,0,0,7,0,0,0,0,0],\
[0,0,0,0,2,6,0,0,9],\
[2,0,0,3,0,0,0,0,6],\
[0,0,0,2,0,0,9,0,0],\
[0,0,1,9,0,4,5,7,0]])

facile=np.array([\
[0,4,0,9,6,0,0,3,0],\
[6,1,0,7,0,3,4,0,9],\
[0,3,2,0,8,4,0,7,5],\
[0,0,4,0,0,0,0,0,7],\
[2,9,0,0,0,0,0,8,4],\
[8,0,0,0,0,0,2,0,0],\
[1,2,0,4,9,0,8,5,0],\
[4,0,9,6,0,5,0,1,3],\
[0,7,0,0,3,1,0,4,0]])

moyen=np.array([\
[0,2,0,0,9,0,4,0,0],\
[0,0,5,7,0,0,0,0,0],\
[1,8,0,0,5,4,6,0,0],\
[2,0,0,0,0,5,1,4,0],\
[9,0,0,4,0,3,0,0,6],\
[0,4,6,2,0,0,0,0,7],\
[0,0,2,6,4,0,0,1,9],\
[0,0,0,0,0,9,2,0,0],\
[0,0,9,0,1,0,0,3,0]])

diff=np.array([\
[0,0,0,2,0,6,5,4,0],\
[0,2,0,8,0,0,0,0,0],\
[0,9,4,7,0,0,6,0,0],\
[0,0,8,0,0,5,0,7,4],\
[0,0,0,0,0,0,0,0,0],\
[5,7,0,1,0,0,3,0,0],\
[0,0,3,0,0,7,2,9,0],\
[0,0,0,0,0,1,0,8,0],\
[0,8,1,3,0,9,0,0,0]])

extreme=np.array([\
[1,0,0,0,0,7,0,9,0],\
[0,3,0,0,2,0,0,0,8],\
[0,0,9,6,0,0,5,0,0],\
[0,0,5,3,0,0,9,0,0],\
[0,1,0,0,8,0,0,0,2],\
[6,0,0,0,0,4,0,0,0],\
[3,0,0,0,0,0,0,1,0],\
[0,4,0,0,0,0,0,0,7],\
[0,0,7,0,0,0,3,0,0]])

#grille trouvee sur wikipedia reputee anti forcage
antiforcage=np.array([\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,3,0,8,5],\
[0,0,1,0,2,0,0,0,0],\
[0,0,0,5,0,7,0,0,0],\
[0,0,4,0,0,0,1,0,0],\
[0,9,0,0,0,0,0,0,0],\
[5,0,0,0,0,0,0,7,3],\
[0,0,2,0,1,0,0,0,0],\
[0,0,0,0,4,0,0,0,9]])

zero=np.zeros((9,9),dtype=int)

zz=np.array([\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0]])

# dans les 4 fonctions suivantes, on implemente des fonctions pour manipuler les indices plus facilement dans certaines fonctions qui suivront notamment pour le forcage.

def pos(i,j):
    i+=1
    j+=1
    p=9*i+j
    return p
    
def position_to_indices(p):
    i=p//9
    j=p%9
    return i,j

def ligne(p):
    return p%9
    
def colonne(p):
    return p%9

#####################################################################################
#Implementation des fonctions donnant les possibilites pour une case dans la grille #
#####################################################################################

def possibilite_sur_ligne(G,i,j):
    if G[i,j]!=0:
        return []
    possible=[]
    for k in range(1,10):
        if k not in G[i]:
            possible.append(k)
    return possible


def possibilite_sur_colonne(G,i,j):
    if G[i,j]!=0:
        return []
    possible=[]
    for k in range(1,10):
        if k not in G[:,j]:
            possible.append(k)
    return possible

def possibilite_sur_carre(G,i,j):
    if G[i,j]!=0:
        return []
    p=3*(i//3)
    q=3*(j//3)
    possible=[]
    for k in range(1,10):
        if k not in G[p:p+3 , q:q+3]:
            possible.append(k)
    return possible


def possibilite_ancien(G,i,j):
#cette fonction realise l'intersection des possibilites de ligne, colonne carre pour une case donnee.
    p=3*(i//3)
    q=3*(j//3)
    G,pL=nuplet_ligne(G,i)
    pL=pL[j]
    G,pC=nuplet_colonne(G,j)
    pC=pC[i]
    G,pS=nuplet_carre(G,i,j)
    pS=pS[3*(i%3)+j%3] ## pb pour remonter a lindice
    #print(pL,pC,pS)
    possible=[]
    n=len(pL)
    for k in range(n):
        if pL[k] in pC :
            if pL[k] in pS:
                possible.append(pL[k])
    return possible

def possibilite(G,i,j):
#cette fonction realise l'intersection des possibilites de ligne, colonne carre pour une case donnee.
    pL=possibilite_sur_ligne(G,i,j)
    pC=possibilite_sur_colonne(G,i,j)
    pS=possibilite_sur_carre(G,i,j)
    possible=[]
    n=len(pL)
    for k in range(n):
        if pL[k] in pC :
            if pL[k] in pS:
                possible.append(pL[k])
    return possible

def resolution_simple(G):
#cette fonction resoud la grille en remplissant les cases n'ayant qu'une possibilite
# la variable c nous permet de savoir si la grille est modifiee apres avoir regarde les possibilites pour chaque case.
#Si la grille a ete modifiee, on analyse a nouveau la grille pour savoir s'il est possible de a remplir encore.
    c=1
    while c!=0:
        c=0
        for i in range(9):
            for j in range(9):
                possible=possibilite(G,i,j)
                if len(possible)==1:
                    G[i,j]=possible[0]
                    c+=1
    return G

#############################################
#Implementation de la resolution par forcage#
#############################################


def analyse(G):
#cette fonction permet de compter le nombre de possibilites par case
    possible=[0]*81
    for k in range(81) :
        i,j=position_to_indices(k)
        for l in possibilite(G,i,j):
                possible[k]+=1
                
    return possible



def insertsort(Lpossible):
#on utilise un algorithme de tri par insertion pour classer les cases avec le moins de possibilites pour le forcage. On est ainsi plus efficace.
    Lposition=[i for i in range(81)]
    n=len(Lpossible)
    for k in range(1,n):
        j=k
        while (j>0) and (Lpossible[j]<Lpossible[j-1]):
            Lpossible[j],Lpossible[j-1]=Lpossible[j-1],Lpossible[j]
            Lposition[j],Lposition[j-1]=Lposition[j-1],Lposition[j]
            j-=1
    return Lposition


def est_valide_finale(G,position,Lposition):
#cette fonction effecte le forcage pour les cases de la grille
    #position terminale
    if position>=81:
        return True
    #case examinee
    i,j=position_to_indices(Lposition[position])
    #test si la case est occupe
    if G[i,j]!=0 :
        return est_valide_finale(G,position+1,Lposition)
    for k in possibilite(G,i,j):
        G[i,j]=k
        if est_valide_finale(G,position+1,Lposition):
            return True
    G[i,j]=0
    return False
            
def solution(G):
#cette fonction realise la resolution de la grille en 2 temps. D'abord elle resoud à l'aide de la fonction resolution simple, puis elle termine la resolution de la grille par forcage
    debut=time()
    G=resolution_simple(G)
    Lposition=insertsort(analyse(G))
    for k in range(81):
        if est_valide_finale(G,k,Lposition):
            return G

########################
#methodes par exclusion#
########################
        
def exclusion_ligne(G,i):
    exclusion=np.array([[0,-1] for l in range(9)])
# on cree une matrice 9x2 avec : la  1ere colonne, qui grace a l'indice de la ligne de exclusion garde en memoire l'endroit ou placer le chiffre si il est unique. 
#dans la 2e colonne, on stocke l'indice de la colonne de la grille ou il y a une unique possibilite comme ca on ne fait pas trop de parcours de listes pour retrouver
#l'indice de la case avec la possibilite que l'on peut remplir avec exclusion.
    for j in range(9):
        for k in possibilite(G,i,j):
            exclusion[k-1,0]+=1
            if exclusion[k-1,0]==1:
                exclusion[k-1,1]=j
            else :
                exclusion[k-1,1]=-1
    for j in range(9):
        indice_seul=exclusion[j,1]
        if indice_seul!=-1:
            G[i,indice_seul]=j+1
    return G

def exclusion_colonne(G,j):
    exclusion=np.array([[0,-1] for l in range(9)])
    for i in range(9):
        for k in possibilite(G,i,j):
            exclusion[k-1,0]+=1
            if exclusion[k-1,0]==1:
                exclusion[k-1,1]=i
            else :
                exclusion[k-1,1]=-1
    for i in range(9):
        indice_seul=exclusion[i,1]
        if indice_seul!=-1:
            G[indice_seul,j]=i+1
    return G

def exclusion_carre(G,r,s):
    p=3*(r//3)
    q=3*(s//3)
    exclusion=np.array([[0,-1,-1] for l in range(9)])
    for i in range(p,p+3):
        for j in range(q,q+3):
            for k in possibilite(G,i,j):
                exclusion[k-1,0]+=1
                if exclusion[k-1,0]==1:
                    exclusion[k-1,1]=i
                    exclusion[k-1,2]=j
                else :
                    exclusion[k-1,1]=-1
                    exclusion[k-1,2]=-1
    for k in range(9):
        i=exclusion[k,1]
        j=exclusion[k,2]
        if i!=-1:
            G[i,j]=k+1
    return G

 
ligne=np.array([[0,1,0,3,4,0,6,7,8]])
colonne=np.transpose(ligne)
carre=np.array([[1,2,3],[4,0,6],[7,8,9]])



def resolution_medium(G):
#resolution avec methode par exclusion. Similaire a la resolution simple, on utilise une variable c
#pour savoir si a l'issu d'un tour de boucle la grille evolue.
    c=1
    while c!=0:
        c=0
        for i in range(9):
            for j in range(9):
                possible=possibilite(G,i,j)
                if len(possible)==1:
                    G[i,j]=possible[0]
                    c+=1
                Q=np.copy(G) 
                G=exclusion_ligne(G,i)
                G=exclusion_colonne(G,j)
                G=exclusion_carre(G,i,j)
                if np.array_equal(G,Q)==False:
                    c+=1
    return G

def solution2(G):
#avec methodes simple, par exclusion et tri pour le forcage.
    debut=time()
    G=resolution_simple(G)
    G=resolution_medium(G)
    Lposition=insertsort(analyse(G))
    for k in range(81):
        if est_valide_finale(G,k,Lposition):
            return G
        
################################################
#implementation de forcage par n-uplet exclusif#
################################################

def nuplet_ligne(G,i):
    matrice_des_possibilites=[]
    for j in range(9): # on cree une liste de listes regroupant les possibilites
        matrice_des_possibilites.append(possibilite(G,i,j))

    n_uplets=[]
    
    for h in range(0,9): #cette partie permet de regrouper les cases ayant les memes possibilites
        equals=[h]
        n_uplets.append(equals)
        for j in range(h,9):#a noter que les comparaisons se font astucieusement, on ne recompare pas les cases qui precedent
            if matrice_des_possibilites[h]!=[]:
                if matrice_des_possibilites[h]==matrice_des_possibilites[j]:
                    n=len(n_uplets)
                    for k in range(n):
                        if j not in n_uplets[k]: #on ajoute dans equals l'indice (celui de la colonne suffit) des cases ayant les memes possibilites que G(i,h) 
                                equals.append(j)           
        del(n_uplets[-1]) # on supprime l'element [h] de nuplets pour evetuellement ajouter une liste avec les indices des cases formant un nuplet
        if len(equals)>1:
            n_uplets.append(equals)                 
    n=len(n_uplets)
    for j in range(n): 
        indice_colonne=n_uplets[j][0]
        if len(n_uplets[j])==len(matrice_des_possibilites[indice_colonne]): # c'est ici que s'effectue le test n-uplet n exclusif
           
            for k in range(9):  # ici on elimine les possibilites des autres cases dans le cas ou on obtient un n uplet n exclusif
                if k not in n_uplets[j]:
                    for l in matrice_des_possibilites[indice_colonne] :
                         if l in matrice_des_possibilites[k]:
                             matrice_des_possibilites[k].remove(l)
    
    for j in range(9): # on remplit la grille si les n uplets n exclusifs n'ont laisses qu'une possibilite dans une case
        if len(matrice_des_possibilites[j])==1:
            #G[i][j]=matrice_des_possibilites[j][0]
            del(matrice_des_possibilites[j][-1])
    return G,matrice_des_possibilites # on renvoie la grille et la matrice des possibilites pour pouvoir operer la resolution avec des possibilites restreintes


def nuplet_colonne(G,i):
# nous nous sommes rendu compte que par un simple jeu de transpositions il etait facile de realiser nuplets_colonne a partir de nuplet ligne 
    Q=np.copy(G)
    Q=np.transpose(Q)
    R,matrice_des_possibilites=nuplet_ligne(Q,i)
    return np.transpose(R),matrice_des_possibilites


def nuplet_carre(G,r,s):
    p=3*(r//3)
    q=3*(s//3)
    matrice_des_possibilites=[]
    for i in range(p,p+3):
        for j in range(q,q+3):
            matrice_des_possibilites.append(possibilite(G,i,j))
            
    n_uplets=[]
    
    for h in range(0,9): 
        equals=[h]
        n_uplets.append(equals)
        for j in range(h,9):
            if matrice_des_possibilites[h]!=[]:
                if matrice_des_possibilites[h]==matrice_des_possibilites[j]:
                    n=len(n_uplets)
                    for k in range(n):
                        if j not in n_uplets[k]: 
                                equals.append(j)           
        del(n_uplets[-1]) 
        if len(equals)>1:
            n_uplets.append(equals)                 
    n=len(n_uplets)
    for j in range(n): 
        indice_colonne=n_uplets[j][0]
        if len(n_uplets[j])==len(matrice_des_possibilites[indice_colonne]): 
           
            for k in range(9):  
                if k not in n_uplets[j]:
                    for l in matrice_des_possibilites[indice_colonne] :
                         if l in matrice_des_possibilites[k]:
                             matrice_des_possibilites[k].remove(l)
    
    for j in range(9): 
        if len(matrice_des_possibilites[j])==1:
            t=p+j//3 # on remplit le carre
            u=q+j%3
            #G[t][u]=matrice_des_possibilites[j][0]
            del(matrice_des_possibilites[j][-1])

    return G,matrice_des_possibilites


def resolution_difficile(G):
    G=resolution_simple(G)
    G=resolution_medium(G)
    c=1
    while c!=0:
        c=0
        for i in range(9):
            for j in range(9):
                possible=possibilite(G,i,j)
                if len(possible)==1:
                    G[i,j]=possible[0]
                    c+=1
                Q=np.copy(G)
                G,a=nuplet_ligne(G,i)
                G,a=nuplet_colonne(G,j)
                G,a=nuplet_carre(G,i,j)
                if np.array_equal(G,Q)==False:
                    c+=1
    return G

def solution3(G):
#avec methodes simple, par exclusion, par nuplet exclusif et tri pour le forcage.
    debut=time()
    G=resolution_difficile(G)
    Lposition=insertsort(analyse(G))
    for k in range(81):
        if est_valide_finale(G,k,Lposition):
            return G

###################
#Fonctions annexes#
###################

def verification(G):
# cette fonction permet de verifier si la grille est correcte
    one=[1 for i in range(9)]
    for i in range(9):
        verifL=[0 for i in range(9)]
        verifC=[0 for i in range(9)]
        for j in range(9):
            verifL[G[i,j]-1]+=1
            verifC[G[j,i]-1]+=1
        if verifL!=one or verifL!=one:
            return False
    return True

                    
def createur_sudoku():
#pour creer un sudoku, on cree une grille vide, on insere un chiffre aleatoire
#dans une case aleatoirement choisie puis on resoud la grille. Enfin, on supprime
#un nombre aleatoire de chiffres de la grille. Cela nous garantit bien que la grille sera faisable.
    G=np.array([\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,0,0,0,0,0,0,0,0]])
    a=randint(0,80)
    i,j=position_to_indices(a)
    b=randint(1,9)
    G[i,j]=b
    G=solution2(G)
    p=randint(0,80)
    Lpossibilite=[i for i in range(81)]
    for k in range(p):
        q=choice(Lpossibilite)
        Lpossibilite.remove(q)
        i,j=position_to_indices(q)
        G[i,j]=0
    return G

def evaluateur_difficulte(G):
#On estime la difficulte d'une grille en fonction de la complexite des techniques utilisees.
    G1=np.copy(G)
    G2=np.copy(G)
    G3=np.copy(G)
    G4=np.copy(G)
    G1=resolution_simple(G1)
    G2=resolution_medium(G2)
    G3=solution2(G3)
    G4=resolution_difficile(G4)
    if np.array_equal(G1,G3):
        return("grille facile")
    if np.array_equal(G2,G3):
        return("grille medium")
    if np.array_equal(G4,G3):
        return("grille difficile")
    else :
        return("grille extreme")
#rajouter un menu grille aleatoire et un menu save avec creation et sauvegarde du fichier

exclu=np.array([\
    [9, 6, 7, 1, 3, 2, 4, 8, 5],\
    [4, 3, 5, 8, 9, 7, 2, 6, 1],\
    [8, 1, 2, 6, 4, 5, 3, 9, 7],\
    [1, 2, 6, 4, 8, 9, 7, 5, 3],\
    [5, 9, 8, 7, 1, 3, 6, 2, 4],\
    [7, 4, 3, 5, 2, 6, 8, 1, 9],\
    [2, 7, 9, 3, 5, 8, 1, 4, 6],\
    [6, 5, 4, 2, 7, 1, 9, 3, 8],\
    [3, 8, 1, 9, 6, 4, 5, 7, 2]])
