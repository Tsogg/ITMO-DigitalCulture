a = 0.25 #1
b = 0.23 #2
c = 0.13 #3
d = 0.09 #4
e = 0.16 #5
f = 0.13 #6
g = 0.24 #7
h = 0.01 #8
k = 0.15 #9
o = (1 - a)*(1 - b)*(1 - c)*(1 - d)*(1 - k)
l = o / (1 - c) - o
print(round(o,2))
print(round(l,2))
print(round((1 - h) * (1 - k),2))
