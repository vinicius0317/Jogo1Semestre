import pygame
from pygame.locals import *
from sys import exit
from time import sleep, time
from random import randint

#Inicialização
pygame.init()
pygame.display.set_caption('Mediévico Reis')
largura = 1200
altura = 720
delay = 1


#Base de Texto
base_font_titulo = pygame.font.SysFont('algerian', 40)
base_font_carta = pygame.font.SysFont('algerian', 19)
user_text = ''
user_titulo = 'Comunicado do Rei' 
user_linha1 = 'Bem vindos ao Medievicos Reis, eu sou o Rei e organizador do torneio, será que você é capaz de vencer todos' 
user_linha2 = 'e conquistar a cobiçada plantação de arroz?'
user_linha3 = ' para confirmar sua participação insira seu nome'
input_rect = pygame.Rect(550, 500, 140, 32)
TextoSelecionado = pygame.Color('lightskyblue3')
TextoNaoSelecionado = pygame.Color('gray15')
color = TextoNaoSelecionado
BTexto = False

Morreu = 0

#Variaveis
VidaMaxPersonagem = 100
ManaMaxPersonagem = 100
VidaAtualPersonagem = 100
ManaAtualPersonagem = 100
ValorPreencherVidaPersonagem = 120
ValorPreencherManaPersonagem = 120
VidaMaxInimigo = 100
ManaMaxInimigo = 100
VidaAtualInimigo = 100
ManaAtualInimigo = 100

RealizandoAcao = False
SituacaoAtk = 0
#0 = nulo, 1 = indo, 2 = voltando

EstadoEvasao = False
EstadoSonolento = False

EstadoEvasaoInimigo = False
EstadoSonolentoInimigo = False

AtkSoniferoInimigo = False

InimigoMorreu = False

MovimentoSaindo = 5

AtkBasico = False
AtkMeteoro = False
AtkEvasao = False
AtkSonifero = False
AtkSupremo = False
AtkSupremoInimigo = False

Acao = 0
AcaoInimigo = 0

RecargaPocaoVida = 3
RecargaPocaoMana = 3
RecargaPocaoVidaIni = 3
RecargaPocaoManaIni = 3

DanoReduzido = 2

OndaAtual = 0
InimigoAtual = 0
NInimigos = 4
NOndas = 4

PosicaoAtualPrincipal = 0
PosicaoAtualInimigo = 0
PosicaoAtualMeteoro = 0
PosicaoAtualMeteoroInimigo = 0
PosicaoEspadaSonifero = 0
PosicaoEspadaSoniferoInimigo = 0
EspadaAtual = 0
EspadaAtualInimigo = 0
iPosicoes = 0
TurnoAtual = 1

ManaAtkBasico = 0
ManaEvasao = 20
ManaMeteoro = 40
ManaSonifero = 50
ManaAtkSupremo = 60

ManaAtks = []
ManaAtks.append(0)
ManaAtks.append(20)
ManaAtks.append(40)
ManaAtks.append(50)
ManaAtks.append(60)

PersoEnfraquecido = False
PersoDormindo = False
InimigoEnfraquecido = 2
InimigoDormindo = 2

EsperarEvacao = False
#Para dar um delay e esperar pra mostrar o texto de miss


Timer = pygame.time.Clock()

Madeira = []
'''Posições Espadas
    Madeira[0] = Espada / Madeira[1] = Sabre / Madeira[2] = Katana / Madeira[3] = Espada2 / Madeira[4] = Adaga '''
Cobre = []
'''Posições Sabres
    Cobre[0] = Espada / Cobre[1] = Sabre / Cobre[2] = Katana / Cobre[3] = Espada2 / Cobre[4] = Adaga '''
Mithral = []
'''Posições Sabres
    Mithral[0] = Espada / Mithral[1] = Sabre / Mithral[2] = Katana / Mithral[3] = Espada2 / Mithral[4] = Adaga '''

AcoNegro = []
'''Posições Sabres
    AcoNegro[0] = Espada / AcoNegro[1] = Sabre / AcoNegro[2] = Katana / AcoNegro[3] = Espada2 / AcoNegro[4] = Adaga '''

Diamante = []
'''Posições Sabres
    Diamante[0] = Espada / Diamante[1] = Sabre / Diamante[2] = Katana / Diamante[3] = Espada2 / Diamante[4] = Adaga '''


Inimigos1 = []
Inimigos2 = []
Inimigos3 = []
Inimigos4 = []
Inimigos5 = []

QtdInimigos = []
QtdInimigos.append(1)
QtdInimigos.append(2)
QtdInimigos.append(3)
QtdInimigos.append(4)
QtdInimigos.append(5)



Personagens = []
''' Posições Personagens[0] = perso0 Azul / Personagens[1] = perso1 Verde / Personagens[2] = perso2 VerdeAgua / Personagens[3] = perso3 Vermelho
'''

#Lista Personagens
'''P = pygame.image.load('data/Personagens/perso0.png')
Personagens.append(P)
P = pygame.image.load('data/Personagens/perso1.png')
Personagens.append(P)
P = pygame.image.load('data/Personagens/perso2.png')
Personagens.append(P)
P = pygame.image.load('data/Personagens/perso3.png')
Personagens.append(P)'''

#Posições Personagem principal 
PosicoesXPersoPrin = []
PosicoesXPersoPrin.append(250)
PosicoesXPersoPrin.append(300)
PosicoesXPersoPrin.append(350)
PosicoesXPersoPrin.append(400)
PosicoesXPersoPrin.append(450)
PosicoesXPersoPrin.append(500)
PosicoesXPersoPrin.append(550)
PosicoesXPersoPrin.append(575)
PosicoesXPersoPrin.append(600)

PosicoesYPersoPrin = []
PosicoesYPersoPrin.append(400)
PosicoesYPersoPrin.append(350)
PosicoesYPersoPrin.append(300)
PosicoesYPersoPrin.append(275)
PosicoesYPersoPrin.append(250)
PosicoesYPersoPrin.append(275)
PosicoesYPersoPrin.append(300)
PosicoesYPersoPrin.append(340)
PosicoesYPersoPrin.append(420)

#Posições Inimigo
PosicoesXInimigo = []
PosicoesXInimigo.append(800)
PosicoesXInimigo.append(750)
PosicoesXInimigo.append(700)
PosicoesXInimigo.append(650)
PosicoesXInimigo.append(600)
PosicoesXInimigo.append(550)
PosicoesXInimigo.append(500)
PosicoesXInimigo.append(475)
PosicoesXInimigo.append(450)

PosicoesYInimigo = []
PosicoesYInimigo.append(400)
PosicoesYInimigo.append(350)
PosicoesYInimigo.append(300)
PosicoesYInimigo.append(275)
PosicoesYInimigo.append(250)
PosicoesYInimigo.append(275)
PosicoesYInimigo.append(300)
PosicoesYInimigo.append(340)
PosicoesYInimigo.append(420)




#PosiçõesEspada Personagem principal
PosicoesXEspada = []
PosicoesXEspada.append(450)
PosicoesXEspada.append(500)
PosicoesXEspada.append(505)
PosicoesXEspada.append(560)
PosicoesXEspada.append(600)
PosicoesXEspada.append(650)
PosicoesXEspada.append(700)
PosicoesXEspada.append(740)
PosicoesXEspada.append(780)

PosicoesYEspada = []
PosicoesYEspada.append(420)
PosicoesYEspada.append(370)
PosicoesYEspada.append(320)
PosicoesYEspada.append(290)
PosicoesYEspada.append(260)
PosicoesYEspada.append(290)
PosicoesYEspada.append(320)
PosicoesYEspada.append(375)
PosicoesYEspada.append(430)

#PosiçõesEspada Inimigo
PosicoesXEspadaInimigo = []
PosicoesXEspadaInimigo.append(730)
PosicoesXEspadaInimigo.append(680)
PosicoesXEspadaInimigo.append(675)
PosicoesXEspadaInimigo.append(620)
PosicoesXEspadaInimigo.append(580)
PosicoesXEspadaInimigo.append(530)
PosicoesXEspadaInimigo.append(480)
PosicoesXEspadaInimigo.append(440)
PosicoesXEspadaInimigo.append(400)

PosicoesYEspadaInimigo = []
PosicoesYEspadaInimigo.append(420)
PosicoesYEspadaInimigo.append(370)
PosicoesYEspadaInimigo.append(320)
PosicoesYEspadaInimigo.append(290)
PosicoesYEspadaInimigo.append(260)
PosicoesYEspadaInimigo.append(290)
PosicoesYEspadaInimigo.append(320)
PosicoesYEspadaInimigo.append(375)
PosicoesYEspadaInimigo.append(430)


PosicoesXAtkMeteoro = []
PosicoesXAtkMeteoro.append(1500) #Fora da Tela
PosicoesXAtkMeteoro.append(250)
PosicoesXAtkMeteoro.append(340)
PosicoesXAtkMeteoro.append(430)
PosicoesXAtkMeteoro.append(520)
PosicoesXAtkMeteoro.append(610)
PosicoesXAtkMeteoro.append(700)
PosicoesXAtkMeteoro.append(800)

PosicoesYAtkMeteoro = []
PosicoesYAtkMeteoro.append(1500) #Fora da Tela
PosicoesYAtkMeteoro.append(100)
PosicoesYAtkMeteoro.append(150)
PosicoesYAtkMeteoro.append(200)
PosicoesYAtkMeteoro.append(250)
PosicoesYAtkMeteoro.append(300)
PosicoesYAtkMeteoro.append(350)
PosicoesYAtkMeteoro.append(400)


PosicoesXAtkMeteoroInimigo = []
PosicoesXAtkMeteoroInimigo.append(1500) #Fora da Tela
PosicoesXAtkMeteoroInimigo.append(880)
PosicoesXAtkMeteoroInimigo.append(800)
PosicoesXAtkMeteoroInimigo.append(700)
PosicoesXAtkMeteoroInimigo.append(610)
PosicoesXAtkMeteoroInimigo.append(520)
PosicoesXAtkMeteoroInimigo.append(430)
PosicoesXAtkMeteoroInimigo.append(340)

