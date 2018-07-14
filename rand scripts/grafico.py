import matplotlib.pyplot as plt

a = 1
b = 2
c = 2
yvals1 = list()
yvals2 = list()

def primeiroGrau(x):
    return a * x + b

def segundoGrau(x):
    return a * (x**2) + b * x + c 

for x in range(100):
   yvals1.append(primeiroGrau(x))
   yvals2.append(segundoGrau(x))

x = plt.plot(range(100), yvals1, 'b')   
y = plt.plot(range(100), yvals2, 'r')

