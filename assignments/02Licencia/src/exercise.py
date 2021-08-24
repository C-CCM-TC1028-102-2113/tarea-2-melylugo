
def main():
    #Escribe tu código debajo de esta línea
    edad=int(input("Ingresa tu edad: "))

    if edad>=18:
        id=str(input("¿Tienes identificación oficial? (s/n): "))
        if id=="s":
            print ("Trámite de licencia concedido")
        else: 
            print ("Respuesta incorrecta")
    else: 
       print ("No cumples requisitos")
    pass


if __name__ == '__main__':
    main()