PosicoesYAtkMeteoroInimigo = []
PosicoesYAtkMeteoroInimigo.append(1500) #Fora da Tela
PosicoesYAtkMeteoroInimigo.append(100)
PosicoesYAtkMeteoroInimigo.append(150)
PosicoesYAtkMeteoroInimigo.append(200)
PosicoesYAtkMeteoroInimigo.append(250)
PosicoesYAtkMeteoroInimigo.append(300)
PosicoesYAtkMeteoroInimigo.append(350)
PosicoesYAtkMeteoroInimigo.append(400)

PosicoesXInimigoSaindo = []
PosicoesXInimigoSaindo.append(800)
PosicoesXInimigoSaindo.append(900)
PosicoesXInimigoSaindo.append(1000)
PosicoesXInimigoSaindo.append(1100)

PosicoesYInimigoSaindo = []
PosicoesYInimigoSaindo.append(400)
PosicoesYInimigoSaindo.append(350)
PosicoesYInimigoSaindo.append(400)
PosicoesYInimigoSaindo.append(350)


VidaMaxInimigos1 = 100 #[]
VidaMaxInimigos2 = 350 #[]
VidaMaxInimigos3 = 600 #[]
VidaMaxInimigos4 = 850 #[]
VidaMaxInimigos5 = 1150 #[]

#Inseridno Vida dos inimigos
'''VidaInimigos1.append(100)
VidaInimigos2.append(350)
VidaInimigos3.append(600)
VidaInimigos4.append(850)
VidaInimigos5.append(1150)'''


AtaquesSkills = []
AS = pygame.image.load('data/Habilidades/AtkBasico.png')
AtaquesSkills.append(AS)
AS = pygame.image.load('data/Habilidades/Escudo.png')
AtaquesSkills.append(AS)
AS = pygame.image.load('data/Habilidades/Meteoro.png')
AtaquesSkills.append(AS)
AS = pygame.image.load('data/Habilidades/zZz.png')
AtaquesSkills.append(AS)
AS = pygame.image.load('data/Habilidades/AtkSupremo.png')
AtaquesSkills.append(AS)

Pocoes = []
P = pygame.image.load('data/Pocoes/PocaoVida.png')
Pocoes.append(P)
P = pygame.image.load('data/Pocoes/PocaoMana.png')
Pocoes.append(P)
P = pygame.image.load('data/Pocoes/PocaoVazia.png')
Pocoes.append(P)

AtksInimigos = []
AtksInimigos.append(1)
AtksInimigos.append(2)
AtksInimigos.append(3)
AtksInimigos.append(4)
AtksInimigos.append(5)
AtksInimigos.append(6)


ManaAtkBasico = 0
ManaEvasao = 20
ManaMeteoro = 40
ManaSonifero = 50
ManaStkSupremo = 60
AtkInimigo = 8
#AtkInimigo vai de 0 a 4
#Declarado como 8 para não bugar no começo


QtdManaAtkInimigo = []
QtdManaAtkInimigo.append(0)
QtdManaAtkInimigo.append(20)
QtdManaAtkInimigo.append(40)
QtdManaAtkInimigo.append(50)
QtdManaAtkInimigo.append(60)
''' QtdManaAtkInimigo[0] = 0 Atk Basico / QtdManaAtkInimigo[1] = 20 Evasão / QtdManaAtkInimigo[2] = 40 Meteoro / QtdManaAtkInimigo[3] = 50 Sonífero
    QtdManaAtkInimigo[4] = 60 Atk Supremo'''
#QtdManaAtkInimigo.append(6)


#Inserindo Madeira na lista
M = pygame.image.load('data/Espadas/EspadaMadeira.png')
Madeira.append(M)
M = pygame.image.load('data/Sabres/SabreMadeira.png')
Madeira.append(M)
M = pygame.image.load('data/Katanas/KatanaMadeira.png')
Madeira.append(M)
M = pygame.image.load('data/Espadas2/Espada2Madeira.png')
Madeira.append(M)
M = pygame.image.load('data/Adagas/AdagaMadeira.png')
Madeira.append(M)

#Inserindo Cobre na lista
C = pygame.image.load('data/Espadas/EspadaCobre.png')
Cobre.append(C)
C = pygame.image.load('data/Sabres/SabreCobre.png')
Cobre.append(C)
C = pygame.image.load('data/Katanas/KatanaCobre.png')
Cobre.append(C)
C = pygame.image.load('data/Espadas2/Espada2Cobre.png')
Cobre.append(C)
C = pygame.image.load('data/Adagas/AdagaCobre.png')
Cobre.append(C)

#Inserindo Mithral na lista
MT = pygame.image.load('data/Espadas/EspadaMithral.png')
Mithral.append(MT)
MT = pygame.image.load('data/Sabres/SabreMithral.png')
Mithral.append(MT)
MT = pygame.image.load('data/Katanas/KatanaMithral.png')
Mithral.append(MT)
MT = pygame.image.load('data/Espadas2/Espada2Mithral.png')
Mithral.append(MT)
MT = pygame.image.load('data/Adagas/AdagaMithral.png')
Mithral.append(MT)

#Inserindo AcoNegro na lista
AN = pygame.image.load('data/Espadas/EspadaAcoNegro.png')
AcoNegro.append(AN)
AN = pygame.image.load('data/Sabres/SabreAcoNegro.png')
AcoNegro.append(AN)
AN = pygame.image.load('data/Katanas/KatanaAcoNegro.png')
AcoNegro.append(AN)
AN = pygame.image.load('data/Espadas2/Espada2AcoNegro.png')
AcoNegro.append(AN)
AN = pygame.image.load('data/Adagas/AdagaAcoNegro.png')
AcoNegro.append(AN)

#Inserindo Diamante na lista
D = pygame.image.load('data/Espadas/EspadaDiamante.png')
Diamante.append(D)
D = pygame.image.load('data/Sabres/SabreDiamante.png')
Diamante.append(D)
D = pygame.image.load('data/Katanas/KatanaDiamante.png')
Diamante.append(D)
D = pygame.image.load('data/Espadas2/Espada2Diamante.png')
Diamante.append(D)
D = pygame.image.load('data/Adagas/AdagaDiamante.png')
Diamante.append(D)


#Lista inimigos onda 1. Aqui vai inserir os inimigos da primeira onda
'''I1 = pygame.image.load('data/Katanas/KatanaMadeira.png')
Inimigos1.append(K)
I1 = pygame.image.load('data/Katanas/KatanaCobre.png')
Inimigos1.append(K)
I1 = pygame.image.load('data/Katanas/KatanaMithral.png')
Inimigos1.append(K)
I1 = pygame.image.load('data/Katanas/KatanaAcoNegro.png')
Inimigos1.append(K)
I1 = pygame.image.load('data/Katanas/KatanaDiamante.png')
Inimigos1.append(K)'''



#Lista inimigos onda 1. Aqui vai inserir os inimigos da segunda onda
'''I2 = pygame.image.load('data/Katanas/KatanaMadeira.png')
Inimigos2.append(K)
I2 = pygame.image.load('data/Katanas/KatanaCobre.png')
Inimigos2.append(K)
I2 = pygame.image.load('data/Katanas/KatanaMithral.png')
Inimigos2.append(K)
I2 = pygame.image.load('data/Katanas/KatanaAcoNegro.png')
Inimigos2.append(K)
I2 = pygame.image.load('data/Katanas/KatanaDiamante.png')
Inimigos2.append(K)'''

#Lista inimigos onda 1. Aqui vai inserir os inimigos da terceira onda
'''I3 = pygame.image.load('data/Katanas/KatanaMadeira.png')
Inimigos3.append(K)
I3 = pygame.image.load('data/Katanas/KatanaCobre.png')
Inimigos3.append(K)
I3 = pygame.image.load('data/Katanas/KatanaMithral.png')
Inimigos3.append(K)
I3 = pygame.image.load('data/Katanas/KatanaAcoNegro.png')
Inimigos3.append(K)
I3 = pygame.image.load('data/Katanas/KatanaDiamante.png')
Inimigos3.append(K)'''

#Lista inimigos onda 1. Aqui vai inserir os inimigos da quarta onda
'''I4 = pygame.image.load('data/Katanas/KatanaMadeira.png')
Inimigos4.append(K)
I4 = pygame.image.load('data/Katanas/KatanaCobre.png')
Inimigos4.append(K)
I4 = pygame.image.load('data/Katanas/KatanaMithral.png')
Inimigos4.append(K)
I4 = pygame.image.load('data/Katanas/KatanaAcoNegro.png')
Inimigos4.append(K)
I4 = pygame.image.load('data/Katanas/KatanaDiamante.png')
Inimigos4.append(K)'''

#Lista inimigos onda 1. Aqui vai inserir os inimigos da quinta onda
'''I5 = pygame.image.load('data/Katanas/KatanaMadeira.png')
Inimigos5.append(K)
I5 = pygame.image.load('data/Katanas/KatanaCobre.png')
Inimigos5.append(K)
I5 = pygame.image.load('data/Katanas/KatanaMithral.png')
Inimigos5.append(K)
I5 = pygame.image.load('data/Katanas/KatanaAcoNegro.png')
Inimigos5.append(K)
I5 = pygame.image.load('data/Katanas/KatanaDiamante.png')
Inimigos5.append(K)'''


#Tamanho das Espadas
i = 0
while i < 5:
    Madeira[i] = pygame.transform.scale(Madeira[i], [100, 130])
    i += 1
#Tamanho dos Sabres
i = 0
while i < 5:
    Cobre[i] = pygame.transform.scale(Cobre[i], [100, 130])
    i += 1
#Tamanho das Katanas
i = 0
while i < 5:
    Mithral[i] = pygame.transform.scale(Mithral[i], [100, 130])
    i += 1

#Tamanho das Adagas
i = 0
while i < 5:
    AcoNegro[i] = pygame.transform.scale(AcoNegro[i], [100, 130])
    i += 1

#Tamanho das Espadas2
i = 0
while i < 5:
    Diamante[i] = pygame.transform.scale(Diamante[i], [100, 130])
    i += 1

#Tamanho icones Habilidades
i = 0
while i < 5:
    AtaquesSkills[i] = pygame.transform.scale(AtaquesSkills[i], [90, 60])
    i += 1



#Background Grafico
TelaInicial = True
TelaPersonagem = False
Inicializacao = False
TelaLuta1 = False
TelaPause = False
TelaMorreu = False
tela = pygame.display.set_mode((largura, altura))
Background = pygame.image.load('data/NomeJogo2.png')
Arena = pygame.image.load('data/fundo2.png')
fundo = pygame.image.load('data/fundo.png')

