"""
1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""
colors = ["piros", "kék", "zöld", "sárga", "lila"]
while True:
    user = input("Adj meg egy színt: ")
    if user in colors:
        print("A szín már szerepel a listában.")
    elif user == "":
        break
    else:
        print("A szín még nem szerepel a listában.")
    print(", ".join(colors))