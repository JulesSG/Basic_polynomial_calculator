"""
Estrutura de datos:
polinomio = [[grado,coeficiente],[grado,coeficiente],[grado,coeficiente],...]
"""

def agrePoli():# Esta funcion se encarga de crear un polinomio a partir de la estrutura de datos definida.
    poli = []
    grado = int(input("Dijite el gradomas alto del polinomio: "))
    print("Si uno de los terminos ax^n no existe en el polinomio, dijitar 0 en los espacios\n")
    for i  in range(grado + 1):
        grado =int (input(f"ingrese el gradro del {i + 1} termino: "))
        coefi= int (input(f"ingrese el coeficiente del {i + 1} termino: "))
        if coefi != 0:
            poli.append([grado,coefi])
    return poli

def cargarMemoria(): #Esta funcion se ejecuta 1 vez al empezar el programa, carga los polinomios en momoria al programa.
    try:
         global polis # en esta lista se guardan los polinomios, es una variable global para su facil acceso.
         polis = []
         l = open("Polinomios.txt", "r")
         for i in l:
             poli = []
             for j in i.split("/"):
                 aux = j.split(";")
                 poli.append(aux)
             poli.pop()
             polis.append(poli)
    except:
        pass # el bloque try-except se encarga de que el programa no se cuelgue si no hay datos que cargar.

def escrMemoria(poli): # esta funcion se encarga de cargar los polinomios a memoria secundaria.
    l = open("Polinomios.txt", "a")
    aux=""
    for i in poli:
        aux+=f"{i[0]};{i[1]}/"
    print(aux)
    l.write(aux+"\n")
def impresora(i):# esta funcion se encarga de acomodar los polinomios en su forma canonica para imprimirlos en pantalla.
    aux = ""
    for j in i:
        if int(j[1]) > 0:

            if int(j[0]) == 0:
                aux = aux + f"+{j[1]} "
            elif int(j[0]) == 1:
                aux = aux + f"+{j[1]}X "
            else:
                aux = aux + f"+{j[1]}X^{j[0]} "
        else:
            if int(j[0]) == 0:
                aux = aux + f"{j[1]} "
            elif int(j[0]) == 1:
                aux = aux + f"{j[1]}X "
            else:
                aux = aux + f"{j[1]}X^{j[0]} "
    return aux

def verDatos():# esta funcion se encarga de enumerar e imprimir los polinomios en memoria secundaria.
    cont = 0
    for i in polis:
        aux = impresora(i)
        cont += 1
        print(f"{cont}. " + aux+"\n")

def evaluaPol(x, poli): # esta funcion se encarga de evaluar un numero en un polinomio y calcular el resultado .
    resul = 0
    for i in poli:
        resul += int(i[1])*pow(int(x), int(i[0]))
    return resul
def ordenarPoli(poli): # Esta funcion ordena los polinomios de manera decendiente segun su grado
    for i in range(len(poli)-1):
        for j in range((len(poli)-1)):
            if int(poli[j + 1][0]) > int(poli[j][0]):
                aux = poli[j]
                poli[j] = poli[j + 1]
                poli[j + 1] = aux
    return poli

def suma(poli): # esta funcion suma 2 polinomios
    resul = []
    aux = []
    for i in poli[0]:
        centinela = 0
        for j in poli[1]:
            if i[0] == j[0]:
                centinela += 1
                aux.append(poli[1].index(j))
                resul.append([i[0], int(i[1])+int(j[1])])
        if centinela == 0:
            resul.append(i)
    for i in poli[1]:
        if poli[1].index(i) not in aux:
            resul.append(i)
    return impresora(ordenarPoli(resul))

def resta(poli): #esta funcion resta 2 polinomios
    resul = []
    aux = []
    for i in poli[0]:
        centinela = 0
        for j in poli[1]:
            if i[0] == j[0]:
                centinela += 1
                aux.append(poli[1].index(j))
                resul.append([i[0], int(i[1]) - int(j[1])])
        if centinela == 0:
            resul.append(i)
    for i in poli[1]:
        if poli[1].index(i) not in aux:
            resul.append([i[0],-1*int(i[1])])
    return impresora(ordenarPoli(resul))
