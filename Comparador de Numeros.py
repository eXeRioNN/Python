def main():
    print("Comparador de Numeros")
    numero1=float(input("escriba un numero: "))
    numero2=float(input("escriba otro numero: "))
    if numero1<numero2:
        print("Menor: "+str(numero1), ";", "Mayor: ", str(numero2))
    elif numero1==numero2:
        print("ambos numeros son iguales")
    else:
        print("Menor:", str(numero2), ";", "Mayor:", str(numero1))
    salida=input("desea seguir utilizando el programa? (Y/N): ")
    if salida=="Y":
        main()
    else:
        print("gracias por utilizar el programa")
if __name__=="__main__":
    main()
           