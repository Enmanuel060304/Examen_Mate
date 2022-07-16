''' Importamos librerias y funciones a utilizar '''
from cs50 import get_float, get_int
import math
from os import system


''' Definimos funcion principal '''
def main():

    ''' funcion portada pinta la portada de nuestra '''
    Portada()


    ''' Utilizamos un while (True) porque en python no existe el do while '''
    while True:
        print("---------->Elija una Opcion<-----------")
        print("1.Pasar al Menu.")
        print("2.Salir del programa.")
        opc = get_int("Digite su opcion Aqui-------> ")

        if (opc == 1):
            while True:
                menu()
                op = get_int("Digite una opcion-----> ")
                calculo(op)


                print(" ")
                print("¿Desea calcular algo mas?")
                print("1.Si")

                print("2.No")
                op = get_int("Digite una opcion------->")
                if op == 2:
                    print("Usted ha Salido del Programa")
                    exit()

        elif(opc == 2):
            print("--------->Usted ha Salido del Programa<------------")
            exit()
        else:
            print("Elija Una Opcion Valida")

''' Definimos funcion que imprime en pantalla la portada de nuestro proyecto '''
def Portada():
    system("clear")
    print(" ")
    print("\t\tUNIVERSIDAD NACIONAL DE INGENIERIA")
    print(" ")
    print("\t███████    █████████████████████████████    ███████")
    print("\t███████    █████████████████████████████    ███████")
    print("\t███████    █████████████████████████████    ███████")
    print("\t███████    ███████               ███████")
    print("\t███████    ███████    ███████    ███████    ███████")
    print("\t███████    ███████    ███████    ███████    ███████")
    print("\t███████    ███████    ███████    ███████    ███████")
    print("\t███████    ███████    ███████    ███████    ███████")
    print("\t███████               ███████    ███████    ███████")
    print("\t█████████████████████████████    ██████████████████")
    print("\t█████████████████████████████    ██████████████████")
    print("\t█████████████████████████████    ██████████████████")
    print(" ")

    print("\t\tPROYECTO FINAL DE MATEMATICA II")
    print(" ")
    print("\t\t\tIntegrantes: ")
    print("            Br.Jose Enmanuel Urbina Fierro 2021-0269U")
    print("            Br.Justin Steven Aburto Guevara 2021-0239U")
    print(" ")
    print("\t\t\t   Fecha: ")
    print("\t\t    24 de Junio de 2022")
    print(" ")
    print("\t\t     Managua, Nicaragua")
    print(" ")
    print(" ")


''' definimos funcion que imprime en pantalla las funciones que el programa puede calcular '''
def menu():
    system("clear")
    print("//////////////////////////////////////")
    print("-------->Menu de Opciones<------------")
    print("1.Calcular Seno.")
    print("2.Calcular Coseno.")
    print("3.Calcular Tangente.")
    print("4.Calcular Secante.")
    print("5.Calcular Cosecante")
    print("6.Calcular Cotangente")
    print("7.Calcular Logaritmo Natural.")
    print("8.Calcular Exponencial.")
    print("9.Calcular Log")
    print("10.Salir")
    print("///////////////////////////////////////")


''' definimos funcion que calcula e imprime los resultados del calculo de aproximacion en las funciones '''
def calculo(opcion):

    ''' Opcio 1 calcula la aproximacion a funcion seno '''
    if opcion == 1:
        system("clear")
        print("--------------->Sen(x)<----------------------")
        angulo = 0.0
        while True:
            angulo = get_float("Ingresa angulo -----> ")
            if validar_angulo(angulo):
                break
        print("Sen(",Angulos_Especiales(angulo),") = ",Taylor_Seno(angulo))


    elif opcion == 2:
        system("clear")
        print("--------------->Cos(x)<----------------------")
        angulo = 0.0
        while True:
            angulo = get_float("Ingresa angulo -----> ")
            if validar_angulo(angulo):
                break
        print("Cos(",Angulos_Especiales(angulo),") = ",Taylor_Coseno(angulo))

    elif opcion == 3:
        system("clear")
        print("--------------->Tan(x)<----------------------")
        angulo = 0.0
        while True:
            angulo = get_float("Ingresa angulo -----> ")
            if validar_angulo(angulo):
                break
        print("Tan(",Angulos_Especiales(angulo),") = ",Taylor_Tangente(angulo))

    elif opcion == 4:
        system("clear")
        print("--------------->Sec(x)<----------------------")
        angulo = 0.0
        while True:
            angulo = get_float("Ingresa angulo -----> ")
            if validar_angulo(angulo):
                break
        print("Sec(",Angulos_Especiales(angulo),") = ",Taylor_Secante(angulo))

    elif opcion == 5:
        system("clear")
        print("--------------->Csc(x)<----------------------")
        angulo = 0.0
        while True:
            angulo = get_float("Ingresa angulo -----> ")
            if validar_angulo(angulo):
                break
        print("Csc(",Angulos_Especiales(angulo),") = ",Taylor_CoSecante(angulo))

    elif opcion == 6:
        system("clear")
        print("--------------->Cot(x)<----------------------")
        angulo = 0.0
        while True:
            angulo = get_float("Ingresa angulo -----> ")
            if validar_angulo(angulo):
                break
        print("Cot(",Angulos_Especiales(angulo),") = ",Taylor_CoTangente(angulo))

    elif opcion == 7:
        system("clear")
        print("--------------->Ln(x)<----------------------")
        x = Rango_Convergencia_Ln()
        print("Ln(",x,") = ",Taylor_LogaritmoNa(x))

    elif opcion == 8:
        system("clear")
        print("--------------->exp(x)<----------------------")
        x = get_int("Ingresa un Numero -----> ")
        print("exp(",x,") = ",Taylor_Exponencial(x))

    elif opcion == 9:
        system("clear")
        print("--------------->Log(x)<----------------------")
        x = Rango_Convergencia_Ln()
        print("Log(",x,") = ",Taylor_Log(x))

    elif opcion == 10:
        print("----->Haz seleccionado la opcion salir<----------")
        exit()
    else:
        print("Opcion no Valida")


