def pedir_lista_entera(mensaje, cantidad_esperada):
    while True:
        entrada = input(mensaje)
        lista = list(map(int, entrada.strip().split()))
        if len(lista) != cantidad_esperada:
            print(f"Error: Se esperaban {cantidad_esperada} números, pero se recibieron {len(lista)}. Intenta nuevamente.")
        else:
            return lista 
  