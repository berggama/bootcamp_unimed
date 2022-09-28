def posicao():
  while True:
      try:
        letra = input().upper()
    
        if (type(letra)== 'int') or (len(letra)!=1):
          raise ValueError('Valor fora do intervalo permitido')
        else:
          break
      except ValueError as error:
            print(error)

  alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
  print(alfabeto.find(letra)+1)