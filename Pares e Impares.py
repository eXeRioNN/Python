print("Pares e Impares")
inf= int(input("ingrese un numero entero: "))
sup= int(input(f"Ingrese un numero mayor a {inf}: "))
while sup<inf:
    print(f"Le he pedido un numero mayor a {inf}")
    sup=int(input(f"ingrese un numero mayor a {inf}: "))
for i in range(inf, sup + 1):
        if i%2==0:
            print(f"el numero {i} es par")
        else: print(f"el numero {i} es impar")

