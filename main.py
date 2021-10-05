from matplotlib import pyplot


def contagem(dicio, key):
    if key not in dicio.keys():
        dicio[key] = 1
    else:
        dicio[key] += 1


def questao(numero, texto):
    print()
    print(f'------------- QUESTÃO {numero} -------------')
    print(texto)
    print()


def saida(dicio, total=False):
    tot = 0
    for k, v in dicio.items():
        print(f'{k}: {v}')
        tot += v
    if total:
        print(f'TOTAL: {tot}')


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
        if IES == 'Instituto Federal de Educação Ciência e Tecnologia' and reg == 'Nordeste':
            contagem(dados4, uf)

        # Questão 5
        cat_adm = dados[20]
        contagem(dados5, cat_adm)

# Gráfico 1
pyplot.figure(1)
pyplot.title('Instituições de Ensino Superior')
pyplot.pie(dados1.values(), labels=dados1.keys())
pyplot.savefig('questao-1.png')

# Gráfico 2
pyplot.figure(2)
pyplot.title('Quantidade de Faculdades por Região')
pyplot.plot(dados2.keys(), dados2.values(), marker='o')
pyplot.savefig('questao-2.png')

# Gráfico 3
pyplot.figure(3)
pyplot.title('Localização das Universidades Brasileiras')
pyplot.pie(dados3.values(), labels=dados3.keys())
pyplot.savefig('questao-3.png')

# Gráfico 4
pyplot.figure(4)
pyplot.title('Quantidade de Institutos Federais da Região Nordeste')
pyplot.bar(dados4.keys(), dados4.values())
pyplot.savefig('questao-4.png')

# Gráfico 5
pyplot.figure(5)
pyplot.title('Categoria Administrativa das Instituições de Ensino Superior')
pyplot.pie(dados5.values(), labels=dados5.keys())
pyplot.savefig('questao-5.png')

# Saída de dados
questao(1, 'Quais são os tipos de instituições de ensino superior e '
           'quantas de cada existem no Brasil?')
saida(dados1)

questao(2, 'Qual a região que possui mais faculdades e qual a que possui menos?')
saida(dados2)

questao(3, 'Quantas universidades existem na capital? E no interior?')
saida(dados3)

questao(4, 'Quantos institutos federais possui a região nordeste, divididos por estado?')
saida(dados4, total=True)

questao(5, 'Qual o total de instituições de ensino superior, divididas '
           'por categoria administrativa?')
saida(dados5, total=True)
