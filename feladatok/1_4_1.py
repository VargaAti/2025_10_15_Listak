div_3 = []
div_5 = []
div_both = []

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        div_both.append(i)
    elif i % 5 == 0:
        div_5.append(i)
    elif i % 3 == 0:
        div_3.append(i)

print(f"3-al osztható számok: {div_3}")
print(f"5-el osztható számok: {div_5}")
print(f"3-al és 5-el osztható számok: {div_both}")
