import tkinter as tk
import numpy as np
import sudoku1
from tkinter import filedialog

grille1=np.array([\
[9,0,0,1,0,0,0,0,5],\
[0,0,5,0,9,0,2,0,1],\
[8,0,0,0,4,0,0,0,0],\
[0,0,0,0,8,0,0,0,0],\
[0,0,0,7,0,0,0,0,0],\
[0,0,0,0,2,6,0,0,9],\
[2,0,0,3,0,0,0,0,6],\
[0,0,0,2,0,0,9,0,0],\
[0,0,1,9,0,4,5,7,0]])

height = 450
width  = 450
size_square = 50


#pour faire le menu

def open_sudoku():
#grace a une boite de dialogue on demande a l'utilisateur d'ouvrir une grille stockee en format .txt
        file = tk.filedialog.askopenfilename(initialdir = "~/",title = "Select file",filetypes = (("texte files","*.txt"),("all files","*.*")))
        file=open(file)
        tableau=file.readlines()
        file.close()
        n=len(tableau)
        # on cree des variables globales pour utiliser les fonctions
        global sudoku
        global Q
        sudoku=[]
        for i in range(n-9,n):
                lignetableau=tableau[i].strip()
                lignetableau=lignetableau.split(',')
                ligne=[0 for k in range(9)]
                for j in range(9):
                        ligne[j]=int(lignetableau[0][j])
                sudoku.append(ligne)
        print("Open !")
        sudoku=np.array(sudoku)
        Q=np.copy(sudoku)
        draw_sudoku(canvas,sudoku) #on dessine le sudoku

def open_random():
#cette fonction permet d'ouvrir 
        global sudoku
        global Q
        sudoku=sudoku1.createur_sudoku()
        Q=np.copy(sudoku)
        draw_sudoku(canvas,sudoku)


def solve():
        print("Solve !")
        grille=sudoku1.solution2(sudoku)
        draw_sudoku2(canvas,grille) #permet d'ajouter les chiffres completes en rouge
        


def initWin(window):
        canvas = tk.Canvas(window,width=width,height=height)
        canvas.pack()
        menu_bar = tk.Menu(window)
        filemenu = tk.Menu(menu_bar)
        filemenu.add_command(label="Open", command=open_sudoku)
        filemenu.add_command(label="Open random", command=open_random)
        filemenu.add_command(label="Save", command=save)
        filemenu.add_command(label="Solve", command=solve)
        filemenu.add_command(label="Difficulty evaluator", command=difficulty)
        menu_bar.add_cascade(label="Menu interactif", menu=filemenu)
        window.config(menu=menu_bar)
        return canvas

def draw_grid(canvas):
	for i in range(0,10):
		if i%3 == 0:
			canvas.create_line(i*size_square, 0,i*size_square, size_square*9,width=3)
			canvas.create_line(0,i*size_square, size_square*9,i*size_square,width=3)
		else:
			canvas.create_line(i*size_square, 0,i*size_square, size_square*9,width=1)
			canvas.create_line(0,i*size_square, size_square*9,i*size_square,width=1)

def clear_grid(canvas):
	canvas.delete("all")
	draw_grid(canvas)


def draw_sudoku(canvas,G):
        for i in range(len(G)):
                for j in range(len(G[1])):
                        if (G[i][j] != 0):
                                canvas.create_text(size_square/2+50*j,size_square/2+50*i,text=str(G[i][j]))

def draw_sudoku2(canvas,G):
#permet de remlir en rouge les chiffres issus de la resolution
        for i in range(9):
                for j in range(9):
                        if Q[i,j]==0 :
                                canvas.create_text((2*j+1)*size_square/2,(2*i+1)*size_square/2,text=str(G[i,j]),fill='red') 

def difficulty():
#evaluateur de difficulte
        print("Difficulté estimée :",sudoku1.evaluateur_difficulte(sudoku))

def save():
        nom=input("Nom de la grille (n'oubliez le .txt) : ")
        n=len(nom)
        print(nom)
        while nom[n-4:]!=".txt" :
                print("l'extension n'a pas ete entree correctement")
                nom=input("Nom de la grille (n'oubliez le .txt surtout !) :")
                n=len(nom)
                print(nom)
        f = open(nom,'w')
        for i in range(9):
                for j in range(9):
                        f.write(str(sudoku[i,j]))
                f.write('\n')
        f.close()
        print("Saved in the current repository <3 ! ")
        
if __name__ == '__main__':
	
	window = tk.Tk()
	canvas = initWin(window)
	draw_grid(canvas)
	window.mainloop()
