# Función que valida si una CI ecuatoriana es válida
# 2021 Victor Bayas

def validar_cedula(cedula):
    longitud = len(cedula)
    # Validar que la CI contenga exactamente 10 dígitos
    if longitud == 10:
        provincia = int(cedula[0:2])  # dos primeros dígitos de la CI
        # Son válidas las provincias del 1 al 24 (o 30 en el caso de los ecuatorianos nacidos en el extranjero)
        if 1 <= provincia <= 24 or provincia == 30:
            tercer_digito = int(cedula[2])
            # El tercer dígito debe estar entre 0 y 6
            if 0 <= tercer_digito <= 6:
                validador = int(cedula[9])
                coeficientes = (2, 1, 2, 1, 2, 1, 2, 1, 2)  # coeficientes del módulo 10
                suma = 0
                for i in range(0, len(coeficientes)):
                    multip = (int(cedula[i])*coeficientes[i])
                    # Si una multiplicación es >= 10 se le debe restar 9
                    if multip >= 10:
                        multip -= 9
                    # print(f'Digito {int(cedula[i])}, multiplicacion {multip}')
                    suma += multip
                mod = suma % 10  # calculamos el módulo 10
                resta = 10 - mod  # para calcular el validador restamos de 10 el módulo obtenido
                print(f'\nSuma: {suma}\n'
                      f'Módulo 10 de la suma: {mod}\n'
                      f'Resta del módulo: {resta}\n'
                      f'Validador: {validador}\n')
                # Una cédula es válida si la resta de 10 menos el módulo y el validador son iguales
                # Las cédulas que terminan en 0 sólo son válidas si el módulo también es 0 por ser un caso especial
                if resta == validador or (mod == 0 and validador == 0):
                    print(f'La cédula {cedula} es válida')
                else:
                    print(f'La cédula {cedula} no es válida')
            else:
                print('El tercer dígito no es válido')
        else:
            print('El código de provincia no es válido')
    else:
        print('Un número de cédula debe tener 10 dígitos')


# Uso: validar_cedula(nro_cedula), pasar valor como un string
nro_cedula = input('Ingrese un número de cédula: ')
validar_cedula(nro_cedula)
