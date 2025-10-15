"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
"""
import random as r
numbers = []
for i in range(10):
        numbers.append(r.randint(1,3))
        i += 1
print(f"Lista: {numbers}")
num_to_del = int(input("Adj meg egy számot amit törölni szeretnél a listából: "))
# filtered = list(filter(lambda x: x != num_to_del, numbers))
# print(f"Lista: {filtered}")
while num_to_del in numbers:
        print(numbers.remove(num_to_del))
print(numbers)