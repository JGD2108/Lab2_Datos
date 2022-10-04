from Node import Node
class LinkedList: 
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data):
        P = Node(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P 

    def suma(self, suma):
        P = self.PTR
        suma=0
        num=""
        while(P != None):
            x=0
            for i in P.data:
                num = num+ str(P.data[x])
                x=x+1
            suma = (int(suma) + int(num))
            P = P.next
            num=""
        new_sum=suma
        print(new_sum)
        suma= str(new_sum)
        numero = [(a) for a in str(new_sum)]
        print(numero)
        resultado = LinkedList()
        for w in range(len(numero)):
            resultado.AddNode(numero[w])
            print(resultado)

    def mult(self, mult):
        P = self.PTR
        Pr=P
        mult=1
        num=""
        while(Pr!=None):
            x=0
            for i in P.data:
                print(i)
                num= num+ str(P.data[x])
                x=x+1
            print(num)
            mult = (int(mult) * int(num))
            P = P.next
            Pr=P
            num=""
        new_mult=mult
        number=1
        numero= []
        for a in str(new_mult):
            number2 = a
            print(number2)
            if "-" in a:
                number=-1
            else:
                numero.append(number*int(a))
                number=1
        ##numero = [int(a) for a in str(new_mult)]
        resultado = LinkedList()
        for w in range(len(numero)):
            resultado.AddNode(numero[w])
        print(resultado)

    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.data) + "(->)"
            P = P.next
        respuesta = respuesta+ "None"
        return respuesta   

