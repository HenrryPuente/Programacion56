# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
@HenryPuente
t=int(input("Ingrese las horas laboradas: "))

h=int(input("Ingrese la tarifa por horas: "))
if t<=40:
    s=t*h
    
else:
    h1=t+0.50*t
    t1=h-40
    s=h1-t1+40*t-9
    print("el valor a cancelar es: ",s)
    