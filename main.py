import matplotlib.pyplot as plt
import numpy as np
import math

contador_iteraciones = 0

blanco = "\033[37m"
fondoRojo = "\033[41m"
quitarColor = "\u001B[0m"


#Metodo de biseccion

def main():
    opcion: int = 0
    while opcion != 5:
        print("||---------------------------------------------------||")
        print("||              SELECCIONE OPCION                    ||")
        print("||              1. Raices ecua. cuadratica           ||")
        print("||              2. Metodo Biseccion UMG              ||")
        print("||              3. Metodo Newton-Rapson              ||")
        print("||              4. Metodo Newton-Rapson Modificado   ||")
        print("||              5. SALIR                             ||")
        print("||---------------------------------------------------||\n")
        opcion = int(input("Su opcion es: "))
        if opcion == 1:
            valores_de_x1_y_x2_con_formula_cuadratica()
        if opcion == 2:
            metodoBiseccionUMGIniciador()
        if opcion == 3:
            metodoNewtonRapsonIniciador()
        if opcion == 4:
            metodoNewtonRapsonModificadoIniciador()

    print("Gracias por usar este programa")


def valores_de_x1_y_x2_con_formula_cuadratica():
    print("Este programa pide los coeficientes de ecuaciones"
          + " cuadraticas para determinarlas mediante la formula: \n"
          + " (-b+√b^2-4ac)/2a y (-b-√b^2-4ac)/2a")

    es_compleja: bool = False

    a = 0
    while a == 0:
        a = int(input("Ingrese el coeficiente a: "))
        if a == 0:
            print("Este coeficiente no puede ser 0")

    b = int(input("Ingrese el coeficiente b: "))
    c = int(input("Ingrese el coeficiente c: "))

    temp_inside_sqr = (b ** 2) - (4 * a * c)

    if temp_inside_sqr < 0:
        es_compleja = True
        temp_inside_sqr *= -1

    temp_sqr = math.sqrt(temp_inside_sqr)
    temp_b_f = (-b) / (2 * a)
    temp_b_sqr = temp_sqr / (2 * a)

    if es_compleja:
        print("La respuesta de los coeficientes ingresados es: ")
        print(blanco + f"X1 = {temp_b_f} + {temp_b_sqr}i")
        print(f"X2 = {temp_b_f} - {temp_b_sqr}i{quitarColor}")
    else:
        print("La respuesta de los coeficientes ingresados es: ")
        print(blanco + f"X1 = {temp_b_f - temp_b_sqr}")
        print(f"X2 = {temp_b_f + temp_b_sqr}{quitarColor}")

##################################################################################


def metodoBiseccionUMGIniciador():

    print("Este programa busca las raices de una funcion"
          " por medio del metodo de Biseccion \n"
          "Ingrese valores para: \n")
    # """Paso 1"""

    Xl: float = float(input("Xl (inferior): "))
    Xu: float = float(input("Xu (superior): "))

    #math.
    #Cambiar en caso de ser necesario
    fXl: float = ((math.e ** (3*Xl)) - 4)
    fXu: float = ((math.e ** (3*Xu)) - 4)

    #print(f"f(Xl) = {fXl}")
    #print(f"f(Xu) = {fXu}")

    if not (fXl * fXu < 0):
         print(f"Los valores Xl = {Xl} y Xu = {Xu} no son validos ")
         metodoBiseccionUMGIniciador()
    else:

        print("||==================||")
        print("|| Iteracion No. 0  ||")
        print("||==================||")

        print(f"Primer Xl = {Xl}")
        print(f"f(Xl) = {fXl}")
        print(f"Primer Xu = {Xu}")
        print(f"f(Xu) = {fXu}")

        """Paso 2"""
        Xr: float = (Xl + Xu) / 2
        print(f"Primer Xr = {Xr}")

        # Cambiar en caso de ser necesario
        fXr: float = ((math.e ** (3*Xr)) - 4)

        print(f"f(Xr) = {fXr}")

        contador_IteracionesEsCero()
        """Paso 3"""
        # A
        if fXl * fXr < 0:
            metodoBiseccionUMG(Xl, Xr, 3, Xr)
        # B
        elif fXl * fXr > 0:
            metodoBiseccionUMG(Xr, Xu, 3, Xr)
        # C
        elif fXl * fXr == 0:
            print(f"La raiz esta en {Xr}")


