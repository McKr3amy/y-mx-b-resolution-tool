import math
#https://www.desmos.com/calculator
print("Ta quel information sur ta règle?")
print("1. Deux points sur le plan cartesien")
print("2. Un point sur le point cartesien et m")
print("3. Un point sur le point cartesien et b")
print("4. les variables m et b")
information_sur_règle = input("?: ")
if information_sur_règle == "1":
    premier_pointx = int(input("Quel est la valeur de x du premier point?: "))
    premier_pointy = int(input("Quel est la valeur de y du premier point?: "))
    deuxieme_pointx = int(input("Quel est la valeur de x du deuxième point?: "))
    deuxieme_pointy = int(input("Quel est la valeur de y du deuxième point?: "))
    mx = deuxieme_pointx - premier_pointx
    my = deuxieme_pointy - premier_pointy
    m = my / mx
    mixmx = premier_pointx * m
    if mixmx > premier_pointy or premier_pointy > mixmx:
        b = premier_pointy - mixmx
        m = str(m)
        b = str(b)
        print("ta règle est de y = "+m+"x"+" + "+b)
    if premier_pointy == mixmx:
        b = premier_pointy - mixmx
        m = str(m)
        b = str(b)
        print("ta règle est de y = "+m+"x")
if information_sur_règle == "2":
    premier_pointx = int(input("Quel est la valeur de x du premier point?: "))
    premier_pointy = int(input("Quel est la valeur de y du premier point?: "))
    m = int(input("Quel est la valeur de m?: "))
    mixmx = premier_pointx * m
    if mixmx > premier_pointy or premier_pointy > mixmx:
        b = premier_pointy - mixmx
        m = str(m)
        b = str(b)
        print("ta règle est de y = "+m+"x"+" + "+b)
    if premier_pointy == mixmx:
        b = premier_pointy - mixmx
        m = str(m)
        b = str(b)
        print("ta règle est de y = "+m+"x")