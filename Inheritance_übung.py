#Klassendiagramm mit Person Pensionierter Kind und Erwachsener

class Person:
    def __init__(self, name, male, alter):
        if not isinstance(name,str):
            raise TypeError("name must be string")
        if not isinstance(male,bool):
            raise TypeError("male must be boolean")
        if not isinstance(alter,int):
            raise TypeError("alter must be integer")
        self.name = name
        self.male = male
        self.alter = alter




    def print_beschreibung(self):
        print("Ich heisse " + self.name + " und bin " + str(self.alter) +\
              " Jahre alt und bin ein " + self.Klassenname)

    @property
    def alter(self):
        return self.__alter

    @alter.setter
    def alter(self,alter):
        if alter < 0:
            raise ValueError("alter must be positive")
        self.__alter = alter
        try:
            self.__alter = int(alter)
        except ValueError:
            raise ValueError("alter must be integer")

class Pensionierter(Person):
    def __int__(self,name,male,alter, rente, Klassenname="Pensionierter(in)"):
        super().__init__(name,male,alter)
        if not isinstance(rente, int):
            raise TypeError("rente must be integer")
        if not isinstance(Klassenname, str):
            raise TypeError("Klassenname must be string")
        self.rente = rente
        self.Klassenname = Klassenname

    @property
    def rente(self):
        return self.__rente

    @rente.setter
    def rente(self,rente):
        if rente < 0:
            raise ValueError("rente must be positive")
        self.__rente = rente
        try:
            self.__rente = int(rente)
        except ValueError:
            raise ValueError("rente must be integer")

class Kind(Person):
    def __init__(self,name,male,alter, anzahl_zaehne, spielzeug, Klassenname="Kind"):
        super().__init__(name,male,alter)
        if not isinstance(Klassenname, str):
            raise TypeError("Klassenname must be string")
        if not isinstance(anzahl_zaehne, int):
            raise TypeError("anzahl_zaehne must be integer")
        if not isinstance(spielzeug, str):
            raise TypeError("spielzeug must be string")
        self.spielzeug = spielzeug
        self.Klassenname = Klassenname
        self.anzahl_zaehne = anzahl_zaehne

    @property
    def anzahl_zaehne(self):
        return self.__anzahl_zaehne

    @anzahl_zaehne.setter
    def anzahl_zaehne(self,anzahl_zaehne):
        if anzahl_zaehne < 0:
            raise ValueError("anzahl_zaehne must be positive")
        self.__anzahl_zaehne = anzahl_zaehne
        try:
            self.__anzahl_zaehne = int(anzahl_zaehne)
        except ValueError:
            raise ValueError("anzahl_zaehne must be integer")

    def spielzeug_tauschen(self, spielzeug):
        self.spielzeug = spielzeug
        print("Ich tausche mein " + self.spielzeug + " gegen " + spielzeug)

class Erwachsener(Person):
    def __init__(self,name, male, alter, Lohn, ist_verheiratet, kinder=None, Klassenname="Erwachsener"):
        super().__init__(name, male, alter)
        if not isinstance(Lohn, int):
            raise TypeError("Lohn must be integer")
        if not isinstance(ist_verheiratet, bool):
            raise TypeError("ist_verheiratet must be boolean")
        self.Lohn = Lohn
        self.ist_verheiratet = ist_verheiratet
        if kinder is None:
            kinder = []
        self.kinder = kinder
        self.Klassenname = Klassenname


    @property
    def Lohn(self):
        return self.__Lohn

    @Lohn.setter
    def Lohn(self,Lohn):
        if Lohn < 0:
            raise ValueError("Lohn must be positive")
        self.__Lohn = Lohn
        try:
            self.__Lohn = int(Lohn)
        except ValueError:
            raise ValueError("Lohn must be integer")

    def print_kinder(self):
          for i in range(len(self.kinder)):
            print(self.kinder[i])
            if i < len(self.kinder)-1:
                print("und")

E1=Erwachsener("Hans", True, 40, 5000, True, ["Julia","fritz"],"Erwachsener")
E1.print_kinder()
E1.print_beschreibung()

class coinflip():
    def __init__(self,coinnumber):
        self.coinnumber = coinnumber
        self.resultlist = []
    def flip(self):
        import random

        for i in range(self.coinnumber):
            x = random.randint(0,1)
            if x == 0:
                self.resultlist.append("Kopf")
            if x== 1:
                self.resultlist.append("Zahl")
        return self.resultlist

    def print_result(self):
        print(self.resultlist)

    
game = coinflip(10)

game.flip()
game.print_result()