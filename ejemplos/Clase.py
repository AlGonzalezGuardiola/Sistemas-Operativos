import time
class Coche():
    def __init__(self, modelo, motor, neumaticos, puertas, velocidad, velocidad_punta):
        self.modelo = modelo
        self.motor = motor
        self.neumaticos = neumaticos
        self.puertas = puertas
        self.velocidad = velocidad
        self.velocidad_punta = velocidad_punta
   
   
    def velocidad(self):
        self.velocidad = 0

    def acelerar(self):
        while self.velocidad<self.velocidad_punta:
            self.velocidad +=5
            time.sleep(0.05) 
            print("Estoy acelerando", self.velocidad, "km por hora")
        self.desacelerar()

    def desacelerar(self):
        while self.velocidad > 0:
            self.velocidad -=5
            time.sleep(0.05) 
            print("estoy reduciendo a", self.velocidad, "km por hora")
        self.arrancar()
    
    def arrancar(self):
        #return self.velocidad
        print("voy a arrancar el coche")
        self.acelerar()

if __name__ == '__main__':
    c1 = Coche("Volkswagen Golf GTI", "V6 Biturbo", "Medios", 3, 0, 120)
    c1.arrancar()
