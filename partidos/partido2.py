import random
import pdb


class Equipo():
    
    def __init__(self,nombre, GK, RB, RCB, LCB, LB, RCM, LCM, CAM, LW, ST, RW):
        self.nombre = nombre
        self.GK = GK 
        self.RB = RB 
        self.RCB = RCB
        self.LCB = LCB
        self.LB = LB
        self.RCM = RCM
        self.LCM = LCM
        self.CAM = CAM
        self.LW = LW
        self.ST = ST
        self.RW = RW
        self.posiciones = [self.GK, self.RB, self.RCB, self.LCB, self.LB, self.RCM, self.LCM, self.CAM, self.LW, self.ST, self.RW]    


    def __str__(self):
        return "["+self.nombre+"]"

    def ocasion_gol(self):
        a = random.randint(0,1)
           
        if a == 0:
            return 0 
        else:
            return 1    

class Partido():
    def __init__(self,E1,E2, n_ocasiones):
        self.E1 = E1 
        self.E2 = E2 
        self.n_ocasiones = n_ocasiones
        self.golesE1 = 0
        self.golesE2 = 0
        self.ganador = 0
        self.goleador = 0
    
    #def crono():
    def ocasion(self, equipo):
        goleadores_posibles = [pos for pos in self.E1.posiciones if pos != self.E1.GK]
        goleador = random.choice(goleadores_posibles)
        if equipo == 1:
            gol = self.E1.ocasion_gol()
            self.golesE1 += gol
        else:
            gol = self.E2.ocasion_gol()
            self.golesE2 += gol
        if gol == 1:
            print(f"Hay una ocasión de gol, el resultado es: {self.golesE1}-{self.golesE2}, Gol de {goleador} ({self.E1.nombre})")
        else:
            print(f"Hay una ocasión de gol: {self.golesE1}-{self.golesE2}, Falló el cabrón de {goleador}.")


    
    
    def JugarPartido(self):        
       for i in range(self.n_ocasiones):
            a = random.randint(0, 1)
            if a == 0:
                self.ocasion(0) # le mandamos el equipo por parametro.
            else:
               self.ocasion(1)
           
    def show_winner(self):
        if self.golesE1 > self.golesE2:
            print("El ganador del partido es", self.E1)
        elif self.golesE1 < self.golesE2:                
            print("El ganador del partido es", self.E2)
        else:
           print(self.E1, "y", self.E2, "han empatado.") 


    #def Tarjetas(self, Amarilla, Roja):
     #   self.Amarilla = Amarilla
      #  self.Roja = Roja

if __name__ == '__main__':

    Rcd_Mallorca = Equipo("Rcd Mallorca", "Rajkovic", "Pablo Maffeo", "Raillo", "Valjent", "Jaume Costa", "Darder", "Morlanes", "Dani Rodríguez", "Not Kang In Lee", "Muriqi", "Larin")
    Real_Madrid = Equipo("Real Madrid", "Courtois", "Carvajal", "Militao", "Alaba", "Mendy", "Camavinga", "Tchouameni", "Bellingham", "ViniJr", "Joselu", "Rodrygo")
    
    #JugarPartido
    #pdb.set_trace()
    p1 = Partido(Rcd_Mallorca, Real_Madrid, 20)
    p1.JugarPartido()
    p1.show_winner()

