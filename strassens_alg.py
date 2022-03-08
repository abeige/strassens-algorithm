import numpy as np
from math import ceil

# STRASSEN'S ALGORITHM
def multiply(m1, m2, n):
    if n == 1:
        return m1 * m2

    n2 = int(n/2)
    a = m1[:n2, :n2]
    b = m1[:n2, n2:]
    c = m1[n2:, :n2]
    d = m1[n2:, n2:]

    e = m2[:n2, :n2]
    f = m2[:n2, n2:]
    g = m2[n2:, :n2]
    h = m2[n2:, n2:]

    m1 = multiply(a, f - h, n/2)
    m2 = multiply(a + b, h, n/2)
    m3 = multiply(c + d, e, n/2)
    m4 = multiply(d, g - e, n/2)
    m5 = multiply(a + d, e + h, n/2)
    m6 = multiply(b - d, g + h, n/2)
    m7 = multiply(a - c, e + f, n/2)

    top = np.concatenate((m5 + m4 - m2 + m6, m1 + m2), axis=1)
    bottom = np.concatenate((m3 + m4, m1 + m5 - m3 - m7), axis=1)
    return np.concatenate((top, bottom))


print("Welcome to efficient recursive matrix multiplication")

# INPUT SIZE OF MATRICES
prompt = True

while (prompt):
    n = input("enter side length of square matrix ")
    try:
        n = int(n)
    except:
        print("please enter a number")
        continue
    if n < 2:
        print("please enter a positive number greater than 1")
    else:
        prompt = False

# INPUT THE MATRICES
padding = 2 ** ceil(np.log2(n))
m1 = np.zeros((padding, padding))
m2 = np.zeros((padding, padding))

for r in range(n):
    print("row " + str(r + 1) + ": ")
    for c in range(n):
        m1[r][c] = input("  column " + str(c + 1) + ": ")

print(m1)

for r in range(n):
    print("row " + str(r + 1) + ": ")
    for c in range(n):
        m2[r][c] = input("  column " + str(c + 1) + ": ")

print(m2)

# RECURSIVE MULTIPLICATION
print(multiply(m1, m2, padding))
