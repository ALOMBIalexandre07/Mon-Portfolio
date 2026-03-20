def somme1(nb):
    s = 0
    for i in range (nb + 1):
        s += i
    print ("Somme1 =", s)

nombre = int(input("Saisir un nombre "))
somme1(nombre)