TelaPause = pygame.image.load('data/TelaPause.png')

ImgMorreu = pygame.image.load('data/TelaMorreu.png')

imgEsquivou = pygame.image.load('data/Habilidades/Evasao.png')

imgDormindo = pygame.image.load('data/Habilidades/zZz.png')


#Texto Vida / Mana
pygame.font.init()
#TxtVida = VidaAtualPersonagem
fonte = pygame.font.match_font('algerian')
fonteVidaMana = pygame.font.SysFont(fonte, 25)
fonteEvasao = pygame.font.SysFont(fonte, 35)
fonteEnfraquecido = pygame.font.SysFont(fonte, 25)
fonteMorreu = pygame.font.SysFont(fonte, 40)
TxtVida = fonteVidaMana.render(str(VidaAtualPersonagem), 1, (0,0,0))
TxtMana = fonteVidaMana.render(str(ManaAtualPersonagem), 1, (0,0,0))
TxtVidaInimigo = fonteVidaMana.render(str(VidaAtualInimigo), 1, (0,0,0))
TxtManaInimigo = fonteVidaMana.render(str(ManaAtualInimigo), 1, (0,0,0))


#Objetos

drawGroup = pygame.sprite.Group()
DrawPersoPrincipal = pygame.sprite.Group()
DrawEspadaPrincipal = pygame.sprite.Group()
DrawMeteoro = pygame.sprite.Group()
DrawInimigoSaindo = pygame.sprite.Group()


#Seleção de personagem

Blue = False
Greenw = False
Selecionou = False
Selecionado = 0
Chapeu = 0



def DesenhaPosicao(Selecionado, Posicao, Acao):
    #Acao / 0 = Parado , 1 = Primeiro Salto , 2 = caindo , 3 = no ar, 4 = Dano, 5 = Sono
    DrawPersoPrincipal = pygame.sprite.Group()
    
    perso = pygame.sprite.Sprite(DrawPersoPrincipal)
    #perso.image = Personagens[Selecionado]
    if Acao == 0:
        perso.image = pygame.image.load('data/Personagens/perso'+str(Selecionado)+str(Chapeu)+'.png')
    elif Acao == 1:
        perso.image = pygame.image.load('data/PersonagensPulando/perso'+str(Selecionado)+str(Chapeu)+'.png')
    elif Acao == 2:
        perso.image = pygame.image.load('data/PersonagensCaindo/perso'+str(Selecionado)+str(Chapeu)+'.png')
    elif Acao == 3:
        perso.image = pygame.image.load('data/PersonagensNoAr/perso'+str(Selecionado)+str(Chapeu)+'.png')
    elif Acao == 4:
        perso.image = pygame.image.load('data/PersonagensDano/perso'+str(Selecionado)+str(Chapeu)+'.png')
    elif Acao == 5:
        perso.image = pygame.image.load('data/PersonagensSono/perso'+str(Selecionado)+str(Chapeu)+'.png')
        
    perso.image = pygame.transform.scale(perso.image, [230, 200])
    
    #perso.image = perso.image.copy()
    #perso.image = pygame.transform.flip(perso.image, True, False)

    perso.rect = pygame.Rect(PosicoesXPersoPrin[Posicao], PosicoesYPersoPrin[Posicao], 100, 100)
    
    ''' Posições X respectivamente 250, 350, 450, 550, 600
        Posições Y respectivamente 400, 300, 250, 300, 380'''
        
    DrawPersoPrincipal.draw(tela)
    

def DesenhaPosicaoInimigo(Posicao, Onda, InimigoAtual, Acao, Saindo = ''):
    #Acao / 0 = Parado , 1 = Primeiro Salto , 2 = caindo , 3 = no ar, 4 = Dano, 5 = Dormindo
    InimigoPos1 = pygame.sprite.Group()
    inimigo = pygame.sprite.Sprite(InimigoPos1)
    
    #inimigo.image = pygame.image.load('data/Personagens/perso0.png')
    if Acao == 0:
        inimigo.image = pygame.image.load('data/Inimigos/ini'+str(Onda)+str(InimigoAtual)+'.png')
    elif Acao == 1:
        inimigo.image = pygame.image.load('data/InimigosPulando/ini'+str(Onda)+str(InimigoAtual)+'.png')
    elif Acao == 2:
        inimigo.image = pygame.image.load('data/InimigosCaindo/ini'+str(Onda)+str(InimigoAtual)+'.png')
    elif Acao == 3:
        inimigo.image = pygame.image.load('data/InimigosNoAr/ini'+str(Onda)+str(InimigoAtual)+'.png')
    elif Acao == 4:
        inimigo.image = pygame.image.load('data/InimigosDano/ini'+str(Onda)+str(InimigoAtual)+'.png')
    elif Acao == 5:
        inimigo.image = pygame.image.load('data/InimigosSono/ini'+str(Onda)+str(InimigoAtual)+'.png')

    if Saindo == 'Saindo':
        inimigo.image = pygame.transform.scale(inimigo.image, [230, 200])
        inimigo.image = inimigo.image.copy()
        inimigo.image = pygame.transform.flip(inimigo.image, True, False)
        inimigo.rect = pygame.Rect(PosicoesXInimigoSaindo[Posicao], PosicoesYInimigoSaindo[Posicao], 100, 100)
    else:
        inimigo.image = pygame.transform.scale(inimigo.image, [230, 200])
        inimigo.rect = pygame.Rect(PosicoesXInimigo[Posicao], PosicoesYInimigo[Posicao], 100, 100)
        InimigoPos1.draw(tela)

    

def DesenhaPosicaoEspada(OndaAtual, Posicao, TipoEspada, Ataque = ''):
    #TipoEspada --- 1 = Madeira  2 = Cobre  3 = Mithral  4 = AcoNegro  5 = Diamante
    DrawEspadaPrincipal = pygame.sprite.Group()
    
    espadaprin = pygame.sprite.Sprite(DrawEspadaPrincipal)
    if OndaAtual == 0:
        if(OndaAtual == 0 and (TipoEspada == 0 or TipoEspada == 1)):
            espadaprin.image = Madeira[0]
        else:
            espadaprin.image = Madeira[TipoEspada - 1]
    elif OndaAtual == 1:
        if(OndaAtual == 1 and TipoEspada == 0):
            espadaprin.image = Madeira[4]
        else:
            espadaprin.image = Cobre[TipoEspada - 1]
    elif OndaAtual == 2:
        if(OndaAtual == 2 and TipoEspada == 0):
            espadaprin.image = Cobre[4]
        else:
            espadaprin.image = Mithral[TipoEspada - 1]
    elif OndaAtual == 3:
        if(OndaAtual == 3 and TipoEspada == 0):
            espadaprin.image = Mithral[4]
        else:
            espadaprin.image = AcoNegro[TipoEspada - 1]
    elif OndaAtual == 4:
        if(OndaAtual == 4 and TipoEspada == 0):
            espadaprin.image = AcoNegro[4]
        else:
            espadaprin.image = Diamante[TipoEspada - 1]
    
    #espadaprin.image = pygame.transform.scale(espadaprin.image, [100, 130])
    espadaprin.image = espadaprin.image.copy()
    
    if Posicao == 2 or Posicao == 3 or Posicao == 4 or Posicao == 5 or Posicao == 6:
        espadaprin.image = pygame.transform.flip(espadaprin.image, False, False)
    else:
        espadaprin.image = pygame.transform.flip(espadaprin.image, True, False)
        
    if Ataque == 'Sonifero':
        espadaprin.image = pygame.transform.rotate(espadaprin.image, -60)
        
    espadaprin.rect = pygame.Rect(PosicoesXEspada[Posicao], PosicoesYEspada[Posicao], 100, 130)

    ''' Posições X respectivamente 450, 550, 600, 700, 780
        Posições Y respectivamente 420, 320, 260, 320, 430'''    
    
    DrawEspadaPrincipal.draw(tela)


def DesenhaPosicaoEspadaInimigo(OndaAtual, Posicao, TipoEspada, Ataque = ''):
    #TipoEspada --- 0 = Madeira  1 = Cobre  2 = Mithral  3 = AcoNegro  4 = Diamante
    DrawEspadaInimigo = pygame.sprite.Group()
    
    espadaini = pygame.sprite.Sprite(DrawEspadaInimigo)
    if OndaAtual == 0:
        espadaini.image = Madeira[TipoEspada]
    elif OndaAtual == 1:
        espadaini.image = Cobre[TipoEspada]
    elif OndaAtual == 2:
        espadaini.image = Mithral[TipoEspada]
    elif OndaAtual == 3:
        espadaini.image = AcoNegro[TipoEspada]
    elif OndaAtual == 4:
        espadaini.image = Diamante[TipoEspada]
    #espadaprin.image = pygame.transform.scale(espadaprin.image, [100, 130])
    espadaini.image = espadaini.image.copy()
    
    if Posicao == 0 or Posicao == 1 or Posicao == 7 or Posicao == 8:
        espadaini.image = pygame.transform.flip(espadaini.image, False, False)
    else:
        espadaini.image = pygame.transform.flip(espadaini.image, True, False)

    if Ataque == 'Sonifero':
        espadaini.image = pygame.transform.rotate(espadaini.image, 60)
        
    espadaini.rect = pygame.Rect(PosicoesXEspadaInimigo[Posicao], PosicoesYEspadaInimigo[Posicao], 100, 130)

    ''' Posições X respectivamente 450, 550, 600, 700, 780
        Posições Y respectivamente 420, 320, 260, 320, 430'''    
    
    DrawEspadaInimigo.draw(tela)



def DesenhaMeteoro(Posicao):
    DrawMeteoro = pygame.sprite.Group()
    
    meteoro = pygame.sprite.Sprite(DrawMeteoro)
    meteoro.image = pygame.image.load('data/Habilidades/Meteoro.png')
    meteoro.image = pygame.transform.scale(meteoro.image, [100, 130])
    meteoro.rect = pygame.Rect(PosicoesXAtkMeteoro[Posicao], PosicoesYAtkMeteoro[Posicao], 100, 130)
    #tela.blit(meteoro,(PosicoesXAtkMeteoro[Posicao],PosicoesYAtkMeteoro[Posicao]))

    DrawMeteoro.draw(tela)

