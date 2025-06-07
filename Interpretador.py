def check_matriz(M):
    """Testa se a matriz é válida e classifica seu tipo."""
    lin = len(M)
    col = len(M[0])
    cont_ts = 0
    cont_ti = 0
    cont_d = 0
    for i in range(lin):
        if len(M[i]) != col:
            raise ValueError("Todas as linhas devem ter o mesmo número de colunas.")
        for j in range(col):
            if not isinstance(M[i][j], (int, float)):
                raise TypeError("Todos os elementos da matriz devem ser números.")
            if M[i][j] != 0:
                if i < j:
                    cont_ts += 1
                elif i > j:
                    cont_ti += 1
                else:
                    cont_d += 1
    if lin == col:
        if cont_ts == 0 and cont_ti == 0:
            return "Matriz diagonal"
        elif cont_ts == 0:
            return "Matriz triangular superior"
        elif cont_ti == 0:
            return "Matriz triangular inferior"
        else:
            return "Matriz quadrada"
    return "Matriz retangular"

def show_matriz(M):
    """Exibe a matriz de forma formatada."""
    for linha in M:
        print(linha)
    print()    

def read_matriz(path):
    """
    Lê uma matriz de um arquivo.
    O arquivo deve conter uma matriz onde cada linha é uma lista de números separados por espaços.
    """
    with open(path, 'r') as file:
        M = []
        for line in file:
            # col = list(map(float, line.strip().split()))
            col = [int(x) if x.isdigit() or (x[0] == '-' and x[1:].isdigit()) else float(x) for x in line.strip().split()]
            M.append(col)
    return M
    
def write_matriz(M, path = "C:\\Users\\berne\\UFRJ\\Estrutura de Dados\\Matrizes.txt"):
    """
    Escreve uma matriz em um arquivo.
    Cada linha da matriz será escrita em uma linha do arquivo, com os números separados por espaços.
    """
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        i = content.count('Matriz')
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f"Matriz {i}\n")
        for linha in M:
            file.write(' '.join(map(str, linha)) + '\n')
        file.write('\n')

def delete_matriz(index, path = "C:\\Users\\berne\\UFRJ\\Estrutura de Dados\\Matrizes.txt"):
    """
    Deleta uma matriz de um arquivo.
    O índice da matriz a ser deletada é passado como parâmetro.
    """
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        i = content.count('Matriz')
    if index < 0 or index >= i:
        raise IndexError("Índice da matriz inválido.")
    with open(path, 'w', encoding='utf-8') as file:
        lines = content.splitlines()
        new_content = []
        matriz_del = False
        for line in lines:
            if line.startswith(f"Matriz {index}"):
               matriz_del = True
            elif line.startswith("Matriz") and matriz_del:
                matriz_del = False
            if not matriz_del:
                new_content.append(line)
        i = 0
        for index,matriz in enumerate(new_content):
            if "Matriz" in matriz:
                matriz_new = matriz[:7] + str(i)
                new_content[index] = matriz_new
                i+=1
        file.write('\n'.join(new_content) + '\n')

A = [[1, 0, 0],
     [2, 3, 0], 
     [4, 5, 6]]

# write_matriz(A)
# c = read_matriz("C:\\Users\\berne\\UFRJ\\Estrutura de Dados\\test1.txt")
# show_matriz(c)
# write_matriz(c)
# delete_matriz(0)