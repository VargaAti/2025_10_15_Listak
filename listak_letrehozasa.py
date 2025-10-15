honapok = ['január', 'február','március', 'április', 'május', 'június']

print(type(honapok))

# lista hossza: len( )
print(len(honapok))

# index szerint kiírás
print(honapok[1])

# hátulról az első, vagyis az utolsó elem
print(honapok[-1])

# 1. 2. index kiíratása
print(honapok[1:3])

# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

# 2. indextől a végéig
print(honapok[2:])

#egy stringbe történő összefűzés ,-vel
print(', '.join(honapok))

# lista bejárása for range ciklussal
for i in range(len(honapok)):
    print(honapok[i])

print("") #sorköz

# lista bejárása for items ciklussal
for honap in honapok:
    print(honap)

