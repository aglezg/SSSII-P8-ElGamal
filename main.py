# ----------------------------------------------------------------
# Práctica 8: Intercambio de claves de Diffie-Hellman y cifrado de ElGamal
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 28/04/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

import sys
from functions import *

# Main
cleanTerminal()
print("\n PRÁCTICA 8: Cifrado de ElGamal\n")

# Lectura de opciones
p = input('  p > ')
if (p.isnumeric() == False):
  sys.exit('Se debe introducir un dígito numérico...')
if (isPrime(int(p)) == False):
  sys.exit('El número "p" introducido no es un número primo')
a = input('  a > ')
if (a.isnumeric() == False):
    sys.exit('Se debe introducir un dígito numérico...')
xa = input('  xa > ')
if (xa.isnumeric() == False):
    sys.exit('Se debe introducir un dígito numérico...')
xb = input('  xb > ')
if (xb.isnumeric() == False):
    sys.exit('Se debe introducir un dígito numérico...')
m = input('  m > ')
if (m.isnumeric() == False):
    sys.exit('Se debe introducir un dígito numérico...')

# Cálculos de ElGamal
ya, yb, k, c, kInverse, mDes = elGamal(int(p), int(a), int(xa), int(xb), int(m))

# Impresión por pantalla
print('\n  >> ya = ' + str(ya) + ', yb = ' + str(yb) + ', K = ' + str(k)
  + ', C = ' + str(c) + ', K^(-1) = ' + str(kInverse) + ', M = ' + str(mDes))