def multi(poli): #esta funcion multiplica 2 polinomios
    resul = []
    for i in poli[0]:
        for j in poli[1]:
            resul.append([int(i[0])+int(j[0]),int(i[1]*int(j[1]))])
    return impresora(simpliPoli(ordenarPoli(resul)))
def simpliPoli(poli): #esta funcion simplifica al maximo un polinomio
    grado = poli[0][0]+1
    resul = []
    for i in range(grado):
        aux = 0
        for j in poli:
            if int(j[0]) == i:
                   aux += int(j[1])
        if aux != 0:
            resul.append([i,aux])
    return ordenarPoli(resul)

def main(): #esta es la funcion principal y la encargada de ejecutar el menu
    cargarMemoria()
    while True:# se hace un ciclo infinito para que el menu se repita hasta que el usuario desee salir
        print("\nAgregar polinomio a memoria.....1\n"
              "Sumar polinomios................2\n"
              "Restar polinomios...............3\n"
              "Multiplicar polinomios..........4\n"
              "Evaluar polinomio...............5\n"
              "Ver polinomios en memoria.......6\n"
              "Salir...........................7\n")

        op = int(input("Dijite una opcion: "))

        if op == 1:
            poli = agrePoli()
            polis.append(poli)
            escrMemoria(poli)
            wait = input("El polinomio se guardo correctamente, presione enter para continuar...")
        elif op == 2:
           poli = []
           for i in range(2):
               aux = input("Si desea usar un polinomio en memoria presione \"y\": ")
               if aux == 'y':
                   numPoli = int(input("Dijite el numero del polinomio que desea usar: "))
                   poli.append(polis[numPoli - 1])
               else:
                   print("Por favor ingresar el polinomio")
                   poli.append(agrePoli())
           try:
                 print(f"El resultado de la suma de polinomios es: {suma(poli)}")
                 wait = input("Presione enter para continuar...")
           except IndexError:
               print("Los polinomio ingresados no se encuentran en memoria")

        elif op == 3:
            poli = []
            print("Favor ingresar los polinomios en orden a restar p1 - p2\n")
            for i in range(2):
                aux = input("Si desea usar un polinomio en memoria presione \"y\": ")
                if aux == 'y':
                    numPoli = int(input("Dijite el numero del polinomio que desea usar: "))
                    poli.append(polis[numPoli - 1])
                else:
                    print("Por favor ingresar el polinomio")
                    poli.append(agrePoli())
            try:
                print(f"El resultado de la resta de polinomios es: {resta(poli)}")
                wait = input("Presione enter para continuar...")
            except IndexError:
                print("Los polinomio ingresados no se encuentran en memoria")
        elif op == 4:
            try:
                poli = []
                for i in range(2):
                    aux = input("Si desea usar un polinomio en memoria presione \"y\": ")
                    if aux == 'y':
                        numPoli = int(input("Dijite el numero del polinomio que desea usar: "))
                        poli.append(polis[numPoli - 1])
                    else:
                        print("Por favor ingresar el polinomio")
                        poli.append(agrePoli())
                print(f"El resultado de la multiplicacion de polinomios es: {multi(poli)}")
                wait = input("Presione enter para continuar...")
            except IndexError:
                print("Los polinomio ingresados no se encuentran en memoria")
        elif op == 5:
           try:
               aux = input("Si desea usar un polinomio en memoria presione \"y\": ")
               if aux == 'y':
                   numPoli = int(input("Dijite el numero del polinomio que desea usar: "))
                   poli = polis[numPoli - 1]
                   print(poli)
               else:
                   print("Por favor ingresar el polinomio")
                   poli = agrePoli()
               x = int(input("Dijite el numero con el que desea evaluar el polinomio: "))
               print(f"El resultado de evaluar {x} en el polinomio es: {evaluaPol(x, poli)}")
               wait = input("Presione enter para continuar...")
           except IndexError:
               print("Los polinomio ingresados no se encuentran en memoria")
        elif op == 6:
            verDatos()
            wait = input("Presione enter para continuar...")
        else:
            break

main()# se llama a la funcion principal