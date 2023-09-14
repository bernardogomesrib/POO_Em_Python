class Televisao:
    def __init__(self,tamanho = 10,marca = "generica"):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca

    def oqestouFazendo(self,var):
        print(var)

    def setCanal(self,var):
        self.oqestouFazendo(f"Estou mudando de canal para o canal {var}")
        self.canal = var

    def Ligar(self):
        self.oqestouFazendo("Estou sendo ligada")
        self.ligada = True

    def Desligar(self):
        self.oqestouFazendo("Estou desligando")
        self.ligada = False
    
    def getTamanho(self):
        return self.tamanho

    def getMarca(self):
        return self.marca

tv = Televisao()
print(tv.ligada)
print(tv.canal)
print(tv.getMarca())
print(tv.getTamanho())
tv_sala = Televisao()
tv_sala.Ligar()
tv_sala.setCanal(3)
tv_grande = Televisao(tamanho=69)
print(tv_grande.getTamanho())
tv_sangsuga = Televisao(marca="Sangsuga",tamanho=70)
print(tv_sangsuga.getMarca())
print(tv_sangsuga.getTamanho())
