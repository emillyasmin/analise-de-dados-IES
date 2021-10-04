def contagem(dicio, key):
    if key not in dicio.keys():
        dicio[key] = 1
    else:
        dicio[key] += 1


def agrupamento(dicio, key, value):
    if key not in dicio.keys():
        dicio[key] = list()
    if value not in dicio[key]:
        dicio[key].append(value)


def questao(numero, texto):
    print()
    print(f'------------- QUESTÃO {numero} -------------')
    print(texto)
    print()


def saida(dicio, lista=False):
    for k, v in dicio.items():
        if lista:
            for i in v:
                print(f'{k}: {i}')
        else:
            print(f'{k}: {v}')


# Cada dicionário responde uma questão
dados1 = dict()
dados2 = dict()
dados3 = dict()
dados4 = dict()
dados5 = dict()

# Abrindo o arquivo
with open('cadastroIES-2011.csv', 'r') as arq:
    for line in arq.readlines():
        dados = line.split(';')

        # Questão 1
        IES = dados[16]
        contagem(dados1, IES)

        # Questão 2
        reg = dados[6]
        if IES == 'Faculdade':
            contagem(dados2, reg)

        # Questão 3
        loc = dados[14]
        if IES == 'Universidade':
            contagem(dados3, loc)

        # Questão 4
        uf = dados[9]
        nome_IES = dados[2].title()
        if IES == 'Instituto Federal de Educação Ciência e Tecnologia' and reg == 'Nordeste':
            agrupamento(dados4, uf, nome_IES)

        # Questão 5
        pag = dados[33]
        if uf == 'RN':
            agrupamento(dados5, nome_IES, pag)
            if pag[0:3] != 'www':
                dados5[nome_IES] = ['não possui']

# Saída de dados
questao(1, 'Quais são os tipos de instituições de ensino superior e '
           'quantas de cada existem no Brasil?')
saida(dados1)

questao(2, 'Qual a região que possui mais faculdades e qual a que possui menos?')
saida(dados2)

questao(3, 'Quantas universidades existem na capital? E no interior?')
saida(dados3)

questao(4, 'Quais são os institutos federais da região nordeste, divididos por estado?')
saida(dados4, lista=True)

questao(5, 'Quais as páginas eletrônicas de cada instituição do Rio Grande do Norte?')
saida(dados5, lista=True)
