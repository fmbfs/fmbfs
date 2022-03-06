import os
from compare_mp3 import compare
from tkinter import Tk
#from tkinter import filedialog as fd
from tkinter.filedialog import askdirectory

#para contar o tempo de execussao
import time
start = time.time()

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
#para visualmente termos nocao de quantos ficheiros do total ja comparou
count = 1

t = len(lista_atual)
#para correr o loop x vezes igual ao numero de ficheiros
for filename in lista_atual:
    
    print(f'{count} de {len(lista_atual)}')

    #se o ficheiro a for mp3
    if filename.endswith('.mp3'):    
        a = directory + "/" + filename
        #print(lista_atual.index(filename))

        #para saltar indices repetidos
        for i in range(1, t):
            if i == lista_atual.index(filename):
                break
            #se o ficheiro b for mp3
            if lista_atual[i - t].endswith('.mp3'):
                print("\nFicheiro A:", a)
                #adiciona o path do ficheiro b
                b = directory + "/" + lista_atual[i - t]
                print("Ficheiro B:", b)
                print('\n')

                #executa a comparacao dos mp3
                #se igual acrescenta a lista de repetidos
                #senao volta ao inicio
                if str(compare(a, b)) == 'Result.SAME_FILE':
                    print('Ficheiros iguais, anexando B para remover...')
                    print('\n')
                    lista_reps.append(b)            

                else:            
                    print('\nFicheiros diferentes, nada removido!\n')
            else:
                print('Ficheiro não é .MP3!\n')
                continue
    else:
        print('Ficheiro não é .MP3!\n')
        continue
    count +=1
    t -= 1
#para remover duplicados na lista
#dict.fromkeys ou set
mylist = list(dict.fromkeys(lista_reps))
print("LISTA reps:\n", mylist)


for repetidos in mylist:
    os.remove(repetidos)

print('\nQuantidade ficheiros: ', len(lista_atual))
print('\n')
print("LISTA ATUAL:\n", lista_files())
end = time.time()
print("Tempo total decorrido: ", end - start)
