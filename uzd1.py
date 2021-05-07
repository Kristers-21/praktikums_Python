""" 
Uzrakstiet programmu, kas ielasa skaitli (kā float) -
riņķa līnijas rādiusu un izvada uz ekrāna (print) 
riņķa līnijas garumu un laukumu, atbilstoši noformējot atbildi.
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
from math import pi
r=float (input("IEvadi skaitli: "))

c=str(2*pi*r)
s=str(pi*r**2)
print("Riņķa līnijas garums ir "+c)
print("bet laukums ir "+s)
