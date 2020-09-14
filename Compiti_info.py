print("Hello world!")



n=5
numeri=[]
print("Dammi dei numeri e io ti dirò qual'è il più grade")
for i in range(n):
    numero=int(input('Inserisci un numero: '))
    numeri.append(numero)

print('I numeri casuali inseriti nella lista sono: ')

for i in range(n):
    print(numeri[i],end=' ')

massimo=numeri[0]
for i in range(n):
    if numeri[i]>massimo:
        massimo=numeri[i]

print()
print('Il valore maggiore inserito è: ', massimo)

print("ora ti genererò 1000 numeri casuali")
print("per visualizzarli clicca 2 volte su squeezed lines")
import random
randomlist = random.sample(range(0, 2000), 1000)
print(randomlist)

