import matplotlib.pyplot as plt

# lê o arquivo .pgm
def readPgm(name):
    file = open(name, 'r')
    assert file.readline() == 'P2\n'
    line = file.readline()
    while line[0] == '#':
        line = file.readline()
    
    (width, height) = [int(i) for i in line.split()]
    #print (width, height)
    depth = int(file.readline())
    assert depth <= 255
    #print(depth)

    img = []
    row = []
    j = 0
    for line in file:
        values = line.split()
        for val in values:
            row.append(int(val))
            j += 1
            if j >= width:
                img.append(row)
                j = 0
                row = []
    file.close()
    return img

# cria uma matriz para alocar o valores de uma imagem
def imgAlloc(nl, nc):
    img = []
    for i in range(nl):
        lin = []
        for j in range(nc):
            lin.append(0)
        img.append(lin)
    return img

# leitura da imagem .pgm
img = readPgm('img.pgm')

# número de linhas e colunas antes de redimensionar
nl = len(img)
nc = len(img[0])

# novos valores para número de linhas e colunas da matriz
novo_num_lins = 85
novo_num_cols = 128

# alocando nova espaço para a imagem redimensionada
imagem = imgAlloc(novo_num_lins, novo_num_cols)

# razão entre a dimensão antiga e a nova
razao_lins = nl // novo_num_lins
razao_cols = nc // novo_num_cols

# x e y sao variáveis que auxiliam a redimensionar a imagem, elas são incrementados pelo valor da razão calculada acima
x = 0
for i in range(novo_num_lins):
    x += razao_lins
    y = 0
    for j in range(novo_num_cols):
        imagem[i][j] = img[x][y]
        y += razao_cols

# visualização de como ficou a imagem redimensionada
#plt.imshow(imagem, cmap='gray')
#plt.show()

# alocando uma matriz para a imagem de saída
saida = imgAlloc(novo_num_lins, novo_num_cols)

# caracteres a serem usados
str = "@$#*%o!=+;:~=,. "

# tamanho da string passada
tam_str = len(str)

# montando a arte ASCII
for i in range(novo_num_lins):
    for j in range(novo_num_cols):

        # escolhe o carácter a ser usado pelo índice
        # o código só funciona se a string ter caracteres "mais escuros" no incio e "mais claros" no final
        indice = imagem[i][j] // tam_str

        # escreve o carácter na saída
        saida[i][j] = str[indice]

# escreve a saída em um arquivo de texto para que seja possível visualizar o resultado
# também é realizada a união de cada carácter de cada linha da matriz seguido de uma quebra de linha
with open('result.txt', 'w') as resultado:
    for linha in saida:
        resultado.write(''.join(linha))
        resultado.write('\n')
