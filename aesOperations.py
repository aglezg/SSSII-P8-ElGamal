# ----------------------------------------------------------------
# Práctica 7: Modos de cifrado en bloque
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 20/04/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo de las funciones del AES
# ----------------------------------------------------------------

from functions import formatMatrix, rotateArray, XORvectors, getColumn

# S-Caja utilizada para la operación 'SubBytes'
SBOX = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
         ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
         ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
         ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
         ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
         ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
         ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
         ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
         ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
         ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
         ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
         ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
         ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
         ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
         ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
         ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

# Vector RCON
RCON = [['01', '00', '00', '00'],
        ['02', '00', '00', '00'],
        ['04', '00', '00', '00'],
        ['08', '00', '00', '00'],
        ['10', '00', '00', '00'],
        ['20', '00', '00', '00'],
        ['40', '00', '00', '00'],
        ['80', '00', '00', '00'],
        ['1b', '00', '00', '00'],
        ['36', '00', '00', '00']]

# SubBytes
def subBytes(matrix):
  result = []
  i = 0
  j = 0
  while (i < len(matrix)):
    resultRow = []
    while (j < len(matrix[i])):
      resultRow.append(SBOX[int(matrix[i][j][0], 16)][int(matrix[i][j][1], 16)])
      j += 1
    j = 0
    i += 1
    result.append(resultRow.copy())
  return result

# ShiftRow
def shiftRow(matrix):
  result = matrix.copy()
  i = 0
  while (i < len(matrix)):
    result[i] = rotateArray(result[i], i)
    i += 1
  return result

# MixColumn
def mixColumns(matrix):
  result = matrix.copy()
  for i in range(4):
    a = []
    b = []
    for c in range(4):
      a.append(int(result[c][i], 16))
      h = int(result[c][i], 16) & 0x80
      b.append((int(result[c][i], 16) << 1) % 256)
      if (h == 0x80):
        b[c] = b[c] ^ 0x1b 
    result[0][i] = hex(b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1]) 
    result[1][i] = hex(b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2]) 
    result[2][i] = hex(b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3]) 
    result[3][i] = hex(b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0]) 
  result = formatMatrix(result)
  return result

# AddRoundKey
def addRoundKey(matrix, key):
  assert (len(matrix) == len(key))
  result = []
  i = 0
  j = 0
  while (i < len(matrix)):
    assert (len(matrix[i]) == len(key[i]))
    result.append(XORvectors(matrix[i], key[i]))
    i += 1
  result = formatMatrix(result)
  return result

# Expansión de claves
def keyExpansion(key, RCON_index):
  result = []
  # RotWord
  colResult = getColumn(key, len(key) - 1)
  colResult = rotateArray(colResult, 1)
  # SubBytes
  colResult = subBytes([colResult])[0]
  # XOR i - 3
  colResult = XORvectors(colResult, getColumn(key, len(key) - 4))
  # XOR RCON
  colResult = XORvectors(colResult, RCON[RCON_index])
  # Guardamos el resultado
  for element in colResult:
    result.append([element])
  # XOR restantes
  for i in range(len(colResult) - 1):
    colResult =  XORvectors(colResult, getColumn(key, i + 1))
    it = 0
    for element in colResult:
      result[it].append(element)
      it += 1
  return result

def AESEncrypt(block, key):
  result = addRoundKey(block, key)
  keyCopy = key.copy()
  for i in range(9):
    keyCopy = keyExpansion(keyCopy, i)    # Expansión i-ésima de claves
    result = subBytes(result)             # SubBytes
    result = shiftRow(result)             # ShiftRows
    result = mixColumns(result)           # MixColumns
    result = addRoundKey(result, keyCopy) # AddRoundKey
  keyCopy = keyExpansion(keyCopy, 9)      # Décima expansión de claves
  result = subBytes(result)               # SubBytes
  result = shiftRow(result)               # ShiftRows
  result = addRoundKey(result, keyCopy)   # AddRoundKey
  return result