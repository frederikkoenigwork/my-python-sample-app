
stuff = "Lorem Ipsum dolor si amat saflksajföldsakjfsadf"

char = "a"

liste = [1,2,3,4,5,6]

listenliste = [[1, 2, 3], [1,2,3]]

print(stuff)


x = 42

if x < 42:
    print("Oh weh")
elif x==42:
    print("The answer to all questions.")
else:
    print("Bigger than 42.")

for x in liste:
    print(x)


for y in range(0,42):
    print(y)







def meineFunktion(liste):
    i = 0
    x = liste[i]
    while x < 5:
        print(x)
        i += 1
        x = liste[i]
        if i >= len(liste):
            break
        x = liste[i]


def generiereListe():
    liste = [1, 2, 3, 4, 42, 1337]
    return liste


listeL = generiereListe()
meineFunktion(listeL)