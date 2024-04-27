import random
g1 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
g2 = int(input('напиши длинну пароля'))

g3 = ""

for i in range(g2):
    g3 += random.choice(g1)

print(g3)