''' con esta funcion validamos que si el angulo que ingreso pertenece a la familia de los radianes '''
def validar_angulo(angulo):

    if (angulo == 0.000000):
        return True
    elif angulo == 30.000000:
        return True
    elif angulo == 45.000000:
        return True
    elif angulo == 60.000000:
        return True
    elif angulo == 90.000000:
        return True
    elif angulo == 120.000000:
        return True
    elif angulo == 135.000000:
        return True
    elif angulo == 150.000000:
        return True
    elif angulo == 180.000000:
        return True
    elif angulo == 210.000000:
        return True
    elif angulo == 225.000000:
        return True
    elif angulo == 240.000000:
        return True
    elif angulo == 270.000000:
        return True
    elif angulo == 300.000000:
        return True
    elif angulo == 315.000000:
        return True
    elif angulo == 330.000000:
        return True
    elif angulo == 360.000000:
        return True
    else:
        return False


def Taylor_Seno(angulo):

    angulo = math.radians(angulo)
    angulo = round(angulo,4)
    print("nuevo valor de angulo: ",angulo)

    ''' inicializo sumatoria en 0 '''
    seno = 0.0

    for k in range(27):
        seno += (-1)**k * angulo**(2 * k + 1) / math.factorial((2 * k + 1))
        seno = round(seno,3)

    return seno

def Taylor_Coseno(angulo):
    angulo = math.radians(angulo)

    angulo = round(angulo,4)
    print("valor del angulo en radianes: ",angulo)
    coseno = 0.0

    for k in range(27):
        coseno += (-1)**k * angulo ** (2 * k) / math.factorial((2 * k))
        coseno = round(coseno, 3)

    return coseno

def Taylor_Exponencial(angulo):
    angulo = round(angulo, 4)
    exponencial = 0.0

    for k in range(27):
        exponencial += angulo** k / math.factorial(k)

    return round(exponencial,3)

def Taylor_Tangente(angulo):
    if angulo == 270.000000:
        return "Indeterminado"

    if angulo == 90.000000:
        return "Indeterminado"

    Tangente = Taylor_Seno(angulo) / Taylor_Coseno(angulo)
    return round(Tangente,3)

def Taylor_CoSecante(angulo):
    if (angulo == 0.000000):
        return "Indeterminado"

    if (angulo == 180.000000):
        return "Indeterminado"

    if (angulo == 360.000000):
        return "Indeterminado"

    Cosecante = 0.0
    Cosecante = 1/Taylor_Seno(angulo)
    return round(Cosecante,3)

def Taylor_Secante(angulo):
    if (angulo == 90.000000):
        return "Indeterminado"

    if (angulo == 270.000000):
        return "Indeterminado"
    secante = 1/Taylor_Coseno(angulo)
    return round(secante,3)

def Taylor_LogaritmoNa(x):
    ln = 0.0
    k = 1
    while True:
        ln += math.pow(-1,k+1) * math.pow(x-1,k)/k
        k+=1

        if k == 27:
            break

    return round(ln,4)

def Taylor_Log (x):
    log = Taylor_LogaritmoNa(x) * 0.43429
    return round(log,4)

def Taylor_CoTangente(angulo):
    if (angulo == 0.000000):
        return "Indeterminado"

    if (angulo == 180.000000):
        return "Indeterminado"

    if (angulo == 360.000000):
        return "Indeterminado"

    cotag = Taylor_Coseno(angulo) / Taylor_Seno(angulo)
    return round(cotag,3)

def Angulos_Especiales (angulo):

    if (angulo == 0.000000):
        return "0"

    if angulo == 30.000000:
        return "π/6"

    if angulo == 45.000000:
        return "π/4"

    if angulo == 60.000000:
        return "π/3"

    if angulo == 90.000000:
        return "π/2"

    if angulo == 120.000000:
        return "2π/3"

    if angulo == 135.000000:
        return "3π/4"

    if angulo == 150.000000:
        return "5π/6"

    if angulo == 180.000000:
        return "π"

    if angulo == 210.000000:
        return "7π/6"

    if angulo == 225.000000:
        return "5π/4"

    if angulo == 240.000000:
        return "4π/3"

    if angulo == 270.000000:
        return "3π/2"

    if angulo == 300.000000:
        return "5π/3"

    if angulo == 315.000000:
        return "7π/4"

    if angulo == 330.000000:
        return "11π/6"

    if angulo == 360.000000:
        return "2π"

def Rango_Convergencia_Ln():
    limite = 0.0

    while True:
        limite = get_float("Valor de x: ")

        if limite > 0 and limite < 2:
            break
    return limite


main()