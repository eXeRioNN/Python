print("Contador de Pares e Impares")
cant=int(input("Cuantos valores va a introducir?: "))
pares=0
for i in range(1, cant+1):
    numero=int(input(f"ingrese el numero {i}: "))
    if numero%2==0:
        pares +=1
print(f"ha escrito {pares} numeros pares y {cant-pares} numeros impares")


    

