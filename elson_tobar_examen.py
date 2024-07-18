import random

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"] 

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000 , 2500000)for _ in range(10)]

def clasificar_sueldos():
    global sueldos
    sueldos_ordenados = sorted(sueldos)

    print("sueldos menores a 800.000")
    count1= 0
    for sueldos in sueldos_ordenados:
        if sueldo < 800000:
            count1 +=1
            print(f"{trabajadores[sueldos.index(sueldo)]}-${sueldo}")
    
    print(f"TOTAL:{count1}")

    print("sueldos entre $800.000 y 2.500.000:")
    count2 = 0
    for sueldo in sueldos_ordenados:
        if 800000 <= 2000000:
            count2 += 1
            print(f"{trabajadores[sueldos.index(sueldo)]}-${sueldo}")
    print(f"TOTAL:{count2}")

    print("sueldos superiores a 2.000.000")
    count3 = 0
    for sueldo in sueldos_ordenados:
        if sueldo > 2000000:
            count3 += 1
            print(f"{trabajadores[sueldos.index(sueldo)]}-${sueldo}")
    print(f"TOTAL:{count3}")

    total_sueldos = sum(sueldos)
    print(f"total sueldos: $ {total_sueldos}")

def ver_estadisticas():
    global sueldos

    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajos = min (sueldos)
    promedio_sueldos = sum(sueldos)/ len(sueldos)

    print(f"sueldo mas alto: ${sueldo_mas_alto}")
    print(f"sueldo mas bajo: $ {sueldo_mas_bajos}")
    print(f"promedio de sueldos: $ {promedio_sueldos:.2f}")


def reporte_sueldos():
    global sueldos

    descuento_salud = 0.07
    descuento_afp = 0.12

    print("reporte de sueldos")
    for i, (trabajador, sueldo) in enumerate(zip(trabajadores, sueldos)):
        descuento_total = (sueldo * descuento_salud) + (sueldo*descuento_afp)
        sueldo_liquido = sueldo - descuento_total
        print(f"{i+1}.{trabajador}:")
        print(f" sueldo base:${sueldo}")
        print(f" descuento salud(7%):${sueldo*descuento_salud:2f}")
        print(f" descuento afp(12%):${sueldo*descuento_afp:2f}")
        print(f" sueldo liquido:${sueldo_liquido:2f}")

def main():
    while True:
        print("------------MENU------------")
        print("1. Asignar sueldos aleatorio")
        print("2. Clasificar sueldos       ")
        print("3. Ver estadistica          ")
        print("4. Reporte de sueldos       ")
        print("5. Salir del programa       ")

        opcion = input("seleccione una opcion 1-5:")

        if opcion == "1":
            asignar_sueldos_aleatorios()
            print("Sueldos asignados aleatoriamente")
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("programa finalizado")
            break
        else:
            print("opcion no valida intente de nuevo")
        
        
            
            
if __name__=="__main__":
    main()
    
        