def metodoBiseccionUMG(Xl: float, Xu: float, errorAbs: float, XrAnterior:float):
    """
    Valor inicial inferior Xl
    Valor inicial superior Xu
    comparamos f(x)
    sustituimos x
    Xr = (Xl + Xu) / 2

    PASOS:
    1. Elija valores iniciales para inferior Xl y superior Xu, que encierren la
    raiz (primero se puede graficar la funcion y luego elegir los valores), de tal
    forma que la funcion cambie de signo en el intervalo
    Esto se verifica comprobando que f(Xl) * f(Xu) < 0.
    2. Una aproximacion de la raiz x, se determina mediante:
        Xr = (Xl + Xu) / 2
    3. Realice las siguientes evaluaciones para determinar en que subintervalo
    esta la raiz:
        a. Si f(Xl) * f(Xr) < 0, entonces la raiz se encuentra dentro del subintervalo
        inferior izquierdo. Por lo tanto haga Xu = Xr, y vuelva al paso 2.
        b. Si f(Xl) * f(Xr) > 0, entonces la raiz se encuentra dentro del subintervalo
        superior derecho. Por lo tanto haga Xl = Xr, y vuelva al paso 2.
        c. Si f(Xl) * f(Xr) = 0, la raiz es igual a Xr; terminar el calculo

    CRITERIO DE PARO Y ESTIMACIONES DE ERRORES
    SI NO SE LLEGA A f(Xl) * f(Xu) = 0, ENTONCES SE CALCULA UN ERROR ESPERADO.
    POR LO REGULAR SE RECOMEINDA QUE E = 0.0001%, pero depende del problema
    La ecuacion para determinar cuanto de Error tenemos es:
        E = |(XrNuevo - XrAnterior) / XrNuevo| * 100%
    """



    #Error, hasta donde vamos a llegar?
    #Cambiar en caso de ser necesario
    error:float = 0.001

    print("-----------------------------------")
    if error<=errorAbs:

        iteracion = contador_IteraccionesMetodo()

        print("||==================||")
        print(f"|| Iteracion No. {iteracion}  ||")
        print("||==================||")

        #Cambiar en caso de ser necesario
        fXl:float = ((math.e ** (3*Xl)) - 4)
        fXu:float = ((math.e ** (3*Xu)) - 4)

        print(f"Xl = {Xl}")
        print(f"f(Xl) = {fXl}")
        print(f"Xu = {Xu}")
        print(f"f(Xu) = {fXu}")

        """Paso 2"""
        Xr:float = (Xl + Xu) / 2
        print(f"Xr = {Xr}")

        #Cambiar en caso de ser necesario
        fXr: float = ((math.e ** (3*Xr)) - 4)

        print(f"f(Xr) = {fXr}")

        errorNuevo: float = calcularError(Xr, XrAnterior)
        print(f"Error Actual = {errorNuevo}")

        """Paso 3"""
        #A
        if fXl * fXr < 0:
            metodoBiseccionUMG(Xl, Xr, errorNuevo, Xr)
        #B
        elif fXl * fXr > 0:
            metodoBiseccionUMG(Xr, Xu, errorNuevo, Xr)
        #C
        elif fXl * fXr == 0:
            print(f"La raiz esta en {Xr}")
    else:
        print(f"La raiz es aproximadamente: {XrAnterior}")

###################################################################################

def metodoNewtonRapsonIniciador():

    print("Este programa busca las raices de una funcion"
          " por medio del metodo de Newton-Rapson \n"
          "Ingrese valor para: \n")
    Xi: float = float(input("Xi: "))
    contador_IteracionesEsCero
    metodoNewtonRapson(Xi, 1)

