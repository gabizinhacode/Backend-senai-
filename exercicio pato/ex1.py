#Uma empresa de jogos digitais esta criando um simulador de animais. Um dos personagens sera um pato, que deve ser capaz de voar e nadar 
#crie e classe voador com metodo voar()
#crie a classe aquatico com o metodo nadar()
#crie a classe pato que herda de ambas e implemnte os comportamentos
# Para herdar de 2 utilize class nome_da_classe(pai1, pai2): 

class Voador:
    def voar(self):
        return "O pato da gabi esta voando"
    
class Aquatico: 
    def nadar(self):
        return "O pato da gabi esta nadando"

class Pato(Voador, Aquatico):
    pass 

pato = Pato()
print(pato.voar())
print(pato.nadar())

