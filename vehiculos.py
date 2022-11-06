class Vehiculo():
    def __init__(self, color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return "color {}, {} ruedas".format (self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo=tipo

    def __str__(self):
        return "Biciclera color {}, {} ruedas, tipo {}".format(self.color, self.ruedas, self. tipo)


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo=tipo
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return "Motocicleta color {}, {} ruedas, tipo {}, {} km/h, {} cc".format(self.color, self.ruedas, self. tipo, self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
        self.carga=carga


    def __str__(self):
        return "Camioneta color {}, {} ruedas, {} km/h, {} cc, {} kg".format(self.color, self.ruedas, self.velocidad, self. cilindrada, self.carga)

coche= Coche("blanco", 4, 160, 1000)
bicicleta=Bicicleta("rosa", 2, "montaña")
moto=Motocicleta("azul", 3, "urbana", 120, 125)
camion=Camioneta("amarillo",4, 140, 1200, 6000)


lista_vehiculos=[]
lista_vehiculos.append(coche)
lista_vehiculos.append(bicicleta)
lista_vehiculos.append(moto)
lista_vehiculos.append(camion)

def catalogar(lista_vehiculos):
    for c in lista_vehiculos:
        print("Clase:", type(c).__name__)
        print("Atributos", c)

def catalog(lista_vehiculos, num_ruedas = -1):
    if num_ruedas== -1:
        for c in lista_vehiculos:
            print("Clase:", type(c).__name__)
            print("Atributos:", c)
    else:
        a_ruedas = []
        for r in lista_vehiculos:
            c_ruedas=r.ruedas
            if c_ruedas==num_ruedas:
                a_ruedas.append(r)
        print("Se han encontrado {} vehiculos con {} ruedas".format(len(a_ruedas), num_ruedas))
        for a in a_ruedas:
            print(a)

catalog(lista_vehiculos)            







