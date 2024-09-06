livros = []

qnt = int(input("quantos livros vc quer adicionar?"))
for i in range (qnt):
    livroadd = input("insira seu livro: ")
    livros.append(livroadd)
for i in livros:
    print(i)
