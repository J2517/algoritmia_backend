from logica.buscador import encontrar_menor_mayor
from logica.validador import pedir_lista_entera
      
def main():
    n = int(input("Ingrese el tamaño de la lista: "))
    lista = pedir_lista_entera("Ingrese la lista de números enteros separados por espacios: ", n)
        
    q = int(input("Ingrese el número de consultas: "))

    consultas = pedir_lista_entera("Ingrese la lista de consultas separadas por espacios: ", q)
        
    for consulta in consultas:
        menor, mayor = encontrar_menor_mayor(lista, consulta)
        print(f"{menor} {mayor}")

if __name__ == "__main__":
    main()