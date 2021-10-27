import random


a = input("Введите число a и через пробел число b (a<b): ")


b = a.split(" ")
d = float(b[0])
e = float(b[1])
k = "%.3f" % e
k = float(k) - 0.001


f = "%.3f" % random.uniform(d,k)
q = "%.3f" % random.uniform(d,k)
s = "%.3f" % random.uniform(d,k)
g = "%.3f" % random.uniform(d,k)
h = "%.3f" % random.uniform(d,k)


print(f,q,s,g,h)

#Для покупки ПО свяжитесь с автором по почте.