import time 
import random 

victoria_pc = 0
victoria_yo = 0
opciones = ["piedra","papel","tijera"]

if input("Vamos a jugar piedra papel o tijera!!! listo? (pone 'si' para aceptar): ").lower() == "si":
    print("Joya, tenes 'tijera' para tijera, 'papel' para papel y 'piedra' para piedra")
    while victoria_yo <3 and victoria_pc <3:
        tirada = input("Vas vos: ").lower()
        if tirada() not in opciones:
            print("no valido")
            break
        else:
            tirada_maquina = random.choice(opciones)
            time.sleep(1)
            print(f"La computadora eligio: {tirada_maquina}")
            if(tirada_maquina==tirada):
                time.sleep(0.5)
                print(f"Empate! van \n{victoria_pc} \n{victoria_yo} ")
                print("----------")
                time.sleep(1)

            elif ((tirada.lower=="tijera" and tirada_maquina=="piedra") or 
                  (tirada_maquina=="papel" and tirada=="piedra") or  
                  (tirada_maquina=="tijera" and tirada=="papel")):
                victoria_pc = victoria_pc+1
                time.sleep(0.5)
                print(f"Punto para la maquina! van \nMaquina:{victoria_pc} \nVos: {victoria_yo}")
                print("----------")
                time.sleep(1)
            
            else: 
                victoria_yo=victoria_yo+1
                time.sleep(0.5)
                print(f"Punto para vos! van \nMaquina: {victoria_pc} \nVos: {victoria_yo}") 
                print("----------")
                time.sleep(1)
    
    if victoria_pc == 3 : print("Gano la pc, mas suerte para la proxima!")
    elif victoria_yo==3 : print("Ganaste vos! felicidades!!!")
           
else : print("Mieeedoooso/a...")