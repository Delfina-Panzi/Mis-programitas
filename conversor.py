import time

def mostrar_menu():
     print("\n--- CONVERSOR ---")
     print("1. Masa")
     print("2. Longitud")
     print("3. Temperatura")
     print("4. Salir\n")

def elegir_opcion():
     while True:
        try:
            opcion = int(input("Ingresa->\n"))
            if 1<=opcion<=4: 
               return opcion
               
            else: print("-- La opcion debe estar entre 1 y 4 --")
        except: print("-- Ingresa algo valido! --")

def conversor_unidades_masa(numeroParaConvertir, unidad_entrada,unidad_salida):
    unidades = {
        "kg" : 1000,
        "libra" : 453.592,
        "hg" : 100,
        "dag" : 10,
        "g" : 1,
        "dg" : 0.1,
        "cg" : 0.01,
        "mg" : 0.001 
    }
    if unidad_entrada not in unidades or unidad_salida not in unidades:
          return "Error: Unidad no reconocida"
          
        
    pasar_a_gramos = numeroParaConvertir * unidades[unidad_entrada]
    resultado = pasar_a_gramos / unidades[unidad_salida]
    return resultado

def conversor_unidades_temperatura(numeroParaConvertir, unidad_entrada,unidad_salida):
     unidades = ["c","f","k"]
     a_celsius = {
          "c":    lambda v: v,
          "k":     lambda v: v - 273.15,
          "f": lambda v: (v - 32) * 5/9
     }
     desde_celsius = {
        "c":    lambda v: v,
        "k":     lambda v: v + 273.15,
        "f":  lambda v: v * 9/5 + 32
    }
     if unidad_entrada not in unidades or unidad_salida not in unidades:
         return "Error: Unidad no reconocida"
     convertir_a_celsius = a_celsius[unidad_entrada](numeroParaConvertir)
     resultado = desde_celsius[unidad_salida](convertir_a_celsius)
     return resultado
                      
def conversor_unidades_longitud(numeroParaConvertir,unidad_entrada,unidad_salida):
     unidades = {
     "km": 1000, #Kilometro
     "mi": 1609.34,     #Milla
    "hm": 100,       # Hectómetro
    "dam": 10,       # Decámetro
    "m": 1,          # Metro (nuestro pivote)
    "dm": 0.1,       # Decímetro
    "cm": 0.01,      # Centímetro
    "mm": 0.001,     # Milímetro
    "in": 0.0254,    # Pulgada 
    "ft": 0.3048     # Pie
     }
     if unidad_entrada not in unidades or unidad_salida not in unidades:
         return "Error: Unidad no reconocida"
     convertir_a_metros = numeroParaConvertir * unidades[unidad_entrada]
     resultado = convertir_a_metros / unidades[unidad_salida]
     return resultado

def pedir_unidad_longitud(valor):
    time.sleep(0.5)
    print(f"\n{valor} ¿qué?... \n")
    time.sleep(0.3)
    
    print("--- UNIDADES DE LONGITUD ---")
    # Mostramos las unidades que soporta nuestro diccionario
    print("-> mi (Millas)")
    print("-> km (Kilómetros)")
    print("-> m  (Metros)")
    print("-> cm (Centímetros)")
    print("-> mm (Milímetros)")
    print("-> in (Pulgadas)")
    print("----------------------------")
    
    time.sleep(0.4)
    
    # .strip() elimina espacios accidentales que el usuario pueda escribir
    unidad_entrada = input("Elegí tu unidad de entrada: ").lower().strip()
    unidad_salida = input("Ahora tu unidad de salida: ").lower().strip()
    if unidad_entrada not in unidades or unidad_salida not in unidades:
      return "Error: Unidad no reconocida"
    
    # Retornamos ambas unidades en una tupla
    unidades = (unidad_entrada,unidad_salida)
    return unidades

def pedir_unidad_temperatura (valor):
     time.sleep(0.5)
     print(f"\n{valor} que?...\n")
     time.sleep(0.3)
     unidades = ["c","k","f"]
     print("--- TEMPERATURA ---")
     print("-> °C (Celsius)")
     print("-> K (Kelvin)")
     print("-> °F (Farenheit)")
     
     print("-- --")
     time.sleep(0.4)
     
     unidad_entrada= input("Elegi tu unidad de entrada: ").lower()
     unidad_salida = input("Ahora tu unidad de salida: ").lower()
     
     unidades = (unidad_entrada,unidad_salida)
     return unidades

def pedir_unidad_masa (valor):
     time.sleep(0.5)
     print(f"\n{valor} que?...\n")
     time.sleep(0.3)
     print("--- MASA ---")
     print("-> kg")
     print("-> hg")
     print("-> dag")
     print("-> g")
     print("-> dg")
     print("-> cg")
     print("-> mg")
     print("-- --")
     time.sleep(0.4)
     unidad_entrada= input("Elegi tu unidad de entrada: ").lower()
     unidad_salida = input("Ahora tu unidad de salida: ").lower()
     unidades = (unidad_entrada,unidad_salida)
     return unidades

mostrar_menu()
opcion = elegir_opcion()


if opcion == 1:
     numero = int(input("¿Que valor queres convertir?\n--> "))
     (entrada,salida)=pedir_unidad_masa(numero)
     resultado = conversor_unidades_masa(numero, entrada,salida)
     print(f"Tu resultado es {resultado}{salida}")
if opcion == 3:
      numero = int(input("¿Que valor queres convertir?\n--> "))
      (entrada,salida)=pedir_unidad_temperatura(numero)
      resultado = conversor_unidades_temperatura(numero, entrada,salida)
      print(f"Tu resultado es {resultado} {salida.upper()}")

if opcion == 2:
     numero = int(input("¿Que valor queres convertir?\n--> "))
     (entrada,salida)=pedir_unidad_longitud(numero)
     resultado = conversor_unidades_longitud(numero, entrada,salida)
     print(f"Tu resultado es {resultado} {salida}")





     
     



     
     
         
    
    
    
    


    


    
     
          


