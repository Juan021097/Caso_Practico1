#Llamado de las listas de otro documento
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches


usuarios= []#Lista para agregar usuario desde la terminal
clave = []#Lista para agregar clave desde la terminal
print("***********************************")
print("*    Hola espero estes bien       *")
print("*  Porfavor ingresa tu Usuario:   *")
print("***********************************")
login=input(' ')#pedir usuario
usuarios.append(login)#agregar nombre a lista de usuario
print("***********************************")
print("*  Ahora ingresa tu contraseña    *")
print("***********************************")
password=input(' ')#pedir password
clave.append(password)#agregar nombre a lista de clave

os.system("cls")
if login == 'Juan Carlos' and password == '1234':#Comparar si el usuario y clave son correctos
    print("******************************************************")
    print("*           ¡Bienvenidos a Lifestore                 *")
    print("*           en donde podras visualizar:              *")
    print("*                                                    *")
    print("* [1] Productos más vendidos y productos rezagados   *")
    print("* [2] Productos por reseña en el servicio            *")
    print("* [3]Total de ingresos y ventas promedio mensual,    *")
    print("*    total anual y meses con mas ventas al año       *")
    print("*                                                    *")
    print("*     Porfavor digita una opcion entre 1 y3:         *")
    print("******************************************************")
