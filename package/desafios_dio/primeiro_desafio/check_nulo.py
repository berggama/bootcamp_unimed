def check_nulo():
    while True:
      try:
        salario = float(input()) 
    
        if (salario==0):
          raise ValueError('Valor fora do intervalo permitido')
        else:
          break
      except ValueError as error:
            print(error)