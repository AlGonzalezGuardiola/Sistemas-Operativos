import random
import pdb

class Coche():
    def __init__(self, nombre, caballos):
        self.nombre=nombre
        self.caballos=caballos

    def to_string(self):
        return "{marca:", self.nombre, "caballos: ", self.caballos, "}"
    
class Carrera():
    def __init__(self, coches):
        self.coches=coches
        self.resultado=[] #### UTILIZAR

    def mostrar_parrilla_de_salida(self):
        aux = 1
        for coche in self.coches:
            print("El coche ", coche.nombre, "sale en [",aux,"] posicion")
            aux = aux+1
    
    def empieza_carrera(self):
        print("La carrera ha empezado..")

    def finaliza_carrera(self):

        posiciones_posibles = (self.coches)
        random.shuffle(posiciones_posibles)


        for posicion in posiciones_posibles:
            if posicion == 0:
                self.resultado.append(self.coches[0])
            elif posicion == 1:
                self.resultado.append(self.coches[1])
            elif posicion == 2:
                self.resultado.append(self.coches[2])
    
    def mostrtar_resultado():
        

if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("Ferrari", "200hp")
    c3 = Coche("Mustang", "200hp")
    coches=[c1, c2, c3]

    c = Carrera(coches)
    c.mostrar_parrilla_de_salida()
    c.empieza_carrera()
    c.finaliza_carrera()
    c.muestra_resultado()