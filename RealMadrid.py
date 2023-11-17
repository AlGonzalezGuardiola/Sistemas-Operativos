class Equipo():
    def __init__(self, GK, RB, RCB, LCB, LB, RCM, LCM, CAM, LW, ST, RW):
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

class Partido():
    def __init__(self,E1,E2):
        self.E1 = E1
        self.E2 = E2

    def JugarPartido():
        
if __name__ == '__main__':

    Rcd_Mallorca = Equipo("Rajkovic", "Pablo Maffeo", "Raillo", "Valjent", "Jaume Costa", "Darder", "Morlanes", "Dani Rodríguez", "Not Kang In Lee", "Muriqi", "Larin")
    Real_Madrid = Equipo("Courtois", "Carvajal", "Militao", "Alaba", "Mendy", "Camavinga", "Tchouameni", "Bellingham", "ViniJr", "Joselu", "Rodrygo")
    
    Match = Partido(Real_Madrid,Rcd_Mallorca)
    