def DesenhaMeteoroInimigo(Posicao):
    DrawMeteoroInimigo = pygame.sprite.Group()
    
    meteoroini = pygame.sprite.Sprite(DrawMeteoroInimigo)
    meteoroini.image = pygame.image.load('data/Habilidades/Meteoro.png')
    meteoroini.image = meteoroini.image.copy()
    meteoroini.image = pygame.transform.flip(meteoroini.image, True, False)
    meteoroini.image = pygame.transform.scale(meteoroini.image, [100, 130])
    meteoroini.rect = pygame.Rect(PosicoesXAtkMeteoroInimigo[Posicao], PosicoesYAtkMeteoroInimigo[Posicao], 100, 130)
    #tela.blit(meteoro,(PosicoesXAtkMeteoro[Posicao],PosicoesYAtkMeteoro[Posicao]))

    DrawMeteoroInimigo.draw(tela)
    

'''def DesenhaInimigoSaindo(Posicao, Onda, InimigoAtual, Acao):
    #Acao / 0 = Parado , 1 = Primeiro Salto , 2 = caindo , 3 = no ar
    DrawInimigoSaindo = pygame.sprite.Group()
    inimigoSaindo = pygame.sprite.Sprite(DrawInimigoSaindo)
    
    #inimigoSaindo.image = pygame.image.load('data/Personagens/perso0.png')
    
    if Acao == 1:
        inimigoSaindo.image = pygame.image.load('data/InimigosPulando/ini'+str(Onda)+str(InimigoAtual)+'.png')
    elif Acao == 2:
        inimigoSaindo.image = pygame.image.load('data/InimigosCaindo/ini'+str(Onda)+str(InimigoAtual)+'.png')

    inimigoSaindo.image = pygame.transform.scale(inimigoSaindo.image, [230, 200])
    inimigoSaindo.image = inimigoSaindo.image.copy()
    inimigoSaindo.image = pygame.transform.flip(inimigoSaindo.image, True, False)
    
    inimigoSaindo.rect = pygame.Rect(PosicoesXInimigoSaindo[Posicao], PosicoesYInimigoSaindo[Posicao], 100, 100)
    DrawInimigoSaindo.draw(tela)'''



    
    
