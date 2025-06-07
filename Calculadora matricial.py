def soma_geral(M1,M2):
    """Soma duas matrizes de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for l in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            MF[i][j] = M1[i][j] + M2[i][j]
    return MF
def soma_diagonal(M1,M2):
    """Soma duas matrizes quadradas diagonais de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        MF[i][i] = M1[i][i] + M2[i][i]
    return MF
def soma_triangular_superior(M1,M2):
    """Soma duas matrizes quadradas triangulares superiores de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(i, len(M1)):
            print(M1[i][j], M2[i][j])
            MF[i][j] = M1[i][j] + M2[i][j]
    return MF
def soma_triangular_inferior(M1,M2):
    """Soma duas matrizes quadradas triangulares inferiores de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(0, i + 1):
            MF[i][j] = M1[i][j] + M2[i][j]
    return MF

def subtracao_geral(M1,M2):
    """Subtrai duas matrizes de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            MF[i][j] = M1[i][j] - M2[i][j]
    return MF
def subtracao_diagonal(M1,M2):
    """Subtrai duas matrizes quadradas diagonais de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        MF[i][i] = M1[i][i] - M2[i][i]
    return MF
def subtracao_triangular_superior(M1,M2):   
    """Subtrai duas matrizes quadradas triangulares superiores de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(i, len(M1)):
            MF[i][j] = M1[i][j] - M2[i][j]
    return MF
def subtracao_triangular_inferior(M1,M2):
    """Subtrai duas matrizes quadradas triangulares inferiores de mesmo tamanho."""
    MF = [[0 for col in range(len(M1[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(0, i + 1):
            MF[i][j] = M1[i][j] - M2[i][j]
    return MF

def multiplicacao_por_escalar_geral(M, valor):
    """Multiplica uma matriz por um escalar."""
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j]*= valor
    return M
def multiplicacao_por_escalar_diagonal(M,valor):
    """Multiplica uma matriz diagonal por um escalar."""
    for i in range(len(M)):
        M[i][i]*=valor
    return M
def multiplicacao_por_escalar_triangular_superior(M,valor):
    """Multiplica uma matriz triangular superior por um escalar."""
    for i in range(len(M)):
        for j in range(i, len(M)):
            M[i][j]*=valor
    return M
def multiplicacao_por_escalar_triangular_inferior(M,valor):
    """Multiplica uma matriz triangular inferior por um escalar."""
    for i in range(len(M)):
        for j in range(0, i + 1):
            M[i][j]*=valor
    return M

def multiplicacao_matricial_geral(M1, M2):
    """Multiplica duas matrizes de mesmo tamanho."""
    MF = [[0 for col in range(len(M2[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                MF[i][j] += M1[i][k] * M2[k][j]
    return MF
def multiplicacao_matricial_diagonal(M1, M2):
    """Multiplica duas matrizes quadradas diagonais de mesmo tamanho."""
    MF = [[0 for col in range(len(M2[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        MF[i][i] = M1[i][i] * M2[i][i]
    return MF
def multiplicacao_matricial_triangular_superior(M1, M2):
    """Multiplica duas matrizes quadradas triangulares superiores de mesmo tamanho."""
    MF = [[0 for col in range(len(M2[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(i, len(M2[0])):
            for k in range(i, len(M2)):
                MF[i][j] += M1[i][k] * M2[k][j]
    return MF
def multiplicacao_matricial_triangular_inferior(M1, M2):
    """Multiplica duas matrizes quadradas triangulares inferiores de mesmo tamanho."""
    MF = [[0 for col in range(len(M2[0]))] for lin in range(len(M1))]
    for i in range(len(M1)):
        for j in range(0, i + 1):
            for k in range(0, i + 1):
                MF[i][j] += M1[i][k] * M2[k][j]
    return MF

def transposta(M):
    """Calcula a matriz transposta."""
    MT = [[0 for _ in range(len(M))] for _ in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            MT[j][i] = M[i][j]
    return MT
def traço(M):
    """Calcula o traço de uma matriz quadrada."""
    return sum(M[i][i] for i in range(len(M)))
def determinante_triangular(M):
    """Calcula o determinante de uma matriz triangular."""
    det = 1
    for i in range(len(M)):
        det *= M[i][i]
    return det


A = [[4, 7, 3],
     [9, 0, 2],
     [7, 8, 8]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
C = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
D = [[1, 2, 3],
     [0, 5, 2],
     [0, 0, 5]]
E = [[1, 0, 0],
     [2, 1, 0],
     [3, 4, 1]]
