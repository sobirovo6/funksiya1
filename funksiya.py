#1
def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(1, 2, 3, 4))
print(kopaytma(5, 6))
print(kopaytma(7))

#2

def kvadrat(son1, son2, son3, *sonlar):
    kvadratlar = [son1**2, son2**2, son3**2]
    kvadratlar.extend(son**2 for son in sonlar)
    return kvadratlar

result = kvadrat(1, 2, 3, 4, 5, 6)
print(result)
