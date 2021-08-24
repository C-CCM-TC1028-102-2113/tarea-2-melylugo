def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    indice=peso/(altura**2)

    if peso>0 and altura>0:  
        while indice>20: 
            if 20<=indice<25:
                print ("NORMAL")
            if 25<=indice<30:
                print ("SOBREPESO") 
            if 30<=indice<40:
                print ("OBESIDAD")
            if indice>40:
                print ("OBESIDAD MORBIDA")
        print ("PESO BAJO")
    else: 
        print ("Revisa tus datos, alguno de ellos es erróneo.")

    pass
if __name__=='__main__':
    main()
