def main():
    print("Divisor de Numeros")
    dividendo=(input("Escriba el dividendo: "))
    divisor=float(input("Escriba el divisor: "))
    while divisor==0:
        print("no se puede dividir por cero")
        divisor=float(input("Escriba el divisor: "))
    cociente=int(float(dividendo) // divisor)
    resto= float(dividendo) % divisor
    if resto==0:
        print("La division es exacta. Cociente:" + str(cociente))
    else:
        print("La division no es exacta. Cociente:" +str(cociente)+ "Resto:" + str(resto))
    salida=input("desea utilizarlo nuevamente? (Y/N): ")
    if salida=="Y":
        main()
    else:
        print("gracias por utilizar el programa")
if __name__=="__main__":
    main()











