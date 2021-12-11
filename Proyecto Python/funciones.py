def usuario():
    import json
    with open("Usuario.json") as file:
        usuario=json.load(file)
        if usuario=={}:
            reg_user={}
            valid_alpha_user= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_."
            while True:
                user=input("Ingrese su nuevo nombre de usuario, debe contar con al menos 6 digitos: ")
                if (len(user)>5):
                    nuevo_usuario=set(user)
                    a=set(valid_alpha_user)
                    if len(nuevo_usuario-a)>0:
                        print("Usuario Invalido")
                        continue
                    else:
                        print("Usuario Valido")
                        break
                else:
                    print("Usuario invalido, debe tener al menos 6 caracteres")
                    continue

            while True:
                password=input("Ingrese su contraseña: ")
                if (len(password)>5):
                    new_password=set(password)
                    a=set(valid_alpha_user)
                    if len(new_password-a)>0:
                        print("Contraseña Invalida")
                        continue
                    else:
                        print("Contraseña Valida")
                        break
                else:
                    print("Contraseña Invalida, debe tener al menos 6 caracteres")
                    continue 

            while True:
                codigo=input("Ingrese su codigo para transacciones: ")
                if (len(codigo)>7):
                    nuevo_codigo=set(codigo)
                    a=set(valid_alpha_user)
                    if len(nuevo_codigo-a)>0:
                        print("Contraseña Invalida")
                        continue
                    else:
                        print("Codigo Valido")
                        break
                else:
                    print("Codigo Invalido, debe tener al menos 8 caracteres")
                    continue 
            
            reg_user[(user)]=[(password)]
            reg_user["codigo"]=[(codigo)]
            import json
            with open ("Usuario.json", "w") as file:
                json.dump(reg_user, file, indent=1)    
            
        else:
            while True:
                user=input("Ingrese su nombre de Usuario: ")
                verificacion=usuario.get(user)
                if verificacion:
                    print("usuario Confirmado")
                    break
                else:
                    print("Usuario Invalido")
                    continue
            while True:
                password=input("Ingrese su contraseña: ")
                verificacion=usuario[user]
                if password in verificacion:
                    print("Contraseña Valida")
                    break
                else:
                    print("Contraseña Invalida")
       

def verificacion_criptos():
    import json
    with open("criptomonedas.json", "r") as file:
        criptos = json.load(file)
    if criptos=={}:
        import requests

        def esmoneda(cripto):
            return cripto in monedas

        monedas_list=[]
        data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
        for cripto in data["data"]:
            monedas_list.append(cripto["symbol"])
        monedas=tuple(monedas_list)
    
        while True:
            cripto1=input(f"ingrese el nombre de su primer criptomoneda: ")
            if esmoneda(cripto1):
                cant1=""
                while not cant1.replace('.','',1).isdigit():
                    cant1=input(f"Indique la cantidad de {cripto1}: ")
                else:
                    break
            else:
                print("Moneda Invalida")

        while True:    
            cripto2=input(f"ingrese el nombre de su segunda criptomoneda: ")
            if esmoneda(cripto2):
                cant2=""
                while not cant2.replace('.','',1).isdigit():
                    cant2=input(f"Indique la cantidad de {cripto2}: ")
                else:
                    break
            else:
                print("Moneda Invalida")

        while True:    
            cripto3=input(f"ingrese el nombre de su tercer criptomoneda: ")
            if esmoneda(cripto3):
                cant3=""
                while not cant3.replace('.','',1).isdigit():
                    cant3=input(f"Indique la cantidad de {cripto3}: ")
                else:
                    break
            else:
                print("Moneda Invalida")
    
       
        dict_criptos={(cripto1):(cant1), (cripto2):(cant2), (cripto3):(cant3)}
        import json
        with open ("criptomonedas.json", "w") as file:
                    json.dump(dict_criptos, file, indent=1)      


