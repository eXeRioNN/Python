def main():
    print("Comparador de años")
    año1=int(float(input("en que año estamos?: ")))
    año2=int(float(input("escriba un año cualquiera: ")))
    if año1==año2:
        print("Es el mismo año!")
    elif año1<año2:
        tot=int(año2 - año1)
        print("Faltan", str(tot), "años para llegar a", str(año2))
    else:
        tot2=int(año1 - año2)
        print("Pasaron", str(tot2), "años desde", str(año2))
    salida=input("desea utilizar el programa nuevamente? (Y/N): ")
    if salida=="Y":
        main()
    else:
        print("Gracias por utilizar el programa")
if __name__=="__main__":
    main()
