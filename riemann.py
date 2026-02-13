from sympy import *

funcion_string = None 
funcion_expresion = None
x_eval = 0          # El punto donde queremos la derivada
h = 0               # El tamaño del paso (incremento)
x = symbols('x')    # Declarar la variable x

funcion_string = input("Indique la funcion a evaluar\n[arctan = atan(), e = exp(), potencia = **, logaritmo natural = ln()]\n")
try: 
    funcion_expresion = sympify(funcion_string) # Conversion de string a simbolico
except Exception as R:
    print(f"Error al interpretar la función: {R}")
    exit()

x_eval = float(input("\nIndique el punto donde desea evaluar la derivada (x):\n"))
h = float(input("Indique el tamaño del paso (h) [Ejemplo: 0.01 o 0.0001]:\n"))

#convertir a funcion numerica
f = lambdify(x, funcion_expresion, modules=['math'])

#calcular la derivada exacta con sympy
df_simbolica = diff(funcion_expresion, x)
df_exacta = lambdify(x, df_simbolica, modules=['math'])

try:
    # diferencia hacia adelante [f(x + h) - f(x)] / h
    derivada_adelante = (f(x_eval + h) - f(x_eval)) / h

    #diferencia hacia atrás [f(x) - f(x - h)] / h
    derivada_atras = (f(x_eval) - f(x_eval - h)) / h

    #diferencia centrada [f(x + h) - f(x - h)] / (2 * h)
   
    derivada_centrada = (f(x_eval + h) - f(x_eval - h)) / (2 * h)

    #valor real
    valor_real = df_exacta(x_eval)

except Exception as e:
    print(f"Error en los cálculos: {e}")
    exit()

#resultados
print(f"\n" + "="*50)
print(f"ANÁLISIS DE LA DERIVADA EN x = {x_eval}")
print(f"Función: {funcion_expresion}")
print(f"Derivada exacta f'(x): {df_simbolica}")
print(f"Paso (h) utilizado: {h}")
print("="*50)

print(f"{'Método':<25} | {'Resultado':<15} | {'Error Absoluto'}")
print("-" * 65)
print(f"{'Hacia Adelante':<25} | {derivada_adelante:<15.6f} | {abs(valor_real - derivada_adelante):.8f}")
print(f"{'Hacia Atrás':<25} | {derivada_atras:<15.6f} | {abs(valor_real - derivada_atras):.8f}")
print(f"{'Diferencia Centrada':<25} | {derivada_centrada:<15.6f} | {abs(valor_real - derivada_centrada):.8f}")
print("-" * 65)
print(f"VALOR REAL (Analítico): {valor_real:.6f}")

print("="*50)
