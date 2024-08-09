# -*- coding: utf-8 -*-
"""Actividad01_Punto2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QdhKFsFLRG-_lAcfsrn3G3y-gFnLlny5

Actividad 01- Punto 2

Crea una función llamada doble_factorial que reciba un parámetro llamado n. La función debe devolver el doble factorial de n, que se define como el producto de todos los números naturales desde n hasta 1 que tienen el mismo paridad que n. Por ejemplo, si n es 5, la función debe devolver 15, que es el resultado de 5 x 3 x 1. Llama a la función doble_factorial con diferentes valores para el parámetro n, como 6, 7 o 8.
"""

m = 1

def doble_factorial(n):
  global m
  while n > 1:
      m = m * n
      n = n - 2
  return m



entero = int(input("Escriba un numero entero para obtener el  doble factorial "))
k = doble_factorial(entero)
print(f"El doble factorial es {k} ")