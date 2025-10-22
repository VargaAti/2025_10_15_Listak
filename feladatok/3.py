"""
3. Feladat
Az adott lista (→ 'Próbáld ki!') elemei közül a program kiírja a 3-mal osztható páros számokat!
"""
numbers = []
for i in range(1,41):
    if i % 3 == 0 and i % 2 == 0:
        numbers.append(i)
print(numbers)