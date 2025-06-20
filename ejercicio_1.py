#implementar una calculadora que pida dos numeros y una operacion, vamos a usar la figura de switch....case y luego con if..  elif...esle


#CALCULADORA BASICA

num_1 = float(input("primer numero a consultar"))

num_2 =float(input("segundo numero a consultar"))

operador = input("quer operacion va hacer +,-,/,*): ")

# como asi que switch y case? 
# switch y case forma diferente de escribir condicionales, donde se evalua un parametro booleano, y se va direccionar inmediatamente segun los casos definidos

match operador:
    case "+":
        print("resultado", num_1 + num_2)
    case "-":
        print("resultado", num_1 - num_2)
    case "*":
        print("resultado", num_1 * num_2)
    case "/":
        if num_2 != 0:
            print("resultado", num_1 - num_2)
        else:
            print("resultado no valido")
    case _:
        print("resultado no valido")








