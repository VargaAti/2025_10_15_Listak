"""
1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""
colors = ["piros", "kék", "kék", "zöld", "sárga", "sárga", "lila"]
while True:
    user = input("Adj meg egy színt: ")
    if user in colors:
        print(colors.count(user))
    elif user == "":
        break
    else:
        print("A szín még nem szerepel a listában.")
    print(", ".join(colors))