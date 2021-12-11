def main():
    print("Comparador de Multiplos")
    numero1=int(input("Escriba un numero: "))
    numero2=int(input("escriba otro numero: "))
    if numero1>numero2 or numero1==numero2:
        resto= numero1 % numero2
        if resto==0:
            print(numero1, "es multiplo de", numero2)
        else:
            print(numero1, "no es multiplo de", numero2)
    else:
        resto2=numero2 % numero1
        if resto2==0:
            print(numero2, "es multiplo de", numero1)
        else:
            print(numero2, "no es multiplo de", numero1)
    salida=input("Desea volver a utilizar el programa? (Y/N): ")
    if salida=="Y":
        main()
    else:
        print("Gracias por utilizar el programa")
if __name__=="__main__":
    main()
