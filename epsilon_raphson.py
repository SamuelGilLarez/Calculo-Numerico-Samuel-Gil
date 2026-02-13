from sympy import * #Libreria que convierte strings en expresiones matematicas

funcion_string = None           
funcion_expresion = None    #Una variable funcion para guardar el string y otra para guardar la version modificada por sympy
dfunc_expresion = None
a = 0
b = 0   #Donde inicia y termina el intervalo
objetivo = 0 #Porcentaje de error al que se quiere llegar
error = 1
x0 = 0
i = 0
i_max = 30 #Para que no explote la laptop si la embarro
x = symbols('x')    #Declarar la variable que se usara. En este caso X, pero se podria cambiar por otra letra


funcion_string = input("Indique la funcion a evaluar\n[arctan = atan(), e = exp(), potencia = **, logaritmo natural = ln()]\n")    #Pedir al usuario los datos
try:    #El bloque try permite capturar un error sin que el programa se desbarate
    funcion_expresion = sympify(funcion_string) #Conversion
except Exception as R:
    print(f"Error al interpretar la función: {R}")
    exit()

a = input("\nIndique el intervalo (a,b)\na = ")
b = input("b = ")

try: #Verificar que el intervalo es valido
    a = float(a)
    b = float(b)
except ValueError:
    print("Los valores del intervalo deben ser números.")
    exit()

objetivo = input("Indique el porcentaje de error\n")
objetivo = float(objetivo)

if a < b: #Mostrar al usuario los datos que ha ingresado
    print(f"\nDatos:\nFuncion = {funcion_string}\nIntervalo = ({a} , {b})")
elif a == b:
    print("Indique 2 numeros diferentes para el intervalo")
    exit()
else:
    print(f"\nDatos:\nFuncion = {funcion_string}\nIntervalo = ({b} , {a})")

f = lambdify(x, funcion_expresion, modules=['math'])

x0 = (a+b)/2
dfuncion_expresion = diff(funcion_expresion, x)
f = lambdify(x, funcion_expresion, modules=['sympy'])
df = lambdify(x, dfuncion_expresion, modules=['sympy'])
d2funcion_expresion = diff(dfuncion_expresion, x)
d2f = lambdify(x, d2funcion_expresion, modules=['sympy'])

try:
    convergencia = abs(f(x0) * d2f(x0) / (df(x0)**2))
    print(f"\nCriterio de convergencia en x = {x0}: {convergencia:.6f}")
    if convergencia < 1:
        print("converge.")
    else:
        print("No converge")
except Exception as e:
    print(f"Error al evaluar el criterio de convergencia: {e}")
    exit()

x_actual = x0
error = 100
i = 0

while error > objetivo and i < i_max:
    try:
        fx = f(x_actual)
        dfx = df(x_actual)

        if dfx == 0:
            print("Derivada cero. No se puede continuar.")
            break

        x_siguiente = x_actual - fx / dfx
        error = abs((x_siguiente - x_actual) / x_siguiente) * 100

        print(f"Iteración {i+1}: x = {x_siguiente:.10f}, f(x) = {fx:.10f}, error = {error:.6f}%")

        x_actual = x_siguiente
        i += 1

    except Exception as e:
        print(f"Error durante la iteración: {e}")
        break

if error <= objetivo:
    print(f"\n Raíz aproximada encontrada: {x_actual:.10f} con error de {error:.6f}% en {i} iteraciones.")
else:
    print("\n No se alcanzó el error deseado dentro del número máximo de iteraciones.")

