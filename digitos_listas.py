from LinkedList import LinkedList
class Sistema:
    sw = 0
    while(sw==0):
        cant_numeros= input("Digite la cantidad de numeros a ingresar: ")
        if cant_numeros.isnumeric():
            sw=1
            tam = int(cant_numeros)
        else:
            print("digite un numero valido")
    
    lista = LinkedList()
    for i in range(tam):
        sw = 0
        while(sw==0):
            numero= input("Digite el numero:")
            numero = int(numero)
            numerot = abs(numero)
            numerot= str(numerot)
            if numerot.isnumeric():
                sw=1
            else:
                print("digite un numero valido")
        x= []
        number=1
        for a in str(numero):
            number2 = a
            print(number2)
            if "-" in a:
                number=-1
            else:
                x.append(number*int(a))
                number=1
        print(x)
        ##x = [int(a) for a in str(numero)]
        lista.AddNode(x)
        print(lista)

    opc= input("Escoga 1.Sumar Lista o 2. Multiplicar Lista ")
    opc = int(opc)
    if opc==1:
        suma=0
        lista.suma(suma)
    else: 
        mult=1
        lista.mult(mult)