def __main__():
    print("")
    print("")
    print("1- Transferencias")
    print("2- Consultas")
    print("3- Salir")
    
    while True:
        opcion=input("Seleccione una opcion para continuar: ")
        if (opcion)=="1":
            print("1- Transferir monto")
            print("2- Recibir monto")
            while True:
                opcion=input("Seleccione una opcion para continuar: ")
                if opcion=="1":
                    from funciones import transferencia
                    transferencia()
                elif (opcion)=="2":
                    from funciones import recibir
                    recibir()
                else:
                    continue
        elif opcion=="2":
            print("1- Consulta de saldo")
            print("2- Balance General")
            print("3- Consulta de movimientos")
            while True:
                opcion=input("Seleccione una opcion para continuar: ")
                if opcion=="1":
                    from funciones import consulta_saldo
                    consulta_saldo()
                elif opcion=="2":
                    from funciones import balance_general
                    balance_general()
                elif opcion=="3":
                    from funciones import historial_movimientos
                    historial_movimientos()
                else:
                    continue
        elif opcion=="3":
            print("Gracias por utilizar el programa")
            exit()
        else:
            continue


def transferencia():
    import json
    with open("criptomonedas.json") as file:
        criptos = json.load(file)

    
    while True:
        cripto=input("Indique la moneda a transferir: ")
        verificacion=criptos.get(cripto)
        if verificacion:
            moneda=criptos[cripto]
            cant_moneda=float(moneda)
            break
        else:
            print("Moneda Invalida")

    
    while True:
        cant=input("Indique la cantidad a transferir: ")
        while not cant.replace('.','',1).isdigit():
            cant=input("Indique la cantidad a transferir: ")
        else:
            if float(cant)>cant_moneda:
                print("La cantidad que desea transferir supera su monto")
            else:
                break
    
    
    import json
    with open("Usuario.json") as file:
        usuario=json.load(file)
    cod_trans=input("Indique el codigo de la transferencia: ")
    while True:
        verif_cod=input("Indique su codigo: ")
        if verif_cod in usuario["codigo"]:
            tot=cant_moneda - float(cant)
            print(f"usted transfirio {cant} de {cripto} satisfactoriamente")
            break
        else:
            print("Codigo Incorrecto")
    
    
    import requests
    data=requests.get("https://api.binance.com/api/v3/ticker/price").json()
    for datos in data:
        if datos["symbol"]==(cripto)+"USDT":
            cot=datos["price"]
    cotizacion=tot*float(cot)
    print(f"su saldo de {cripto} es de {tot} con un valor de {cotizacion} USD")

    
    from datetime import datetime
    d=datetime.now()
    fecha=d.strftime("%A %d/%m/%y %H:%H:%S")
    transferencia=f"-{fecha}. codigo de transaccion:{cod_trans}. Debito de {cant} {cripto} a un valor de {cotizacion} USD"
    archivo=open("Historial de Transacciones.txt", "a")
    archivo.write((transferencia)+"\n")
    archivo.close()
    
    
    criptos[(cripto)]=tot
    with open ("criptomonedas.json", "w") as file:
        json.dump(criptos, file, indent=1)    


    while True:
        salida=input("¿Desea realizar otra operacion?(Y/N): ")
        if salida=="Y":
            from funciones import __main__
            __main__()
        elif salida=="N":
            print("Gracias por Utilizar el Programa")
            exit()
        else:
            print("Opcion Invalida")


