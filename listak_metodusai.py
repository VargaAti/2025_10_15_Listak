honapok = ['január', 'február','március', 'április', 'május', 'június']

# elem hozzáadása a listához, utolsó indexet fogja használni
honapok.append('Július')
print(honapok)

honapok.pop()
print(f"{honapok} utolsó hónap törölve")
torolt_honapok = honapok.pop()
print(f"Törölt hónap: {torolt_honapok}")
print(honapok)

# Törlés adott index alapján
torolt_honapok = honapok.pop(0)
print(f"Törölt hónap: {torolt_honapok}")
print(honapok)

print(honapok.remove("február"))
print(honapok)

del honapok[2]
print(honapok)
honapok.insert(0, "február")
print(honapok)

honapok.clear()
print(honapok)