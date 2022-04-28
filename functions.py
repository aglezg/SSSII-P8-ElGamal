import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Comprueba si un número es primo o no
def isPrime(num):
  if num > 1:
    for n in range(2, num):
      if (num % n) == 0:
        return False
    return True
  else:
    return False

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

# Calcula "base ^ (-1) mod (module)" empleando el algoritmo de euclides
# extendido
def extendedEuclides(base, module):
  x = [0, module, base]
  z = [0, 1]
  it = 2
  while (x[it - 1] % x[it] != 0):
    x.append(x[it - 1] % x[it])
    z.append((-(x[it - 1] // x[it]) * z[it - 1] + z[it - 2]) % module)
    it += 1
  return z[len(z) - 1]

# Implementa el cifrado del Gamal
def elGamal(p, a, xa, xb, m):
  ya = quickExp(a, xa, p)
  yb = quickExp(a, xb, p)
  k = quickExp(yb, xa, p) # or quickExp(ya, xb, p)
  assert(k == quickExp(ya, xb, p))
  c = (k * m) % p
  kInverse = extendedEuclides(k, p)
  mDesc = (kInverse * k * m) % p
  return ya, yb, k, c, kInverse, mDesc