#!/usr/bin/env python
def integrand(x):
    return (4/(1+x**2))

#Aproxima la integral
def suma_riemann(limite_inferior,limite_superior,particiones):
    #Calcula el intervalo entre dos rectangulos
    interval = (limite_superior-limite_inferior)/particiones
    integral = 0.0

    for i in range(particiones):
        # Para la primera iteración x=interval/2, despues de eso va suman un intervalo para
        # que quede en la mitad del rectangulo

        x = limite_inferior + (i+1/2)*interval
        integral += integrand(x)

    return interval*integral

print("Pi aproximadamente es: {}".format (suma_riemann(0,1,10000)))
