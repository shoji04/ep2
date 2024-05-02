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

print (" Batalha naval \n Iniciando o Jogo! \n  ")

print (" Computador esta alocando os navios de guerra do pais ... \n computador ja esta em posicao de batalha ! \n ")

print (" 1 : Brasil \n     1 cruzador \n     2 torpedeiro \n     1 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 2 : franca \n     3 cruzador \n     1 torpedeiro \n     1 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 3 : australia \n     1 cruzador \n     3 torpedeiro \n     1 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 4 : russia \n     1 cruzador \n     1 torpedeiro \n     2 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
print (" 5 : japao \n     2 cruzador \n     1 torpedeiro \n     2 destroyer \n     1 couracado \n     1 porta-avioes \n  ") 
        
escolha_pais = int(input('Qual o numero da sua frota ?'))