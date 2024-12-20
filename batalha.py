import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):

    
    def especial(self, inimigo):
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa 30 de Dano!")
        inimigo.vida -=30
    

class Mago(Personagem):


    def especial(self):
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")   
        self.vida +=25


class Arqueiro(Personagem):


    def especial(self,inimigo):
        print(f"{self.nome} usa Chuva de Flechas e Causa 15 de Dano a Todos os Inimigos!")
        for inimigo1 in inimigo:
            if(inimigo1.nome !=self.nome):
                inimigo1.vida-=15

def importar_personagens(caminho):
    with open(caminho, 'r') as file:
        dados = json.load(file)
    
    personagens = []
    if(dados):
        for dado in dados:
            if(dado["classe"] == "Guerreiro"):
                personagens.append(Guerreiro(dado["nome"],dado["vida"],dado["ataque"]))
            
            elif(dado["classe"] == "Mago"):
                personagens.append(Mago(dado["nome"],dado["vida"],dado["ataque"]))
            else:
                personagens.append(Arqueiro(dado["nome"],dado["vida"],dado["ataque"]))
        return personagens, len(personagens)
    

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda p: p.vida, reverse=False)

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])