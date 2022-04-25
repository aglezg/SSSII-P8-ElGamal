# ----------------------------------------------------------------
# Práctica 7: Modos de cifrado en bloque
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 20/04/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from functions import *
from aesOperations import *
import sys

# Main
cleanTerminal()
print("\n PRÁCTICA 8: Modos de cifrado en bloque (CBC)\n")

# Lectura de opciones
key = input("  Clave: ")
if (len(key.replace(' ', '')) != 32 or isHexadecimalString(key) == False):
  sys.exit('La clave introducida no es correcta...')
iv = input("  IV: ")
if (len(iv.replace(' ', '')) != 32 or isHexadecimalString(iv) == False):
  sys.exit('El vector de inicialización introducido no es correcta...')
numberOfBlocks= input('  Número de bloques a introducir: ')
if (numberOfBlocks.isnumeric() == False):
  sys.exit('El número de bloques a introducir debe ser un número')
blocks = []
while (len(blocks) < int(numberOfBlocks)):
  auxBlock = input('    Bloque ' + str(len(blocks) + 1) + ': ')
  if (len(auxBlock.replace(' ', '')) != 32 or isHexadecimalString(auxBlock) == False):
    sys.exit('La clave introducida no es correcta...')
  blocks.append(stringToMatrix(auxBlock))

# Transformamos las cadenas leídas en matrices
key_matrix = stringToMatrix(key)
iv_matrix = stringToMatrix(iv)

# CBC
print()
it = 0
while (it < len(blocks)):
  iv_matrix = AESEncrypt(addRoundKey(blocks[it], iv_matrix), key_matrix)
  print('  > Bloque ' + str(it + 1) + ' de texto cifrado: ' + matrixToString(iv_matrix))
  it+= 1