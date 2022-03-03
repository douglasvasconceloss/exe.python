
somaidade=0
mediaidade=0
idademulher=0
maioridadehomem=0
nomevelho=''
for p in range(1,5):
  nome=str(input('digite o nome da {} pessoa: '.format(p)))
  idade=int(input('digite a idade da {} pessoa: '.format(p)))
  sexo=str(input('digite o sexo da {} pessoa: [M/F] '.format(p)))
  print('--------------------------------------')
  somaidade += idade
  if idade<20 and sexo=='F':
    idademulher += 1
  if p==1 and sexo in 'Mm':
    maioridadehomem=idade
    nomevelho=nome
  if sexo in 'Mm' and maioridadehomem<idade:
    maioridadehomem=idade
    nomevelho=nome

mediaidade=somaidade/4
print('a idade media é de {}'.format(mediaidade))
print('{} mulhere(s) tiveram idade abaixo de 20 anos'.format(idademulher))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
