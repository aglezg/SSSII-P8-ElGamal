# ----------------------------------------------------------------
# Práctica 7: Modos de cifrado en bloque
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 20/04/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo de las funciones
# implementadas en la práctica.
# ----------------------------------------------------------------

import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Formatea una matriz de hexadecimales, eliminando los '0x'
def formatMatrix(matrix):
  result = matrix.copy()
  for row in result:
    it = 0
    while (it < len(row)):
      if ('0x' in row[it]):
        row[it] = row[it].replace('0x', '')
        if (len(row[it]) < 2):
          row[it] = '0' + row[it]
      it += 1
  return result

# Rota elementos de un array
# d: Indica los 'd' primeros elementos a rotar
def rotateArray(array, d):
  result = array.copy()
  dCopy = d
  temp = []
  i = 0
  while (i < d):
    temp.append(array[i])
    i += 1
  i = 0
  while (dCopy < len(array)):
    result[i] = result[dCopy]
    i += 1
    dCopy += 1
  result = result[: i] + temp
  return result

# XOR - entre 2 dígitos hexadecimales
def XOR(hex1: str, hex2: str):
  return hex(int(hex1, 16) ^ int(hex2, 16))

# XOR entre 2 vectores
def XORvectors(vec1, vec2):
  assert(len(vec1) == len(vec2))
  result = []
  it = 0
  while (it < len(vec1)):
    result.append(XOR(vec1[it], vec2[it]))
    it += 1
  result = formatMatrix([result])[0]
  return result
  
# Devuelve una columna de una matriz en específico, determinada por
# su índice.
def getColumn(matrix, index):
  result = []
  it = 0
  while (it < len(matrix)):
    result.append(matrix[it][index])
    it += 1
  return result

# Imprime por pantalla la matriz
def show(matrix):
  i = 0
  j = 0
  while (i < len(matrix)):
    while (j < len(matrix[i])):
      print(matrix[i][j] + ' ', end='')
      j += 1
    j = 0
    i += 1
    print()

# Comprueba si la cadena únicamente posee dígitos hexadecimales
def isHexadecimalString(string):
  hexadecimal_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
  'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
  for char in string:
    if (char in hexadecimal_digits) == False and char != ' ':
      return False
  return True

# Convierte una matriz en una string
def matrixToString(matrix):
  result = ''
  i = 0
  j = 0
  while (i < len(matrix)):
    while (j < len(matrix[i])):
      result += matrix[j][i] + ' '
      j += 1
    i += 1
    j = 0
  return result

# Transforma una cadena de bytes en una matriz
def stringToMatrix(string: str):
  result = []
  vector = list(string.replace(' ', ''))
  aux = ''
  it = 0
  while (it < len(vector)):
    aux += vector[it]
    if (len(aux) == 2):
      if (len(result) < 4):
        result.append([aux])
      else:
        result[(it//2) % 4].append(aux)
      aux = ''
    it+= 1
  return result