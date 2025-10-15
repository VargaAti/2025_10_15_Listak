honapok = ['január', 'február','március', 'április', 'május', 'június']

#sorba rendezi a listát
sorted_honapok = sorted(honapok)
print(honapok)
print(sorted_honapok)

reversed_honapok = sorted(honapok, reverse=True)
print(honapok)
print(reversed_honapok)

print(honapok.index("március"))

print("április" in honapok)