def factorial(n):
    try:
        assert n >= 0, "Error, no hay factorial de numeros negativos."

        fact = 1
        for i in range(2,n+1):
            fact *= i
    except AssertionError as a:
        print(a)
    else:
        print("\nEl factorial es: ", fact)

def dividir(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Error, no se puede dividir entre cero.")
            
        resultado = a / b
    except ZeroDivisionError as ve:
        print(ve)
    else:
        print("\nEl resultado es: ", resultado)

while True:
    print("\nElige una opcion:")
    print("1) Factorial de un numero")
    print("2) Division de dos numeros")
    print("3) Salir")
    op = input("> ")

    if op == "1":
        while True:
            numero = (input("Introduce un numero entero: "))
            try:
                n = int(numero)
                break 
            except ValueError:
                print("No es un numero entero.\n")

        factorial(n)
    
    elif op == "2":
        while True:
            numero1 = (input("Introduce un numero: "))
            numero2 = (input("Introduce otro numero: "))
            try:
                n1 = float(numero1)
                n2 = float(numero2)
                break 
            except ValueError:
                print("Ambos deben ser numeros.\n")

        dividir(n1,n2)

    elif op == "3":
        print("Hasta luego\n")
        break

    else:
        print("Opcion no valida.")