#Classe Botão
class ButtonTelaInicio():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
    def draw(self,tela,outline=None):
        if outline:
            pygame.draw.rect(tela, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(tela, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('algerian', 40)
            text = font.render(self.text, 1, (0,0,0))
            tela.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


    
class ButtonSelecao():
    def __init__(self, color, chapeu, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.chapeu = chapeu
        self.text = text
        
    def draw(self,tela,outline=None):
        if outline:
            pygame.draw.rect(tela, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(tela, self.color, (self.x,self.y,self.width,self.height),0)

        
        if self.chapeu == 1:
            img = pygame.image.load('data/Personagens/chp0.png')
            img = pygame.transform.scale(img, (50, 50))
            tela.blit(img,(self.x,self.y))
        elif self.chapeu == 2:
            img = pygame.image.load('data/Personagens/chp1.png')
            img = pygame.transform.scale(img, (50, 50))
            tela.blit(img,(self.x,self.y))
        elif self.chapeu == 3:
            img = pygame.image.load('data/Personagens/chp2.png')
            img = pygame.transform.scale(img, (50, 50))
            tela.blit(img,(self.x,self.y))
        elif self.chapeu == 4:
            img = pygame.image.load('data/Personagens/chp3.png')
            img = pygame.transform.scale(img, (50, 50))
            tela.blit(img,(self.x,self.y))
        elif self.chapeu == 5:
            img = pygame.image.load('data/Personagens/chp4.png')
            img = pygame.transform.scale(img, (50, 50))
            tela.blit(img,(self.x,self.y))

        
        if self.text != '':
            font = pygame.font.SysFont('algerian', 40)
            text = font.render(self.text, 1, (0,0,0))
            tela.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


class ButtonHabilidades():
    def __init__(self, habilidade, x,y,width,height, text=''):
        '''img = pygame.image.load('data/Personagens/ChapeuViking.png')
        img = pygame.transform.scale(img, [50, 50])'''
        self.x = x
        self.y = y
        self.color = (196,163,110)
        #self.color = (169,118,79)
        self.width = width
        self.height = height
        self.text = text
        self.habilidade = habilidade
        #self.color.set_alpha(128)


    def draw(self, tela,outline=None):
     
        if outline:
            pygame.draw.rect(tela, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(tela, self.color, (self.x,self.y,self.width,self.height),0)

        #if self.habilidade == 1:
            #img = pygame.image.load('data/Espadas/EspadaMadeira.png')
        if self.habilidade == 5:
            img = Pocoes[0]
        elif self.habilidade == 6:
            img = Pocoes[1]
        elif self.habilidade == 7:
            img = Pocoes[2]
        else:
            img = AtaquesSkills[self.habilidade]
            
        #if self.habilidade == 9:
            #img = pygame.image.load('data/Pause.png')
            

        if self.habilidade == 5 or self.habilidade == 6 or self.habilidade == 7:
            img = pygame.transform.scale(img, [50, 35])
            tela.blit(img,(self.x,self.y + 10))
        else:
            img = pygame.transform.scale(img, [50, 50])
            tela.blit(img,(self.x,self.y))
        
        if self.text != '':
            font = pygame.font.SysFont('algerian', 40)
            text = font.render(self.text, 1, (0,0,0))
            tela.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    
        
    def isOver(self, pos):

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

'''class ButtonPause():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
    def draw(self,tela,outline=None):
        if outline:
            pygame.draw.rect(tela, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(tela, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('algerian', 40)
            text = font.render(self.text, 1, (0,0,0))
            tela.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False'''


#Desenvolvimento
while True:
    #Evento para fechar o programa
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    if TelaInicial:
        
        tela.blit(Background, (0, 0))
        
        #Draw
        ButtonA = ButtonTelaInicio((195, 150, 85), 350, 550, 150, 50, 'Iniciar')
        ButtonB = ButtonTelaInicio((195, 150, 85), 650, 550, 200, 50, 'Ranking')
    
        ButtonA.draw(tela, (0, 0, 0))
        ButtonB.draw(tela, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if ButtonA.isOver(pos):   
                TelaInicial = False
                TelaPersonagem = True
            #elif ButtonB.isOver(pos):
                 #print ('clicou no Ranking')
                
        pygame.display.update()


    if TelaPersonagem:
        tela.blit(fundo, (0, 0))
        tela.blit(fundo, (0, 0))
        ButtonC = ButtonSelecao((85, 153, 255), (6), 710, 150, 50, 50, ' ')
        ButtonD = ButtonSelecao((175, 233, 175), (6), 770, 150, 50, 50, ' ')
        ButtonE = ButtonSelecao((195, 150, 85), (6), 710, 600, 100, 50, 'Ok')
        ButtonF = ButtonSelecao((195, 150, 85), (6), 830, 600, 160, 50, 'Voltar')
        ButtonG = ButtonSelecao((255, 230, 128), (6), 830, 150, 50, 50, ' ')
        ButtonH = ButtonSelecao((255, 128, 128), (6), 890, 150, 50, 50, ' ')
        ButtonI = ButtonSelecao((196,163,110), (1), 710, 220, 50, 50, '')
        ButtonJ = ButtonSelecao((196,163,110), (2), 770, 220, 50, 50, '')
        ButtonK = ButtonSelecao((196,163,110), (3), 830, 220, 50, 50, '')
        ButtonL = ButtonSelecao((196,163,110), (4), 890, 220, 50, 50, '')
        ButtonM = ButtonSelecao((196,163,110), (5), 950, 220, 50, 50, '')
        ButtonN = ButtonSelecao((179, 128, 255), (6), 950, 150, 50, 50, ' ')
        
        
        
        ButtonC.draw(tela, (0, 0, 0))
        ButtonD.draw(tela, (0, 0, 0))
        ButtonE.draw(tela, (0, 0, 0))
        ButtonF.draw(tela, (0, 0, 0))
        ButtonG.draw(tela, (0, 0, 0))
        ButtonH.draw(tela, (0, 0, 0))
        ButtonI.draw(tela, (0, 0, 0))
        ButtonJ.draw(tela, (0, 0, 0))
        ButtonK.draw(tela, (0, 0, 0))
        ButtonL.draw(tela, (0, 0, 0))
        ButtonM.draw(tela, (0, 0, 0))
        ButtonN.draw(tela, (0, 0, 0))
        #drawGroup.draw(tela)

        #if Selecionou == True:
            #DesenhaPosicao1(Selecionado)
        #else:
        DesenhaPosicao(Selecionado, 0, 0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ButtonE.isOver(pos):
                
                TelaPersonagem = False
                PersonagemEscolhido = Selecionado
                Inicializacao = True
            elif ButtonF.isOver(pos):
                 
                 TelaPersonagem = False
                 Inicializacao = True     
            elif ButtonC.isOver(pos):
                
                #Greenw = False
                #Blue = True
                Selecionou = True
                Selecionado = 0
            elif ButtonD.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Selecionado = 1
            elif ButtonG.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Selecionado = 2
            elif ButtonH.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Selecionado = 3
            elif ButtonN.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Selecionado = 4
            elif ButtonI.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Chapeu = 0
            elif ButtonJ.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Chapeu = 1
            elif ButtonK.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Chapeu = 2
            elif ButtonL.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Chapeu = 3
            elif ButtonM.isOver(pos):
                
                #Blue = False
                #Greenw = True
                Selecionou = True
                Chapeu = 4
            
        pygame.display.update()



    if Inicializacao:
        tela.blit(fundo, (0, 0))
        #tela.fill((155,0,0))
        ButtonE = ButtonSelecao((195, 150, 85), (6), 710, 600, 100, 50, 'Ok')
        ButtonF = ButtonSelecao((195, 150, 85), (6), 830, 600, 160, 50, 'Voltar')

        ButtonE.draw(tela, (0, 0, 0))
        ButtonF.draw(tela, (0, 0, 0))
                                
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    BTexto = True
                elif ButtonE.isOver(pos):
                     
                     Inicializacao = False
                     TelaLuta1 = True
                elif ButtonF.isOver(pos):
                    
                    Inicializacao = False
                    TelaPersonagem = True     

            if event.type == pygame.KEYDOWN:
                if BTexto == True:
                    if event.key == pygame.K_BACKSPACE:
                       user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        pygame.draw.rect(tela, color,input_rect,2)
    
        text_surface = base_font_carta.render(user_text, True,(255,255,255))
        text_surface2 = base_font_titulo.render(user_titulo, True,(0,0,0))
        text_surface3 = base_font_carta.render(user_linha1, True,(0,0,0))
        text_surface4 = base_font_carta.render(user_linha2, True,(0,0,0))
        text_surface5 = base_font_carta.render(user_linha3, True,(0,0,0))
        tela.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        tela.blit(text_surface2,(400, 100))
        tela.blit(text_surface3,(60, 300))
        tela.blit(text_surface4,(370, 330))
        tela.blit(text_surface5,(350, 450))

        input_rect.w = max(100,text_surface.get_width() + 10)

        if BTexto:
            color = TextoSelecionado
        else:
            color = TextoNaoSelecionado


        pygame.display.update()


    if TelaLuta1:


            tela.blit(Arena, (0, 0))        
            
            PocaoVida = 5
            PocaoMana = 6

            if RecargaPocaoVida != 3:
                PocaoVida = 7
            if RecargaPocaoMana != 3:
                PocaoMana = 7
            
            
            ButtonO = ButtonHabilidades((0),440, 650, 50, 50, '')
            ButtonP = ButtonHabilidades((1),493, 650, 50, 50, '')
            ButtonQ = ButtonHabilidades((2),546, 650, 50, 50, '')
            ButtonR = ButtonHabilidades((3),599, 650, 50, 50, '')
            ButtonS = ButtonHabilidades((4),652, 650, 50, 50, '')
            ButtonT = ButtonHabilidades((PocaoVida),719, 650, 50, 50, '')
            ButtonU = ButtonHabilidades((PocaoMana),772, 650, 50, 50, '')
            ButtonO.draw(tela, (0, 0, 0))
            ButtonP.draw(tela, (0, 0, 0))
            ButtonQ.draw(tela, (0, 0, 0))
            ButtonR.draw(tela, (0, 0, 0))
            ButtonS.draw(tela, (0, 0, 0))
            ButtonT.draw(tela, (0, 0, 0))
            ButtonU.draw(tela, (0, 0, 0))

            #ButtonV = ButtonPause((9),1100, 100, 50, 50, '')
            #ButtonV.draw(tela, (0, 0, 0))

            if AtkInimigo == 1:
                #print('Entrou primeiro If')
                EstadoEvasaoInimigo = True

            #Ataque Personagem
            #EstadoEvasao = False
            #EstadoSonolento = False            
            if PosicaoAtualPrincipal == 0:
                if PosicaoEspadaSonifero == 0:
                    DesenhaPosicaoEspada(OndaAtual, 0, InimigoAtual)
                if EstadoSonolento == True:
                    DesenhaPosicao(PersonagemEscolhido, 0, 5)
                else:
                    DesenhaPosicao(PersonagemEscolhido, 0, 0)
                #if PosicaoEspadaSoniferoInimigo == 0:
                    #DesenhaPosicaoEspadaInimigo(OndaAtual, 0, InimigoAtual)
                if AtkInimigo == 3 :
                    AtkSoniferoInimigo = True
                    PosicaoEspadaSoniferoInimigo = 1
                    PersoDormindo = 1
                    pygame.time.delay(100)
                    #AtkSonoInimigo = True

            if PersoEnfraquecido == True:
                TxtEnfraquecido = fonteEnfraquecido.render(('ENFRAQUECIDO'), 1, (0,0,0))
                tela.blit(TxtEnfraquecido,(310,350))

            if InimigoEnfraquecido == 1:
                TxtEnfraquecido = fonteEnfraquecido.render(('ENFRAQUECIDO'), 1, (0,0,0))
                tela.blit(TxtEnfraquecido,(880,300))

            if PersoDormindo == True:
                TxtSono = fonteEvasao.render(('ZZZ'), 1, (0,0,0))
                tela.blit(TxtSono,(330,330))
                
            if InimigoDormindo == 1:
                TxtSono = fonteEvasao.render(('ZZZ'), 1, (0,0,0))
                tela.blit(TxtSono,(880,300))

            if PosicaoAtualInimigo == 0:
                if PosicaoEspadaSoniferoInimigo == 0:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 0, InimigoAtual)
                if InimigoDormindo == 1:
                    DesenhaPosicaoInimigo(0, OndaAtual, InimigoAtual, 5)
                else:
                    DesenhaPosicaoInimigo(0, OndaAtual, InimigoAtual, 0)

            if AtkBasico == True:
                if PosicaoAtualPrincipal == 1:
                    DesenhaPosicaoEspada(OndaAtual, 1, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 1, 1)
                    #if AtkSonoInimigo == True:
                        #PosicaoEspadaSoniferoInimigo = 1
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        if VidaAtualInimigo <= 0:
                            InimigoMorreu = True
                            AtkInimigo = 8
                        PosicaoAtualPrincipal -= 1
                        if AtkInimigo == 0:
                            PosicaoAtualInimigo = 1
                        elif AtkInimigo == 2:
                            PosicaoAtualMeteoro = 1
                        if AtkInimigo == 4:
                            SituacaoAtk = 1
                            AtkInimigo = 0
                            PosicaoAtualInimigo = 1
                            SituacaoAtk = 1
                        SituacaoAtk = 1
                        AtkBasico = False
                        if InimigoEnfraquecido == 1:
                            InimigoEnfraquecido -= 1
                        if InimigoDormindo == 1:
                            InimigoDormindo -= 1
                        pygame.time.wait(15)
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 2:
                    DesenhaPosicaoEspada(OndaAtual, 2, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 2, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 3:
                    DesenhaPosicaoEspada(OndaAtual, 3, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 3, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 4:
                    DesenhaPosicaoEspada(OndaAtual, 4, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 4, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 5:
                    DesenhaPosicaoEspada(OndaAtual, 5, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 5, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 6:
                    DesenhaPosicaoEspada(OndaAtual, 6, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 6, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 7:
                    DesenhaPosicaoEspada(OndaAtual, 7, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 7, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 8:
                    DesenhaPosicaoEspada(OndaAtual, 8, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 8, 2)
                    if SituacaoAtk == 1:
                        PosicaoAtualPrincipal += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualPrincipal -= 1
                        if EsperarEvacao == True:
                            EsperarEvacao = False
                            PosicaoAtualInimigo = 0
                            RealizandoAcao = False
                            AtkInimigo = 8
                            EstadoEvasaoInimigo = False
                            pygame.time.wait(300)
                        pygame.time.wait(300)
                    pygame.time.wait(15)
                elif PosicaoAtualPrincipal == 9:
                    DesenhaPosicaoEspada(OndaAtual, 8, InimigoAtual)
                    DesenhaPosicao(PersonagemEscolhido, 8, 2)
                    PosicaoAtualPrincipal = 8
                    SituacaoAtk = 2
                    if EstadoEvasaoInimigo == False:
                        if AtkSupremo == True:
                            VidaAtualInimigo = VidaAtualInimigo - ((VidaMaxInimigo / 100) * (60))
                            AtkSupremo = False
                        else:
                            VidaAtualInimigo = VidaAtualInimigo - ((VidaMaxInimigo / 100) * (10 * (OndaAtual + 1) * (InimigoAtual +1)))
                            #VidaAtualInimigo = VidaAtualInimigo - ((VidaMaxInimigo / 100) * (10 * (OndaAtual + 1) * (InimigoAtual +1)))
                        DesenhaPosicaoInimigo(0, OndaAtual, InimigoAtual, 4)
                    else:
                        TxtEvasao = fonteEvasao.render(('MISS'), 1, (0,0,0))
                        tela.blit(TxtEvasao,(880,350))
                        ManaAtualInimigo = ManaAtualInimigo - ManaEvasao
                        if ManaAtualInimigo < 0:
                            ManaAtualInimigo = 0
                        if ManaAtualInimigo <= ManaMaxInimigo - 2:
                            ManaAtualInimigo = ManaAtualInimigo + 2
                        EsperarEvacao = True
                        AtkSupremo = False
                    if PersoEnfraquecido == True:
                        PersoEnfraquecido = False
                    
                    pygame.time.wait(10)

                    
            '''if PosicaoAtualMeteoro == 0:
                DesenhaMeteoro(0)'''
                
            #print(AtkInimigo)
            if AtkMeteoro == False:
                DesenhaMeteoro(0)
            
            if AtkMeteoro == True:
                if PosicaoAtualMeteoro == 1:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 2:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 3:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 4:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 5:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 6:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 7:
                    DesenhaMeteoro(PosicaoAtualMeteoro)
                    #AtkMeteoro = False
                    if EstadoEvasaoInimigo == False: 
                        VidaAtualInimigo = VidaAtualInimigo - ((VidaMaxInimigo * 0.10))
                        DanoReduzido = 1
                        InimigoEnfraquecido = 1
                        #PosicaoAtualMeteoro = 0
                    else:
                        TxtEvasao = fonteEvasao.render(('MISS'), 1, (0,0,0))
                        tela.blit(TxtEvasao,(880,350))
                        ManaAtualInimigo = ManaAtualInimigo - ManaEvasao
                        if ManaAtualInimigo < 0:
                            ManaAtualInimigo = 0
                        if ManaAtualInimigo <= ManaMaxInimigo - 2:
                            ManaAtualInimigo = ManaAtualInimigo + 2
                        EsperarEvacao = True
                        #PosicaoAtualMeteoro += 1
                        EstadoEvasaoInimigo = False
                    if AtkInimigo == 0:
                            PosicaoAtualInimigo = 1
                            SituacaoAtk = 1
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 8:
                    if VidaAtualInimigo <= 0:
                            AtkInimigo = 8
                    if EsperarEvacao == True:
                        PosicaoAtualInimigo = 0
                        PosicaoAtualMeteoro = 0
                        EstadoEvasaoInimigo = False
                        EsperarEvacao = False
                        AtkMeteoro = False
                        AtkInimigo = 8
                        RealizandoAcao = False
                        pygame.time.wait(300)
                    else:
                        AtkMeteoro = False
                    if AtkInimigo == 2:
                        AtkMeteoro = True
                        PosicaoAtualMeteoro = 1
                    elif AtkInimigo == 3:
                        PosicaoEspadaSoniferoInimigo = 1
            

            '''if PersoEnfraquecido == True:
                TxtEnfraquecido = fonteEnfraquecido.render(('ENFRAQUECIDO'), 1, (0,0,0))
                tela.blit(TxtEnfraquecido,(310,350))
                PersoEnfraquecido = False'''
              
            if AtkSonifero == True:
                if PosicaoEspadaSonifero == 1:
                    DesenhaPosicaoEspada(OndaAtual, 0, InimigoAtual, 'Sonifero')
                    PosicaoEspadaSonifero += 1
                    pygame.time.wait(15)
                elif PosicaoEspadaSonifero == 2:
                    DesenhaPosicaoEspada(OndaAtual, 0, InimigoAtual)
                    PosicaoEspadaSonifero = 0
                    AtkInimigo = 8
                    AtkSonifero = False
                    EstadoSonolentoInimigo = True
                    RealizandoAcao = False
                    InimigoDormindo = 1
                    pygame.time.wait(300)
                

            '''if PosicaoAtualInimigo == 0:
                if PosicaoEspadaSoniferoInimigo == 0:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 0, InimigoAtual)
                if InimigoDormindo == 1:
                    DesenhaPosicaoInimigo(0, OndaAtual, InimigoAtual, 5)
                else:
                    DesenhaPosicaoInimigo(0, OndaAtual, InimigoAtual, 0)'''


            
                
                
            
            if EstadoSonolento == True:
                #TurnoAtual += 1
                AtkInimigo = 0
                SituacaoAtk = 1
                PosicaoAtualInimigo = 1
                #tela.blit(TxtEvasao,(880,350))
                RealizandoAcao = True
                EstadoSonolento = False
                DesenhaPosicao(PersonagemEscolhido, 0, 5)
                pygame.time.wait(500)
                
            

            if EstadoSonolentoInimigo == True:
                if RecargaPocaoVida == 0:
                    RecargaPocaoVida = 3
                elif RecargaPocaoVida < 3:
                    RecargaPocaoVida -= 1
                if RecargaPocaoMana == 0:
                    RecargaPocaoMana = 3
                elif RecargaPocaoMana < 3:
                    RecargaPocaoMana -= 1
                            
                if RecargaPocaoVidaIni == 0:
                    RecargaPocaoVidaIni = 3
                elif RecargaPocaoVidaIni < 3:
                    RecargaPocaoVidaIni -= 1
                if RecargaPocaoManaIni == 0:
                    RecargaPocaoManaIni = 3
                elif RecargaPocaoManaIni < 3:
                    RecargaPocaoManaIni -= 1
                EstadoSonolentoInimigo = False
                RealizandoAcao = False
                pygame.time.delay(500)

            
            if AtkInimigo == 8 and VidaAtualInimigo <= 0:
                if InimigoMorreu == True:
                    InimigoAtual += 1
                    if InimigoAtual == 4 and OndaAtual == 0:
                        OndaAtual = 1
                        InimigoAtual = 0
                    elif InimigoAtual == 4 and OndaAtual == 1:
                        OndaAtual = 2
                        InimigoAtual = 0
                    elif InimigoAtual == 4 and OndaAtual == 2:
                        InimigoAtual = 0
                        OndaAtual = 3
                    elif InimigoAtual == 4 and OndaAtual == 3:
                        InimigoAtual = 0
                        OndaAtual = 4
                    elif InimigoAtual == 4 and OndaAtual == 4:
                        InimigoAtual = 0
                        OndaAtual = 5
                    if OndaAtual == 0:
                        VidaMaxInimigo = (VidaMaxInimigos1 + (50 * InimigoAtual))
                        VidaAtualInimigo = VidaMaxInimigo
                    elif OndaAtual == 1:
                        VidaMaxInimigo = (VidaMaxInimigos2 + (50 * InimigoAtual))
                        VidaAtualInimigo = VidaMaxInimigo
                    if OndaAtual == 2:
                        VidaMaxInimigo = (VidaMaxInimigos3 + (50 * InimigoAtual))
                        VidaAtualInimigo = VidaMaxInimigo
                    if OndaAtual == 3:
                        VidaMaxInimigo = (VidaMaxInimigos4 + (50 * InimigoAtual))
                        VidaAtualInimigo = VidaMaxInimigo
                    if OndaAtual == 4:
                        VidaMaxInimigo = (VidaMaxInimigos5 + (50 * InimigoAtual))
                        VidaAtualInimigo = VidaMaxInimigo
                    
                    VidaMaxPersonagem += 50
                    VidaAtualPersonagem = VidaMaxPersonagem

                    ManaAtualPersonagem = 100
                    ManaAtualInimigo = 100
                    
                    InimigoMorreu = False
                    RealizandoAcao = False

            
                    
            if AtkInimigo == 0:
                #Ataque inimigo
                '''if PosicaoAtualInimigo == 0:
                    DesenhaPosicaoEspadaInimigo(EspadaAtual, 0)
                    DesenhaPosicaoInimigo(0)'''
                if PosicaoAtualInimigo == 1:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 1, InimigoAtual, 1)
                    DesenhaPosicaoInimigo(1, OndaAtual, InimigoAtual, 1)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                        SituacaoAtk = 0
                        TurnoAtual += 1
                        AtkInimigo = 8
                        if RecargaPocaoVida == 0:
                            RecargaPocaoVida = 3
                        elif RecargaPocaoVida < 3:
                            RecargaPocaoVida -= 1
                        if RecargaPocaoMana == 0:
                            RecargaPocaoMana = 3
                        elif RecargaPocaoMana < 3:
                            RecargaPocaoMana -= 1
                            
                        if RecargaPocaoVidaIni == 0:
                            RecargaPocaoVidaIni = 3
                        elif RecargaPocaoVidaIni < 3:
                            RecargaPocaoVidaIni -= 1
                        if RecargaPocaoManaIni == 0:
                            RecargaPocaoManaIni = 3
                        elif RecargaPocaoManaIni < 3:
                            RecargaPocaoManaIni -= 1
                        
                        RealizandoAcao = False
                        #VidaAtualPersonagem = VidaAtualPersonagem - ((VidaMaxPersonagem / 100) * (11 + InimigoAtual))
                    pygame.time.wait(25)
                    #pygame.time.delay(1)
                elif PosicaoAtualInimigo == 2:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 2, InimigoAtual)
                    DesenhaPosicaoInimigo(2, OndaAtual, InimigoAtual, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                    pygame.time.wait(15)
                    #pygame.time.delay(1)
                elif PosicaoAtualInimigo == 3:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 3, InimigoAtual)
                    DesenhaPosicaoInimigo(3, OndaAtual, InimigoAtual, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                    pygame.time.wait(15)
                    #pygame.time.delay(1)
                elif PosicaoAtualInimigo == 4:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 4, InimigoAtual)
                    DesenhaPosicaoInimigo(4, OndaAtual, InimigoAtual, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualInimigo == 5:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 5, InimigoAtual)
                    DesenhaPosicaoInimigo(5, OndaAtual, InimigoAtual, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualInimigo == 6:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 6, InimigoAtual)
                    DesenhaPosicaoInimigo(6, OndaAtual, InimigoAtual, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualInimigo == 7:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 7, InimigoAtual)
                    DesenhaPosicaoInimigo(7, OndaAtual, InimigoAtual, 3)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                    pygame.time.wait(15)
                elif PosicaoAtualInimigo == 8:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 8, InimigoAtual)
                    DesenhaPosicaoInimigo(8, OndaAtual, InimigoAtual, 2)
                    if SituacaoAtk == 1:
                        PosicaoAtualInimigo += 1
                    elif SituacaoAtk == 2:
                        PosicaoAtualInimigo -= 1
                        if EsperarEvacao == True:
                            pygame.time.wait(300)
                            EsperarEvacao = False
                            EstadoEvasao = True
                        pygame.time.wait(300)
                    pygame.time.wait(15)
                elif PosicaoAtualInimigo == 9:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 8, InimigoAtual)
                    DesenhaPosicaoInimigo(8, OndaAtual, InimigoAtual, 2)
                    PosicaoAtualInimigo = 8
                    SituacaoAtk = 2
                    if EstadoEvasao == False:
                        if AtkInimigo == 4 or AtkSupremoInimigo == True:
                            VidaAtualPersonagem = VidaAtualPersonagem - ((VidaMaxPersonagem / 100) * (60))
                            ManaAtualInimigo = ManaAtualInimigo - 60
                            AtkSupremoInimigo = False
                        else:
                            VidaAtualPersonagem = VidaAtualPersonagem - ((VidaMaxPersonagem / 100) * (11 * (OndaAtual + 1) * (InimigoAtual +1)))
                        DesenhaPosicao(PersonagemEscolhido, 0, 4)
                    else:
                        TxtEvasao = fonteEvasao.render(('MISS'), 1, (0,0,0))
                        tela.blit(TxtEvasao,(330,370))
                        EsperarEvacao = True
                        AtkSupremoInimigo = False
                    if PersoDormindo == True:
                        PersoDormindo = False
                    pygame.time.wait(10)
                    
            if AtkInimigo == 2:
                if PosicaoAtualMeteoro == 1:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 2:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 3:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 4:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 5:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 6:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 7:
                    DesenhaMeteoroInimigo(PosicaoAtualMeteoro)
                    #AtkMeteoro = False
                    if EstadoEvasao == False: 
                        VidaAtualPersonagem = VidaAtualPersonagem - ((VidaMaxPersonagem * 0.10))
                        DanoReduzido = 1
                        #PosicaoAtualMeteoro = 0
                    else:
                        TxtEvasao = fonteEvasao.render(('MISS'), 1, (0,0,0))
                        tela.blit(TxtEvasao,(330,370))
                        EsperarEvacao = True
                        #PosicaoAtualMeteoro += 1
                        EstadoEvasaoInimigo = False
                    if AtkInimigo == 0:
                            PosicaoAtualInimigo = 1
                            SituacaoAtk = 1
                    PosicaoAtualMeteoro += 1
                    pygame.time.wait(15)
                elif PosicaoAtualMeteoro == 8:
                    if EsperarEvacao == True:
                        PosicaoAtualInimigo = 0
                        PosicaoAtualMeteoro = 0
                        EstadoEvasaoInimigo = False
                        EsperarEvacao = False
                        AtkMeteoro = False
                        AtkInimigo = 8
                        pygame.time.wait(300)
                    else:
                        pygame.time.wait(300)
                        PersoEnfraquecido = True
                        AtkMeteoro = False
                    RealizandoAcao = False
                    ManaAtualInimigo = ManaAtualInimigo - ManaMeteoro
                    
                    
                    if ManaAtualInimigo < 0:
                        ManaAtualInimigo = 0
                    if ManaAtualInimigo <= ManaMaxInimigo - 2:
                        ManaAtualInimigo = ManaAtualInimigo + 2
                    if RecargaPocaoVida == 0:
                        RecargaPocaoVida = 3
                    elif RecargaPocaoVida < 3:
                        RecargaPocaoVida -= 1
                    if RecargaPocaoMana == 0:
                        RecargaPocaoMana = 3
                    elif RecargaPocaoMana < 3:
                        RecargaPocaoMana -= 1    
                    if RecargaPocaoVidaIni == 0:
                        RecargaPocaoVidaIni = 3
                    elif RecargaPocaoVidaIni < 3:
                        RecargaPocaoVidaIni -= 1
                    if RecargaPocaoManaIni == 0:
                        RecargaPocaoManaIni = 3
                    elif RecargaPocaoManaIni < 3:
                        RecargaPocaoManaIni -= 1
                    PosicaoAtualMeteoro = 0
                    pygame.time.wait(10)


            #if InimigoEnfraquecido == 0:
                #InimigoEnfraquecido = 2
            #print(InimigoEnfraquecido)
            '''if InimigoEnfraquecido == 1:
                TxtEnfraquecido = fonteEnfraquecido.render(('ENFRAQUECIDO'), 1, (0,0,0))
                tela.blit(TxtEnfraquecido,(880,300))'''
            if AtkSoniferoInimigo == True:
                if PosicaoEspadaSoniferoInimigo == 1:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 0, InimigoAtual, 'Sonifero')
                    PosicaoEspadaSoniferoInimigo += 1
                    AtkInimigo = 8
                    pygame.time.wait(150)
                elif PosicaoEspadaSoniferoInimigo == 2:
                    DesenhaPosicaoEspadaInimigo(OndaAtual, 0, InimigoAtual)
                    PosicaoEspadaSoniferoInimigo = 0
                    AtkSonifero = False
                    AtkSoniferoInimigo = False
                    RealizandoAcao = True
                    EstadoSonolento = True
                    AtkInimigo = 8
                    pygame.time.wait(300)

            '''if AtkSonifero == True:
                if PosicaoEspadaSonifero == 1:
                    DesenhaPosicaoEspada(OndaAtual, 0, InimigoAtual, 'Sonifero')
                    PosicaoEspadaSonifero += 1
                    pygame.time.wait(15)
                elif PosicaoEspadaSonifero == 2:
                    DesenhaPosicaoEspada(OndaAtual, 0, InimigoAtual)
                    PosicaoEspadaSonifero = 0
                    AtkSonifero = False
                    EstadoSonolentoInimigo = True
                    RealizandoAcao = False
                    pygame.time.wait(500)'''

            
            if AtkInimigo == 6:
                VidaAtualInimigo = VidaAtualInimigo + VidaMaxInimigo * 0.3
                if VidaAtualInimigo > VidaMaxInimigo:
                    VidaAtualInimigo = VidaMaxInimigo
                if RecargaPocaoVida == 0:
                    RecargaPocaoVida = 3
                elif RecargaPocaoVida < 3:
                    RecargaPocaoVida -= 1
                if RecargaPocaoMana == 0:
                    RecargaPocaoMana = 3
                elif RecargaPocaoMana < 3:
                    RecargaPocaoMana -= 1    
                if RecargaPocaoVidaIni == 0:
                    RecargaPocaoVidaIni = 3
                elif RecargaPocaoVidaIni < 3:
                    RecargaPocaoVidaIni -= 1
                if RecargaPocaoManaIni == 0:
                    RecargaPocaoManaIni = 3
                elif RecargaPocaoManaIni < 3:
                    RecargaPocaoManaIni -= 1
                AtkInimigo = 8
                RealizandoAcao = False
                EstadoSonolento = False
                
            if AtkInimigo == 7:
                ManaAtualInimigo = ManaAtualInimigo + ManaMaxInimigo * 0.3
                if ManaAtualInimigo > ManaMaxInimigo:
                    ManaAtualInimigo = ManaMaxInimigo
                if RecargaPocaoVida == 0:
                    RecargaPocaoVida = 3
                elif RecargaPocaoVida < 3:
                    RecargaPocaoVida -= 1
                if RecargaPocaoMana == 0:
                    RecargaPocaoMana = 3
                elif RecargaPocaoMana < 3:
                    RecargaPocaoMana -= 1    
                if RecargaPocaoVidaIni == 0:
                    RecargaPocaoVidaIni = 3
                elif RecargaPocaoVidaIni < 3:
                    RecargaPocaoVidaIni -= 1
                if RecargaPocaoManaIni == 0:
                    RecargaPocaoManaIni = 3
                elif RecargaPocaoManaIni < 3:
                    RecargaPocaoManaIni -= 1
                AtkInimigo = 8 
                RealizandoAcao = False
                EstadoSonolento = False



            #drawGroup.draw(tela)

            #Vida
            #Descobrindo % da vida
            if VidaAtualPersonagem <= 0:
                VidaAtualPersonagem = 0
            else:                
                ValorPreencherVidaPersonagem = VidaAtualPersonagem / VidaMaxPersonagem
                ValorPreencherVidaPersonagem = int(120 * ValorPreencherVidaPersonagem)
                pygame.draw.rect(tela, (186,0,1), (302, 652, int(ValorPreencherVidaPersonagem), 18))
            
            pygame.draw.rect(tela, (0,0,0), (300, 650, 122, 20), 2)
            TxtVida = fonteVidaMana.render(str(int(VidaAtualPersonagem)), 1, (0,0,0))
            tela.blit(TxtVida,(350,653))
            
            #Mana
            #Descobrindo % da mana
            if ManaAtualPersonagem <= 0:
                ManaAtualPersonagem = 0
            else:    
                ValorPreencherManaPersonagem = ManaAtualPersonagem / ManaMaxPersonagem
                ValorPreencherManaPersonagem = int(120 * ValorPreencherManaPersonagem)
                pygame.draw.rect(tela, (12,12,250), (302, 682, int(ValorPreencherManaPersonagem), 18))
           
            pygame.draw.rect(tela, (0,0,0), (300, 680, 122, 20), 2)
            TxtMana = fonteVidaMana.render(str(int(ManaAtualPersonagem)), 1, (0,0,0))
            tela.blit(TxtMana,(350,683))





            #Vida
            #Descobrindo % da vida do Ininmigo
            if VidaAtualInimigo <= 0:
                VidaAtualInimigo = 0
                #pygame.time.delay(300)
            else:
                ValorPreencherVidaInimigo = VidaAtualInimigo / VidaMaxInimigo
                #ValorPreencherVidaInimigo = VidaAtualInimigo / VidaMaxInimigos1
                ValorPreencherVidaInimigo = int(120 * ValorPreencherVidaInimigo)
                pygame.draw.rect(tela, (186,0,1), (842, 652, int(ValorPreencherVidaInimigo), 18))
            
            pygame.draw.rect(tela, (0,0,0), (840, 650, 122, 20), 2)
            TxtVidaInimigo = fonteVidaMana.render(str(int(VidaAtualInimigo)), 1, (0,0,0))
            tela.blit(TxtVidaInimigo,(890,653))
            
            #Mana
            #Descobrindo % da mana do Inimigo
            if ManaAtualInimigo <= 0:
                ManAtualInimigo = 0
            else:                
                ValorPreencherManaInimigo = ManaAtualInimigo / ManaMaxInimigo
                ValorPreencherManaInimigo = int(120 * ValorPreencherManaInimigo)
                pygame.draw.rect(tela, (12,12,250), (842, 682, int(ValorPreencherManaInimigo), 18))
           
            pygame.draw.rect(tela, (0,0,0), (840, 680, 122, 20), 2)
            TxtManaInimigo = fonteVidaMana.render(str(int(ManaAtualInimigo)), 1, (0,0,0))
            tela.blit(TxtManaInimigo,(890,683))

            if VidaAtualPersonagem == 0:
                tela.blit(ImgMorreu,(0, 0))
            

            '''if VidaAtualInimigo == 0:
                InimigoMorreu = True
                pygame.time.delay(500)
            if InimigoMorreu == True:
                MovimentoSaindo = 0
                pygame.time.wait(300)
                if MovimentoSaindo == 0:
                    DesenhaInimigoSaindo(0, OndaAtual, InimigoAtual, 1)
                    MovimentoSaindo += 1
                    pygame.time.wait(100)
                if MovimentoSaindo == 2:
                    DesenhaInimigoSaindo(1, OndaAtual, InimigoAtual, 2)
                    MovimentoSaindo += 1
                    pygame.time.wait(100)
                if MovimentoSaindo == 3:
                    DesenhaInimigoSaindo(2, OndaAtual, InimigoAtual, 1)
                    MovimentoSaindo += 1
                    pygame.time.wait(100)
                if MovimentoSaindo == 4:
                    DesenhaInimigoSaindo(3, OndaAtual, InimigoAtual, 2)
                    MovimentoSaindo == 0
                    pygame.time.wait(100)
                InimigoMorreu = False'''

                
            

            '''if VidaAtualInimigo == 0:
                if EspadaAtual == 0:
                    EspadaAtual = 0
                else:
                    EspadaAtual += 1
                InimigoAtual += 1
                EspadaAtualInimigo += 1
                pygame.time.wait(300)'''

            
            PersonagemEscolhido = Selecionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ButtonO.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and AtkBasico == False:
                        EstadoEvasao = False
                        AtkInimigo = randint(0, 7)
                        
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            RecargaPocaoManaIni = 2
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 5
                        if AtkInimigo == 1 and ManaAtualInimigo < ManaEvasao:
                            AtkInimigo = 0
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        '''if AtkInimigo == 2:
                            PosicaoAtualMeteoro = 1'''
                        if AtkInimigo == 6 and ManaAtualInimigo > 30:
                            RecargaPocaoManaIni = 3
                            AtkInimigo = 0
                        if AtkInimigo == 5 and VidaAtualInimigo > (VidaMaxInimigo * 0.15):
                            RecargaPocaoVidaIni = 3
                            AtkInimigo = 0
                            
                        if AtkInimigo == 4:
                            AtkInimigo = 0
                            AtkSupremoInimigo = True
                        #if AtkInimigo == 3:
                            #PosicaoEspadaSoniferoInimigo = 1
                        PosicaoAtualPrincipal = 1
                        SituacaoAtk = 1
                        AtkBasico = True
                        RealizandoAcao = True
                        
                        if ManaAtualPersonagem <= ManaMaxPersonagem - 2:
                            ManaAtualPersonagem = ManaAtualPersonagem + 2
                        
                if ButtonP.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and ManaAtualPersonagem >= ManaEvasao:
                        EstadoEvasao = True
                        AtkInimigo = randint(5, 5)
                        if AtkInimigo == 0 or AtkInimigo == 1:
                            SituacaoAtk = 1
                            PosicaoAtualInimigo = 1
                            AtkInimigo = 0
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 5
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        if AtkInimigo == 3:
                            PosicaoEspadaSoniferoInimigo = 1
                        if AtkInimigo == 6 and ManaAtualInimigo > 30:
                            AtkInimigo = 0
                            RecargaPocaoManaIni = 3
                        if AtkInimigo == 5 and VidaAtualInimigo > (VidaMaxInimigo * 0.15):
                            AtkInimigo = 0
                            RecargaPocaoVidaIni = 3
                        if AtkInimigo == 4:
                            AtkSupremoInimigo = True
                        if AtkInimigo == 0:
                            AtkInimigo = 0
                            PosicaoAtualInimigo = 1
                            SituacaoAtk = 1

                        if AtkInimigo == 4:
                            AtkInimigo = 0
                            AtkSupremoInimigo = True
                        #if AtkInimigo == 2:
                            #PosicaoAtualMeteoro = 1
                        ManaAtualPersonagem = ManaAtualPersonagem - ManaEvasao
                        if ManaAtualPersonagem < 0:
                            ManaAtualPersonagem = 0
                        if ManaAtualPersonagem <= ManaMaxPersonagem - 2:
                            ManaAtualPersonagem = ManaAtualPersonagem + 2
                        RealizandoAcao = True
                        
                        
                if ButtonQ.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and AtkMeteoro == False and ManaAtualPersonagem >= ManaMeteoro:
                        AtkInimigo = randint(0, 7)
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            RecargaPocaoManaIni = 2
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 5
                        if AtkInimigo == 1 and ManaAtualInimigo < ManaEvasao:
                            AtkInimigo = 0
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        if AtkInimigo == 6 and ManaAtualInimigo > 30:
                            AtkInimigo = 0
                            RecargaPocaoManaIni = 3
                        if AtkInimigo == 5 and VidaAtualInimigo > (VidaMaxInimigo * 0.15):
                            AtkInimigo = 0
                            RecargaPocaoVidaIni = 3

                        if AtkInimigo == 4:
                            AtkInimigo = 0
                            AtkSupremoInimigo = True
                        if AtkInimigo == 3:
                            PosicaoEspadaSoniferoInimigo = 1
                        ManaAtualPersonagem = ManaAtualPersonagem - ManaMeteoro
                        if ManaAtualPersonagem < 0:
                            ManaAtualPersonagem = 0
                        if ManaAtualPersonagem <= ManaMaxPersonagem - 2:
                            ManaAtualPersonagem = ManaAtualPersonagem + 2
                        
                        AtkMeteoro = True
                        PosicaoAtualMeteoro = 1
                        
                        RealizandoAcao = True
                        SituacaoAtk = 1
                        
                        
                if ButtonR.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and AtkSonifero == False and ManaAtualPersonagem >= ManaSonifero:
                        AtkInimigo = randint(0, 7)
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            RecargaPocaoManaIni = 2
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 5
                        if AtkInimigo == 1 and ManaAtualInimigo < ManaEvasao:
                            AtkInimigo = 0
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        if AtkInimigo == 3:
                            AtkInimigo = 0
                        if AtkInimigo == 3:
                            PosicaoEspadaSoniferoInimigo = 1
                        if AtkInimigo == 6 and ManaAtualInimigo > 30:
                            AtkInimigo = 0
                            RecargaPocaoManaIni = 3
                        if AtkInimigo == 5 and VidaAtualInimigo > (VidaMaxInimigo * 0.15):
                            AtkInimigo = 0
                            RecargaPocaoVidaIni = 3

                        if AtkInimigo == 4:
                            AtkInimigo = 0
                            AtkSupremoInimigo = True
                        RealizandoAcao = True
                        AtkSonifero = True
                        PosicaoEspadaSonifero = 1
                        #if AtkInimigo == 2:
                            #PosicaoAtualMeteoro = 1
                        ManaAtualPersonagem = ManaAtualPersonagem - ManaSonifero
                        if ManaAtualPersonagem < 0:
                            ManaAtualPersonagem = 0
                        if ManaAtualPersonagem <= ManaMaxPersonagem - 2:
                            ManaAtualPersonagem = ManaAtualPersonagem + 2
                        
                        
                        
                if ButtonS.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and ManaAtualPersonagem >= ManaAtkSupremo:
                        
                        AtkInimigo = randint(0, 7)
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            RecargaPocaoManaIni = 2
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 5
                        if AtkInimigo == 1 and ManaAtualInimigo < ManaEvasao:
                            AtkInimigo = 0
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        if AtkInimigo == 3:
                            PosicaoEspadaSoniferoInimigo = 1
                        PosicaoAtualPrincipal = 1
                        '''if AtkInimigo == 2:
                            PosicaoAtualMeteoro = 1'''
                        if AtkInimigo == 6 and ManaAtualInimigo > 30:
                            AtkInimigo = 0
                            RecargaPocaoManaIni = 3
                        if AtkInimigo == 5 and VidaAtualInimigo > (VidaMaxInimigo * 0.15):
                            AtkInimigo = 0
                            RecargaPocaoVidaIni = 3

                        if AtkInimigo == 4:
                            AtkInimigo = 0
                            AtkSupremoInimigo = True
                        SituacaoAtk = 1
                        AtkBasico = True
                        AtkSupremo = True
                        RealizandoAcao = True
                        #print(AtkInimigo)
                        ManaAtualPersonagem = ManaAtualPersonagem - ManaAtkSupremo
                        if ManaAtualPersonagem < 0:
                            ManaAtualPersonagem = 0
                        if ManaAtualPersonagem <= ManaMaxPersonagem - 2:
                            ManaAtualPersonagem = ManaAtualPersonagem + 2

                        
                if ButtonT.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and RecargaPocaoVida == 3:
                        RecargaPocaoVida = 2
                        AtkInimigo = randint(0, 7)
                        if AtkInimigo == 0 or AtkInimigo == 1:
                            SituacaoAtk = 1
                            PosicaoAtualInimigo = 1
                            AtkInimigo = 0
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            RecargaPocaoManaIni = 2
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            RecargaPocaoVidaIni = 2
                            AtkInimigo = 5
                        '''if AtkInimigo == 1 and ManaAtualInimigo < ManaEvasao:
                            AtkInimigo = 0
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        if AtkInimigo == 3:
                            PosicaoEspadaSoniferoInimigo = 1'''
                        AtkInimigo = 0
                        PosicaoAtualInimigo = 1
                        SituacaoAtk = 1
                        EstadoEvasao = False
                        VidaAtualPersonagem = VidaAtualPersonagem + VidaMaxPersonagem * 0.3
                        if VidaAtualPersonagem > VidaMaxPersonagem:
                            VidaAtualPersonagem = VidaMaxPersonagem 
                        

                        
                if ButtonU.isOver(pos):
                    if PosicaoAtualPrincipal == 0 and RealizandoAcao == False and EstadoSonolento == False and RecargaPocaoMana == 3:
                        RecargaPocaoMana = 2
                        AtkInimigo = randint(0, 7)
                        if AtkInimigo == 0 or AtkInimigo == 1:
                            SituacaoAtk = 1
                            PosicaoAtualInimigo = 1
                            AtkInimigo = 0
                        if ManaAtualInimigo < 20 and RecargaPocaoManaIni == 3:
                            AtkInimigo = 6
                        if VidaAtualInimigo < (VidaMaxInimigo * 0.10) and RecargaPocaoVidaIni == 3:
                            AtkInimigo = 5
                        '''if AtkInimigo == 1 and ManaAtualInimigo < ManaEvasao:
                            AtkInimigo = 0
                        if AtkInimigo == 2 and ManaAtualInimigo < ManaMeteoro:
                            AtkInimigo = 0
                        elif AtkInimigo == 3 and ManaAtualInimigo < ManaSonifero:
                            AtkInimigo = 0
                        elif AtkInimigo == 4 and ManaAtualInimigo < ManaAtkSupremo:
                            AtkInimigo = 0
                        if AtkInimigo == 3:
                            PosicaoEspadaSoniferoInimigo = 1'''
                        EstadoEvasao = False
                        AtkInimigo = 0
                        PosicaoAtualInimigo = 1
                        SituacaoAtk = 1
                        ManaAtualPersonagem = ManaAtualPersonagem + ManaMaxPersonagem * 0.3
                        if ManaAtualPersonagem > ManaMaxPersonagem:
                            ManaAtualPersonagem = ManaMaxPersonagem 
                        
                #if ButtonO.isOver(pos):

                    
            pygame.display.update()
            
       #if TelaPause:
           #tela.blit(Background, (0, 0))

    '''if TelaMorreu:
        #if VidaAtualPersonagem == 0:
                #TxtMorreu = fonteMorreu.render(('VOCÊ MORREU'), 1, (0,0,0))
                    #tela.blit(TxtMorreu,(largura / 2, altura / 2))
        tela.blit(ImgMorreu, (0, 0))
        RealizandoAcao = True
        ButtonW = ButtonSelecao((195, 150, 85), (6), 710, 600, 100, 50, 'Recomeçar')
        ButtonW.draw(tela, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ButtonW.isOver(pos):
                TelaLuta1 = True
                PersonagemEscolhido = Selecionado
                TelaMorreu = False
                OndaAtual = 0
                InimigoAtual = 0
                VidaAtualPersonagem = 100
                VidaAtualInimigo = 100
                VidaMaxPersonagem = 100
                VidaMaxInimigo = 100
                ManaAtualPersonagem = 100
                ManaAtualInimigo = 100
                ManaMaxPersonagem = 100
                ManaMaxPersonagem = 100
                RealizandoAcao = False'''
           
           
                       
        

    #pygame.display.update()
    pygame.time.delay(delay)

               
              


               
    
