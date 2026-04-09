
def factorial(numero_n):
        
        resultado=1
        for i in range(1, numero_n +1):
            resultado = resultado * i
        return resultado

print ("Dame un numero: ")
numero = input()

if numero.isdigit(): # esta funcion .isdigit verifica si tiene numeros
    #tambien esta la funcion .isnumeric que abarcan mas numeros (fracciones y romanos)
    numero_n=int(numero)
    if numero_n<999 :
         print("Su factorial es: ")
         print(factorial(numero_n))
    else : print ("ingresa un numero mas chico, queres romper mi pc?") 

else: print("Tenes que ingresar un numero...")


