from mod import Mod
from os import urandom

def int_from_bytes(s):
    acc = 0
    for b in s:
        acc = acc * 256
        acc += b
    return acc

secret = int_from_bytes("terrible secret".encode("utf-8"))
P = 2**521 - 1
secret < P

secret = mod.Mod(secret, P)

polynomial = [secret]
for i in range(2):
    polynomial.append(Mod(int_from_bytes(urandom(16)), P))
len(polynomial)

def evaluate(coefficients, x):
    acc = 0
    power = 1
    for c in coefficients:
        acc += c * power
        power *= x
    return acc

shards = {}
for i in range(5):
    x = Mod(int_from_bytes(urandom(16)), P)
    y = evaluate(polynomial, x)
    shards[i] = (x, y)

del shards[2]
del shards[3]

retrieved = list(shards.values())
