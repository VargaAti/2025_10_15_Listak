div_3 = []
div_5 = []
div_both = []

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        div_both.append(i)
    if i % 5 == 0:
        div_5.append(i)
    if i % 3 == 0:
        div_3.append(i)

print(f"3-al osztható számok: {div_3}")
print(f"5-el osztható számok: {div_5}")
print(f"3-al és 5-el osztható számok: {div_both}")

# 3-al osztható számok: [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]
# 5-el osztható számok: [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]
# 3-al és 5-el osztható számok: [15, 30, 45, 60, 75, 90]