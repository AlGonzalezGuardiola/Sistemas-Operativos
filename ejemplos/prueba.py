def saludo():
    return "Saludo"

def suma(n1,n2):
    return n1 +n2

def resta(n1,n2):
    return n1 - n2

def multiplicacion(n1,n2):
    return n1 * n2

def print_array(array):
    print (array)
    for n in array:
        print ("Hola me llamo", n)

if __name__=="__main__":

    nombre = "Juan"

    a = suma(1,2)
    b = resta(5,3)
    c = multiplicacion(2,5)
    print (a,b,c)




array = ["borja","alvaro", "caue"]
print_array(array)