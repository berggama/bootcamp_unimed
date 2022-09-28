def lim_inferior(minimo):
    while True:
      try:
        salario = float(input()) 
    
        if (salario<=maximo):
          raise ValueError('Valor fora do intervalo permitido')
        else:
          break
      except ValueError as error:
            print(error)