#Menu principal
    opcion = input( )

    if opcion == '1':
        print("**********************************************")
        print("*         Que deseas consultar               *")
        print("*[1.1]Lista de productos con mayores ventas  *")
        print("*[1.2]Lista de productos con mayor busqueda  *")
        print("*[1.3]Lista de productos con menores ventas  *")
        print("*[1.4]Lista de productos con menor busqueda  *")
        print("* Porfavor digita una opcion entre 1.1 y1.4: *")
        print("**********************************************")
        opcion2 = input()
        if opcion2 == '1.1':
            nueva = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_sales:
                nueva.append(contador[1])
                # print(nueva)

            repeticiones = {}
            for n in nueva:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            listOfValues = resultado.values()
            #print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            #print(resultado)

            new = [9, 14, 15, 16, 19, 20, 23, 24, 26, 27, 30, 32, 34, 35, 36, 37, 38, 39, 41, 43, 53, 55, 56, 58, 59,
                   61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 86, 87, 88, 90, 91,
                   92, 93]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)

            prueva = [(0, 0)]
            for contador2 in range(1, 95):
                prueva.append((listOfValues[contador2 - 1], contador2))

            ordenados = sorted(prueva, reverse=True)
            for conta in range(0,15):
              print("La siguiente lista te muestra las ventas que tuvo y  el id del producto:")
              print(ordenados[conta])


        elif opcion2 == '1.2':
            nueva = []

            for contador in lifestore_searches:
                nueva.append(contador[1])
                # print(nueva)

            repeticiones = {}
            for n in nueva:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            listOfValues = resultado.values()
            #print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            #print(resultado)

            new = [14, 16, 19, 20, 23, 24, 30, 32, 33, 34, 36, 37, 38, 41, 43, 53, 55, 58, 60, 61, 62, 64, 65, 68, 69,
                   71, 72, 75, 77, 78, 79, 81, 82, 83, 86, 87, 88, 90, 92]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)

            prueva = [(0, 0)]
            for contador2 in range(1, 96):
                prueva.append((listOfValues[contador2 - 1], contador2))

            ordenados = sorted(prueva, reverse=True)
            for conta in range(0, 15):
              print("La siguiente lista te muestra el numero de busquedas y el id del producto:")
              print(ordenados[conta])

        elif opcion2 == '1.3':
            nueva = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_sales:
                nueva.append(contador[1])
                # print(nueva)

            repeticiones = {}
            for n in nueva:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [9, 14, 15, 16, 19, 20, 23, 24, 26, 27, 30, 32, 34, 35, 36, 37, 38, 39, 41, 43, 53, 55, 56, 58, 59,
                   61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 86, 87, 88, 90, 91,
                   92, 93]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)

            prueva = [(0, 0)]
            for contador2 in range(1, 95):
                prueva.append((listOfValues[contador2 - 1], contador2))

            ordenados = sorted(prueva, reverse=False)
            for conta in range(0, 15):
              print("La siguiente lista te muestra las ventas que tuvo y  el id del producto:")
              print(ordenados[conta])



        elif opcion2 == '1.4':
            nueva = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_searches:
                nueva.append(contador[1])
                # print(nueva)

            repeticiones = {}
            for n in nueva:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [14, 16, 19, 20, 23, 24, 30, 32, 33, 34, 36, 37, 38, 41, 43, 53, 55, 58, 60, 61, 62, 64, 65, 68, 69,
                   71, 72, 75, 77, 78, 79, 81, 82, 83, 86, 87, 88, 90, 92]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)

            prueva = [ ]
            for contador2 in range(1, 96):
                prueva.append((listOfValues[contador2 - 1], contador2))

            ordenados = sorted(prueva, reverse=False)
            for conta in range(0, 15):
              print("La siguiente lista te muestra el numero de busquedas y el id del producto:")
              print(ordenados[conta])
        else:
            print("Tecleaste mal ")

    elif opcion == '2':
        print("***********************************************")
        print("*         Que deseas consultar                *")
        print("*[2.1]Lista de productos con mejores reseñas  *")
        print("*[2.2]Lista de productos con perores reseñas  *")
        print("* Porfavor digita una opcion entre 2.1 y 2.2: *")
        print("***********************************************")
        opcion3 = input()
        if opcion3 == '2.1':
            nueva = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_sales:
                nueva.append((contador[2], contador[1]))

            otro = [14, 118, 142, 144, 145, 146, 177, 178, 237]
            for cont in otro:
                del nueva[cont]

            ordenados = sorted(nueva, reverse=True)
            for conta in range(0, 20):
                print("La siguiente lista te muestra el listado con los scores mas altos  y  el id del producto:")
                print(ordenados[conta])
        elif opcion3 == '2.2':
            nueva = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_sales:
                nueva.append((contador[2], contador[1]))

            otro = [14, 118, 142, 144, 145, 146, 177, 178, 237]
            for cont in otro:
                del nueva[cont]

            ordenados = sorted(nueva, reverse=False)
            for conta in range(0, 20):
                print("La siguiente lista te muestra eñ score y  el id del producto:")
                print(ordenados[conta])
        else:
            print("Tecleaste mal ")


    elif opcion == '3':
        print("**********************************************")
        print("*         Que deseas consultar               *")
        print("*[3.1]Total de ingresos mensuales            *")
        print("*[3.2]Total de ingresos anuales              *")
        print("*[3.3]Meses con mas ventas al año            *")
        print("* Porfavor digita una opcion entre 3.1 y 3.3:*")
        print("**********************************************")
        opcion4 = input()
        if opcion4 == '3.1':
            nueva5 = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_products:
                nueva5.append(contador[2])
            # print(nueva5)

            Enero = [5, 7, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 67, 68, 69, 70, 89, 90, 103, 104,
                     141, 142, 143, 144, 150, 171, 177, 189, 190, 197, 198, 199, 206, 208, 251, 252, 253, 254, 255, 256,
                     257, 258, 269, 270, 271, 272, 273, 282]
            nueva = []
            for contador in Enero:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            neww = []
            for contador in nueva:
                neww.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in neww:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33,
                   34, 35, 36, 37, 38, 39, 40, 41, 43, 45, 46, 49, 50, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                   67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92,
                   93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes1 = []
            for conteo in range(1, 95):
                mes1.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes1)

            suma_mensual = sum(mes1)
            print("El promedio total de ventas que tuviste en Enero fue : $", suma_mensual)

            Febrero = [3, 8, 40, 41, 42, 66, 86, 87, 88, 93, 100, 102, 117, 122, 123, 124, 126, 138, 139, 140, 152, 169,
                       170, 178, 188, 195, 196, 205, 244, 245, 246, 247, 248, 249, 250, 265, 266, 267, 268, 277, 278]
            nueva = []
            for contador in Febrero:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new2 = []
            for contador in nueva:
                new2.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new2:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 34, 35, 36, 37, 38,
                   39, 40, 41, 43, 44, 46, 49, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                   71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes2 = []
            for conteo in range(1, 95):
                mes2.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes2)

            suma_mensual = sum(mes2)
            print("El promedio total de ventas que tuviste en Febrero fue : $", suma_mensual)

            Marzo = [9, 10, 11, 36, 37, 38, 39, 64, 65, 83, 84, 85, 92, 98, 99, 108, 113, 114, 115, 116, 121, 128, 129,
                     130, 136, 137, 148, 149, 151, 165, 166, 167, 168, 174, 175, 176, 179, 186, 187, 204, 207, 235, 236,
                     237, 238, 239, 240, 241, 242, 243, 264]
            nueva = []
            for contador in Marzo:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new3 = []
            for contador in nueva:
                new3.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new3:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 8, 9, 10, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 30, 32, 34, 35, 36, 37, 38, 39, 40,
                   41, 43, 45, 48, 49, 50, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
                   74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes3 = []
            for conteo in range(1, 95):
                mes3.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes3)

            suma_mensual = sum(mes3)
            print("El promedio total de ventas que tuviste en Marzo fue : $", suma_mensual)

            Abril = [6, 12, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 60, 61, 62, 63, 77, 78, 79, 80, 81, 82,
                     96, 97, 101, 107, 110, 111, 112, 118, 125, 127, 132, 133, 134, 135, 147, 159, 160, 161, 162, 163,
                     164, 172, 173, 182, 183, 184, 185, 192, 193, 194, 200, 201, 202, 222, 223, 224, 225, 226, 227, 228,
                     229, 230, 231, 232, 233, 234, 263, 276, 281, 283]
            nueva = []
            for contador in Abril:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new4 = []
            for contador in nueva:
                new4.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new4:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 9, 10, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                   41, 43, 45, 46, 50, 51, 52, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73,
                   74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes4 = []
            for conteo in range(1, 95):
                mes4.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes4)

            suma_mensual = sum(mes4)
            print("El promedio total de ventas que tuviste en Abril fue : $", suma_mensual)

            Mayo = [4, 13, 20, 21, 22, 72, 73, 74, 75, 76, 91, 105, 109, 131, 145, 146, 153, 155, 156, 157, 158, 203,
                    214, 215, 216, 217, 218, 219, 220, 221, 260, 261, 262, 275, 279, 280]
            nueva = []
            for contador in Mayo:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new5 = []
            for contador in nueva:
                new5.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new5:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34,
                   35, 36, 37, 38, 39, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64,
                   65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 86, 87, 88, 89, 90, 91, 92,
                   93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes5 = []
            for conteo in range(1, 95):
                mes5.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes5)

            suma_mensual = sum(mes5)
            print("El promedio total de ventas que tuviste en Mayo fue : $", suma_mensual)

            Junio = [14, 18, 19, 58, 59, 95, 106, 120, 181, 213, 274]
            nueva = []
            for contador in Junio:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new6 = []
            for contador in nueva:
                new6.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new6:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                   33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59,
                   61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
                   86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes6 = []
            for conteo in range(1, 95):
                mes6.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes6)

            suma_mensual = sum(mes6)
            print("El promedio total de ventas que tuviste en Junio fue : $", suma_mensual)

            Julio = [1, 2, 16, 17, 71, 94, 154, 180, 211, 212, 259]
            nueva = []
            for contador in Julio:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new7 = []
            for contador in nueva:
                new7.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new7:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55, 56, 58, 59,
                   60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
                   85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes7 = []
            for conteo in range(1, 95):
                mes7.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes7)

            suma_mensual = sum(mes7)
            print("El promedio total de ventas que tuviste en Julio fue : $", suma_mensual)

            Agosto = [191, 209, 210]
            nueva = []
            for contador in Agosto:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new8 = []
            for contador in nueva:
                new8.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new8:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53,
                   55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                   80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes8 = []
            for conteo in range(1, 95):
                mes8.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes8)

            suma_mensual = sum(mes8)
            print("El promedio total de ventas que tuviste en Agosto fue : $", suma_mensual)

            Septiembre = [119]
            nueva = []
            for contador in Septiembre:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new9 = []
            for contador in nueva:
                new9.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new9:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                   29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                   54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
                   79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes9 = []
            for conteo in range(1, 95):
                mes9.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes9)

            suma_mensual = sum(mes9)
            print("El promedio total de ventas que tuviste en Septiembre fue : $", suma_mensual)
            print("El promedio total de ventas que tuviste en Octubre fue : $ 0 ", )

            Noviembre = [15]
            nueva = []
            for contador in Noviembre:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new11 = []
            for contador in nueva:
                new11.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new11:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                   29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                   54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
                   79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes11 = []
            for conteo in range(1, 95):
                mes11.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes11)

            suma_mensual = sum(mes11)
            print("El promedio total de ventas que tuviste en Noviembre fue : $", suma_mensual)
            print("El promedio total de ventas que tuviste en Diciembre fue : $ 0")
        elif opcion4 == '3.2':
            nueva5 = [0]#Nueva lista  para usar el campo requerido

            for contador in lifestore_products:
                nueva5.append(contador[2])

            #print(nueva5)

            nueva = []

            for contador in lifestore_sales:
                nueva.append(contador[1])
            # print(nueva)

            repeticiones = {}
            for n in nueva:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))
            listOfValues = list(listOfValues)
            # print(resultado)

            new = [9, 14, 15, 16, 19, 20, 23, 24, 26, 27, 30, 32, 34, 35, 36, 37, 38, 39, 41, 43, 53, 55, 56, 58, 59,
                   61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 86, 87, 88, 90, 91,
                   92, 93]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)

            prueva = [(0)]
            for contador2 in range(1, 95):
                prueva.append((listOfValues[contador2 - 1]))
            # print(prueva)

            prom = [0]
            for promedio in range(1, 95):
                prom.append((prueva[promedio] * nueva5[promedio]))
            # print(prom)
            suma_mensual = sum(prom)
            print("El promedio total de ventas que tuviste esta año fue de : $", suma_mensual)

        elif opcion4 == '3.3':
            nueva5 = []#Nueva lista  para usar el campo requerido

            for contador in lifestore_products:
                nueva5.append(contador[2])
            Abril = [6, 12, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 60, 61, 62, 63, 77, 78, 79, 80, 81, 82,
                     96, 97, 101, 107, 110, 111, 112, 118, 125, 127, 132, 133, 134, 135, 147, 159, 160, 161, 162, 163,
                     164, 172, 173, 182, 183, 184, 185, 192, 193, 194, 200, 201, 202, 222, 223, 224, 225, 226, 227, 228,
                     229, 230, 231, 232, 233, 234, 263, 276, 281, 283]
            nueva = []
            for contador in Abril:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new4 = []
            for contador in nueva:
                new4.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new4:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 9, 10, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                   41, 43, 45, 46, 50, 51, 52, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73,
                   74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes4 = []
            for conteo in range(1, 95):
                mes4.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes4)

            suma_mensual = sum(mes4)
            print("El mes n°1 con mas ventas fue Abril con: $", suma_mensual)
            Marzo = [9, 10, 11, 36, 37, 38, 39, 64, 65, 83, 84, 85, 92, 98, 99, 108, 113, 114, 115, 116, 121, 128, 129,
                     130, 136, 137, 148, 149, 151, 165, 166, 167, 168, 174, 175, 176, 179, 186, 187, 204, 207, 235, 236,
                     237, 238, 239, 240, 241, 242, 243, 264]
            nueva = []
            for contador in Marzo:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            new3 = []
            for contador in nueva:
                new3.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in new3:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 8, 9, 10, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 30, 32, 34, 35, 36, 37, 38, 39, 40,
                   41, 43, 45, 48, 49, 50, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
                   74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes3 = []
            for conteo in range(1, 95):
                mes3.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes3)

            suma_mensual = sum(mes3)
            print("El  mes n°2  con mas ventas fue Marzo con: $", suma_mensual)
            Enero = [5, 7, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 67, 68, 69, 70, 89, 90, 103, 104,
                     141, 142, 143, 144, 150, 171, 177, 189, 190, 197, 198, 199, 206, 208, 251, 252, 253, 254, 255, 256,
                     257, 258, 269, 270, 271, 272, 273, 282]
            nueva = []
            for contador in Enero:
                nueva.append(lifestore_sales[contador - 1])
            # print(nueva)

            neww = []
            for contador in nueva:
                neww.append(contador[1])

            # print(neww)
            repeticiones = {}
            for n in neww:
                if n in repeticiones:
                    repeticiones[n] += 1
                else:
                    repeticiones[n] = 1

            resultado = {}
            for clave in repeticiones:
                valor = repeticiones[clave]
                if valor != 0:
                    resultado[clave] = valor

            # print(resultado)

            listOfValues = resultado.values()
            # print("Type of variable listOfValues is: ", type(listOfValues))

            listOfValues = list(listOfValues)
            # print(resultado)

            new = [1, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33,
                   34, 35, 36, 37, 38, 39, 40, 41, 43, 45, 46, 49, 50, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                   67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92,
                   93, 94, 95]
            for cont1 in new:
                listOfValues.insert(cont1 - 1, 0)
            # print(listOfValues)

            mes1 = []
            for conteo in range(1, 95):
                mes1.append((nueva5[conteo - 1] * listOfValues[conteo - 1]))

            # print(mes1)

            suma_mensual = sum(mes1)
            print("El  mes n°3  con mas ventas fue Enero con : $", suma_mensual)



        else:
            print("Tecleaste mal ")

    else:
        print('Debes digitar un numero entre 1 y 3')
        print('=-=' * 20)
else:
    print('Hay un error vuelve a intentarlo')

