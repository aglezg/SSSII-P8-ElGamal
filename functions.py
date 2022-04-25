import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

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