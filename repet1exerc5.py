"""
REPETIÇÃO5) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O programa deverá apresentar os valores das duas temperaturas.
"""

#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9.0 * C + 160.0) / 5.0, sendo F a temperatura em Fahrenheit e a temperatura em Celsius. Dica: use a funcionalidade eval() para a entrada da temperatura.
C = eval(input("Grau Celsius = "))
 
F = (9.0 * C + 160.0) / 5.0
 
print("%6.2f °C = %6.2f °F" % (C, F))
 
sair = input("\nTecle ENTER para sair...")

#Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C = ((F – 32.0) * 5.0) / 9.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. Dica: use a funcionalidade foat() para a entrada da temperatura.
F = float(input("Grau Fahrenheit = "))
 
C = ((F - 32.0) * 5.0) / 9.0
 
print("%6.2f °F = %6.2f °C" % (F, C))
 
sair = input("\nTecle ENTER para sair...")