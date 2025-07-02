def encontrar_menor_mayor(lista, consulta):
    menor = 'X'
    mayor = 'X'
    
    for num in lista:
        if num < consulta:
            menor = num
        elif num > consulta and mayor == 'X':
            mayor = num
            break
    
    return menor, mayor