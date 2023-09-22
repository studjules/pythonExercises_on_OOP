#Fahrrad Übung

class Fahrrad():
    def __init__(self,marke,anz_zahnkraenze,anz_ritzel,zahnkranz,ritzel):
        self.marke=marke
        self.anz_zahnkraenze =anz_zahnkraenze
        self.anz_ritzel=anz_ritzel
        self.zahnkranz=zahnkranz
        self.ritzel=ritzel

    def get_marke(self):
        print(self.marke)

    def get_anz_zahnkraenze(self):
        print(self.anz_zahnkraenze)

fh= Fahrrad("lo",2,3,4,5)

fh.get_marke()