import math
#https://www.desmos.com/calculator
print("Ta quel information sur ta règle?")
print("1. Deux points sur le plan cartesien")
print("2. Un point sur le point cartesien et m")
print("3. Un point sur le point cartesien et b")
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
if information_sur_règle == "3":
    deuxieme_pointx = int(input("Quel est la valeur de x du deuxieme point?: "))
    deuxieme_pointy = int(input("Quel est la valeur de y du deuxieme point?: "))
    b = int(input("Quel est la valeur de b?: "))
    premier_pointy = b
    premier_pointx = 0
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
print("make sur to go on"+" https://www.desmos.com/calculator"+" to check out the fonction!")