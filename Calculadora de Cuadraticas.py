def main():
    print("Calculadora de cuadraticas")
    a=float(input("ingrese valor de a: "))
    b=float(input("ingrese valor de b: "))
    c=float(input("ingrese valor de c: "))
    if a==0 and b==0:
        print("la ecucacion no tiene solucion")
    elif a==0 and b!=0:
        x=(-c)/b
        print("La ecuacion tiene 1 solucion: x=", str(x))
    elif b**2 - (4*a*c)<0:
        print("La ecuacion no tiene solucion en reales")
    else:
        x1=((-b) + (b**2 - (4*a*c))**0.5)/(2*a)
        x2=((-b) - (b**2 - (4*a*c))**0.5)/(2*a)
        print("La ecuacion tiene 2 soluciones, x1=", str(x1), "y x2=", str(x2))
    salida=input("desea utilizar el programa nuevamente? (Y/N): ")
    if salida=="Y":
        main()
    else:
        print("Gracias por utilizar el programa")
if __name__=="__main__":
    main()