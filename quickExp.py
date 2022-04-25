# Algoritmo de exponenciación rápida
def quickExp(base, exp, module):
  x = 1
  y = base % module
  expCopy = exp
  while (expCopy > 0 and y > 1):
    if (expCopy % 2 != 0):
      x = (x * y) % module
      expCopy = expCopy - 1
    else:
      y = (y * y) % module
      expCopy = expCopy / 2
  return x