def recibir():
    import json
    with open("criptomonedas.json") as file:
        criptos = json.load(file)

    
    while True:
        cripto=input("Indique la moneda a recibir: ")
        verificacion=criptos.get(cripto)
        if verificacion:
            moneda=criptos[cripto]
            cant_moneda=float(moneda)
            break
        else:
            print("Moneda Invalida")

    
    while True:
        cant=input("Indique la cantidad a recibir: ")
        while not cant.replace('.','',1).isdigit():
            cant=input("Indique la cantidad a recibir: ")
        else:
            break
    
    
    import json
    with open("Usuario.json") as file:
        usuario=json.load(file)
    cod_trans=input("Indique el codigo de la transferencia: ")
    while True:
        verif_cod=input("Indique su codigo: ")
        if verif_cod in usuario["codigo"]:
            tot=cant_moneda + float(cant)
            print(f"usted recibio {cant} de {cripto} satisfactoriamente")
            break
        else:
            print("Codigo Incorrecto")
    
    
    import requests
    data=requests.get("https://api.binance.com/api/v3/ticker/price").json()
    for datos in data:
        if datos["symbol"]==(cripto)+"USDT":
            cot=datos["price"]
    cotizacion=tot*float(cot)
    print(f"su saldo de {cripto} es de {tot} con un valor de {cotizacion} USD")


    from datetime import datetime
    d=datetime.now()
    fecha=d.strftime("%A %d/%m/%y %H:%H:%S")
    transferencia=f"-{fecha}. codigo de transaccion:{cod_trans}. Ingreso de {cant} {cripto} a un valor de {cotizacion} USD"
    archivo=open("Historial de Transacciones.txt", "a")
    archivo.write((transferencia)+"\n")
    archivo.close()
    
    
    criptos[(cripto)]=tot
    with open ("criptomonedas.json", "w") as file:
        json.dump(criptos, file, indent=1)   
    

    while True:
        salida=input("¿Desea realizar otra operacion?(Y/N): ")
        if salida=="Y":
            from funciones import __main__
            __main__()
        elif salida=="N":
            print("Gracias por Utilizar el Programa")
            exit()
        else:
            print("Opcion Invalida")


def consulta_saldo():
    import json
    with open("criptomonedas.json") as file:
        criptos = json.load(file)
    

    while True:
        cripto=input("Indique la moneda a consultar: ")
        verificacion=criptos.get(cripto)
        if verificacion:
            moneda=criptos[cripto]
            break
        else:
            print("Moneda Invalida")


    import requests
    data=requests.get("https://api.binance.com/api/v3/ticker/price").json()
    for datos in data:
        if datos["symbol"]==(cripto)+"USDT":
            cot=datos["price"]
    print(f"Su saldo es de {moneda} {cripto} con un valor de {cot} USD ")


    while True:
        salida=input("¿Desea realizar otra operacion?(Y/N): ")
        if salida=="Y":
            from funciones import __main__
            __main__()
        elif salida=="N":
            print("Gracias por Utilizar el Programa")
            exit()
        else:
            print("Opcion Invalida")


def balance_general():
    import json
    with open("criptomonedas.json") as file:
        criptos = json.load(file)
    nombres=list(criptos.keys())
    valores=list(criptos.values())
    
    import requests
    data=requests.get("https://api.binance.com/api/v3/ticker/price").json()
    for datos in data:
        if datos["symbol"]==(nombres[0])+"USDT":
            cot1=float(datos["price"])
    for datos in data:
        if datos["symbol"]==(nombres[1])+"USDT":
            cot2=float(datos["price"])
    for datos in data:
        if datos["symbol"]==(nombres[2])+"USDT":
            cot3=float(datos["price"])
    valor1=float(valores[0])
    valor2=float(valores[1])
    valor3=float(valores[2])
    tot_usd=valor1*cot1+valor2*cot2+valor3*cot3
    print(f"Usted posee {valor1} {nombres[0]}; {valor2} {nombres[1]}; {valor3} {nombres[2]}, con un valor total de {tot_usd} USD")



    while True:
        salida=input("¿Desea realizar otra operacion?(Y/N): ")
        if salida=="Y":
            from funciones import __main__
            __main__()
        elif salida=="N":
            print("Gracias por Utilizar el Programa")
            exit()
        else:
            print("Opcion Invalida")


def historial_movimientos():
    archivo=open("Historial de Transacciones.txt", "r")
    texto=archivo.read()
    archivo.close()
    lineas=texto.splitlines()
    for linea in lineas:
        print(linea)


    while True:
        salida=input("¿Desea realizar otra operacion?(Y/N): ")
        if salida=="Y":
            from funciones import __main__
            __main__()
        elif salida=="N":
            print("Gracias por Utilizar el Programa")
            exit()
        else:
            print("Opcion Invalida")


