class MemoriaDinamica():

    def __init__(self,frutas):
        self.frutas = frutas

    def add(self,fruta):
        self.frutas.append(fruta)

    def remove(self,fruta):
        self.frutas.remove(fruta)

    def listaFrutas(self):
        print(self.frutas)

canasta = MemoriaDinamica([])
canasta.add("mango")
canasta.add("manzana")
canasta.add("banana")
canasta.add("uvas")
canasta.add("sandia")
canasta.remove("mango")
canasta.listaFrutas()
    