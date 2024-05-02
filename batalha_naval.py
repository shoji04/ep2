import random
from constantes import CONFIGURACAO, PAISES, ALFABETO, CORES

#Cria matriz quadrada de espaços
def cria_mapa(N):
    
    matriz = []
   
    for i in range(N):
        
        linha = [' '] * N
        matriz.append(linha)
    
    return matriz

#Navio pode ser alocado na posição?
def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    
    if linha < 0 or coluna < 0 or linha >= len(mapa) or coluna >= len(mapa[0]):
        return False
    
    if orientacao not in ['v', 'h']:
        return False

    if orientacao == 'v':
        if linha + blocos > len(mapa):
            return False
        for i in range(linha, linha + blocos):
            if mapa[i][coluna] != ' ':
                return False
    else:  
        if coluna + blocos > len(mapa[0]):
            return False
        for j in range(coluna, coluna + blocos):
            if mapa[linha][j] != ' ':
                return False

    return True 

#Alocando navios para o computador
def aloca_navios(mapa, blocos):
    n = len(mapa)
    for tamanho in blocos:
        while True:
            linha = random.randint(0, n - 1)
            coluna = random.randint(0, n - 1)
            orientacao = random.choice(['h', 'v'])

            if orientacao == 'h':
                if coluna + tamanho <= n:
                    valido = True
                    for i in range(tamanho):
                        if mapa[linha][coluna + i] != ' ':
                            valido = False
                            break
                    if valido:
                        for i in range(tamanho):
                            mapa[linha][coluna + i] = 'N'
                        break
            else:
                if linha + tamanho <= n:
                    valido = True
                    for i in range(tamanho):
                        if mapa[linha + i][coluna] != ' ':
                            valido = False
                            break
                    if valido:
                        for i in range(tamanho):
                            mapa[linha + i][coluna] = 'N'
                        break
    return mapa

#Verifica se acabou os 'N's da matriz
def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True

paises = ['','Brasil','França','Austrália','Rússia','Japão']
pais_comp = random.choice(['Brasil','França','Austrália','Rússia','Japão'])

print (" Batalha naval \n Iniciando o Jogo! \n  ")

print (f' Computador esta alocando os navios de guerra do pais {pais_comp}... \n computador ja esta em posicao de batalha ! \n ')

print (" 1 : Brasil \n     1 cruzador \n     2 torpedeiro \n     1 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 2 : franca \n     3 cruzador \n     1 torpedeiro \n     1 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 3 : australia \n     1 cruzador \n     3 torpedeiro \n     1 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 4 : russia \n     1 cruzador \n     1 torpedeiro \n     2 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 5 : japao \n     2 cruzador \n     1 torpedeiro \n     2 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
        
escolha_pais = int(input('Qual o numero da sua frota ? \n '))

if escolha_pais == 1:
    print (" Voce escolheu a nacao Brasil \n Agora é sua vez de alocar seus navios de guerra! \n")
elif escolha_pais == 2: 
    print (" Voce escolheu a nacao Franca \n Agora é sua vez de alocar seus navios de guerra! \n")
elif escolha_pais == 3: 
    print (" Voce escolheu a nacao Australia \n Agora é sua vez de alocar seus navios de guerra! \n")
elif escolha_pais == 4: 
    print (" Voce escolheu a nacao Russia \n Agora é sua vez de alocar seus navios de guerra! \n")
elif escolha_pais == 5: 
        print (" Voce escolheu a nacao Japao \n Agora é sua vez de alocar seus navios de guerra! \n")

cor_navio = '\u001b[32m'  # verde
cor_agua = '\u001b[36m'   # ciano
cor_atingido = '\u001b[31m'  # vermelho
reset = '\u001b[0m'

navio_ = '▓'

navio_colorido = cor_navio + navio_ + reset

navio_atingido = cor_atingido + navio_ + reset

agua_final = cor_agua + navio_ + reset


def mostraMapa(mat1, mat2,comp,jog):
        print(f'     COMPUTADOR - {comp}                 JOGADOR - {jog}     \n')
        print('   A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')
        for linha in range(10):
            print(f'{linha+1:2d}', end='')
            for coluna in range(10):
                print(f' {mat1[linha][coluna]} ', end='')
            print(f'{linha+1:2d}', end='')
            print(f'  {linha+1:2d}', end='')
            for coluna in range(10):
                print(f' {mat2[linha][coluna]} ', end='')
            print(f'{linha+1:2d}', end='')
            print(' ')
        print('   A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')

escolha_paispais = int(escolha_pais)
escolhido = paises[escolha_pais]

maps = cria_mapa(10)
new_map = cria_mapa(10)
mapa_comp = cria_mapa(10)

mostraMapa(maps,maps,pais_comp,escolhido)
print('\n')

print (f'alocar: ')
print (f'proximos: ')

inf_letra = input('Informe a letra:')