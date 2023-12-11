class Pila():
    def __init__(self):
        self.array=[]

    def push(self, valor_to_input):
        self.array.append(valor_to_input)

    def pop(self):
        self.array.pop()

    def view_pila(self):
        print("Mi pila es: ", self.array)
        print("Mi pila es de clase: ", type(self.array))

if __name__ == '__main__':
   
    pila = Pila()
    for _ in range(10):
        pila.push("Messi")
    pila.view_pila()
   
    for _ in range(10):
        pila.pop()
    pila.view_pila()
   


    """
    pila = []
    #Empilo
    for i in range(10):
        pila.append(i)
        print("E mi pila: ",pila)

    print()

    #Desempilo
    for i in range(10):
        pila.pop()
        print("D mi pila:",pila)
    """
