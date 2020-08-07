# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:21:39 2020

@author: HenrryPuente
"""
cinicial=int(input("contador inicial : "))
cfinal=int(input("contador final : "))
if cfinal<cinicial:
    print("error: el contador final es menor que el inicial")
    cfinal=int(input("contador final : "))
impresora=input("impresora(1= B/N, 2= Color)=")
if impresora == "1" or "b/n"  :
    r=(cfinal-cinicial)
    resultado=r*0.06
    print("impreciones:",r)
    print("Costo: ",resultado)
if impresora=="2" or "color":
    r=(cfinal-cinicial)
    resultado=r*0.12
    print("impreciones:",r)
    print("Costo: ",resultado)