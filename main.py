nome  =str(input('seu nome?'))

suanota1 = float(input('suanota1:'))
suanota2 = float(input('suanota2:'))
suanota3 = float(input('suanota3'))
media = float(input('sua media:'))

media: float =(suanota1 + suanota2 + suanota3) /7
print ('media')

faltas = int(inout('Quantas Faltas?'))

if media < 7:
   print('Nome, Repreovado!')
elif faltas > 3:
  print('Nome, Reprovado por faltas')
elif media >= 7:
  print('Nome, Foi Aprovado!')