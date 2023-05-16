nota = int(input("Ingrese su nota: "))

# si la nota es entre 1 y menor que 3, perdio la materia
# si la nota es entre 3 y  menor a 4, es aceptable
# pero si la no es entre 4 a 5, es excelente

if nota >=1 and nota < 3:
    print("Perdio la nota")
elif nota >= 3 and nota < 4:
    print("Su nota es aceptable")
elif nota >= 4 and nota <= 5:
    print("Su nota es excelente")
else:
    print("Nota invalida")

    

    
    
# AND = TRUE , SI AMBOS SON IGUALES
# OR = TRUE, SI ALGUNA DE LAS CONDICIONES SE CUMPLE

#if edad >= 18 and nombre!="maria":
#    print("Si puede ingresar, ya que es mayor de edad  y no es maria")
#else:
#    print("Usted es MENOR de edad o te llamas maria, no puede ingresar")
