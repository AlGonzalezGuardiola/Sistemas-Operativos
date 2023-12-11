class Cola():
    
    def __init__(self):
        self.array = ["macia", "juanjo", "jose"]

    def push(self, valor_to_input):
        self.array.append(valor_to_input)

    def pop(self):
        for i in range(10):
            self.array.pop(1)
            

    def view_cola(self):
        print("Mi cola es: ", self.array)
        print("Mi cola es de clase: ", type(self.array))

if __name__ == '__main__':

    c1 = Cola()
    for _ in range(10):
        c1.push("Alvaro")
    c1.view_cola

    for _ in range(10):
        c1.pop()
    c1.view_cola