def metodoNewtonRapson(Xi: float, errorAbs: float):

    error: float = 0.00001
    print("--------------------------------------")
    if error<=errorAbs:

        iteracion = contador_IteraccionesMetodo()

        print("||==================||")
        print(f"|| Iteracion No. {iteracion-1}  ||")
        print("||==================||")

        print(f"Xi = {Xi}")
        #Cambiar en caso de ser necesario
        #8 * math.e**(-0.5*Xi) * math.cos(3*Xi)
        fXi:float =Xi ** 4 +Xi-3


        print(f"f(Xi) = {fXi}")

        #Cambiar segun la derivada de la funcion original
        #-4 * math.e**(-0.5*Xi) * math.cos(3*Xi) - 24 * math.e**(-0.5*Xi) * math.sin(3*Xi)
        fXiDerivada:float = 4*Xi**3 + 1

        print(f"f'(Xi) = {fXiDerivada}")
        XiSiguiente:float = Xi - (fXi / fXiDerivada)
        print(f"Xi+1 = {XiSiguiente}")
        errorActual: float = calcularError(XiSiguiente, Xi)
        print(f"Error Actual = {errorActual}")

        metodoNewtonRapson(XiSiguiente, errorActual)
    else:
        print(f"La raiz es aproximadamene: {Xi}")

########################################################################

def metodoNewtonRapsonModificadoIniciador():
    print("Este programa busca las raices de una funcion"
          " por medio del metodo de Newton-Rapson Modificado\n"
          "Ingrese valor para: \n")
    Xi: float = float(input("Xi: "))
    contador_IteracionesEsCero
    metodoNewtonRapsonModificado(Xi, 1)

def metodoNewtonRapsonModificado(Xi: float, errorAbs: float):

    error: float = 0.0001
    print("--------------------------------------")
    if error<=errorAbs:

        iteracion = contador_IteraccionesMetodo()

        print("||==================||")
        print(f"|| Iteracion No. {iteracion-1}  ||")
        print("||==================||")

        print(f"Xi = {Xi}")
        #Cambiar en caso de ser necesario
        #math.e**math.sqrt(Xi) * math.sin(2*Xi) + math.cos(Xi**3)
        fXi:float = -0.9*Xi**2 + 1.7*Xi + 2.5

        print(f"f(Xi) = {fXi}")

        #Cambiar segun la derivada de la funcion original
        #2*math.e**(math.sqrt(Xi))*math.cos(2*Xi) + 0.5*math.e**(math.sqrt(Xi))*math.sin(2*Xi)/math.sqrt(Xi) - 3*Xi**2*math.sin(Xi**3)
        fXiDerivada:float = -1.8*Xi + 1.7

        print(f"f'(Xi) = {fXiDerivada}")

        #Cambiar segun la segunda derivada de la funcion original
        #-4*math.e**(math.sqrt(Xi))*math.sin(2*Xi) + 0.25*math.e**(math.sqrt(Xi))*math.sin(2*Xi)/Xi + 2.0*math.e**(math.sqrt(Xi))*math.cos(2*Xi)/math.sqrt(Xi) - 0.25*math.e**(math.sqrt(Xi))*math.sin(2*Xi)/Xi**(3/2) - 9*Xi**4*math.cos(Xi**3) - 6*Xi*math.sin(Xi**3)
        fXisegundaDerivada:float = -1.8

        print(f"f''(Xi) = {fXisegundaDerivada}")

        XiSiguiente:float = Xi - ((fXi*fXiDerivada) / (fXiDerivada**2 - fXi*fXisegundaDerivada))
        print(f"Xi+1 = {XiSiguiente}")
        errorActual: float = calcularError(XiSiguiente, Xi)
        print(f"Error Actual = {errorActual}")

        metodoNewtonRapsonModificado(XiSiguiente, errorActual)
    else:
        print(f"La raiz es aproximadamene: {Xi}")




def calcularError(Xr: float, XrAnterior: float):

    if Xr == 0:
        return 1

    return abs((Xr - XrAnterior) / Xr)

def contador_IteraccionesMetodo():
    global contador_iteraciones
    contador_iteraciones+=1
    return  contador_iteraciones

def contador_IteracionesEsCero():
    global contador_iteraciones
    contador_iteraciones = 0


if __name__ == "__main__":
    main()
