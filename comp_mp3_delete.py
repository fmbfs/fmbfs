import os
from compare_mp3 import compare
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter.filedialog import askdirectory


#FUNCTIONS
def lista_files():
    lista = []
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            lista.append(filename)
        
    #print('Ficheiros: ', lista)
    return lista

#MAIN

directory = askdirectory(title='Select Folder of origin') # shows dialog box and return the path
#print(directory)
#destination = askdirectory(title='Select Folder of destination')
#print(destination)

lista_atual = lista_files()
#print(lista_atual)
#print('\n')

#lista em branco para os repetidos
lista_reps = []

print('\nQuantidade ficheiros: ', len(lista_atual))


#para correr o loop x vezes igual ao numero de ficheiros
for filename in lista_atual: 
        
    a = directory + "/" + filename
    #print(lista_atual.index(filename))

    #para saltar indices repetidos
    for i in range(0, len(lista_atual)):
        if i == lista_atual.index(filename):
            break

        print("\nFicheiro A:", a)
        b = directory + "/" + lista_atual[i]
        print("Ficheiro B:", b)
        print('\n')

        if str(compare(a, b)) == 'Result.SAME_FILE':
            print('Ficheiros iguais, anexando B para remover...')
            print('\n')
            lista_reps.append(b)            

        else:            
            print('\nFicheiros diferentes, nada removido!\n')

#para remover duplicados na lista
mylist = list(dict.fromkeys(lista_reps))
print("LISTA reps:\n", mylist)


for repetidos in mylist:
    os.remove(repetidos)

print('\nQuantidade ficheiros: ', len(lista_atual))
print('\n')
print("LISTA ATUAL:\n", lista_files())

