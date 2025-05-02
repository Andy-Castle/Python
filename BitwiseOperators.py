# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift rigth operation

#Estos operadores son de bit a bit, estos trabajan directamente
# sobre los bits que componen los numeros enteros

#Este compara cada bit de dos numeros y devuelve 1 solo si ambos bits son 1
# 5 = 0101, 3 = 0011 → resultado: 0001 (1)
print(5 & 3) #1

#Este compara cada bit de dos números y devuelve 1 si al menos uno de los bits es 1
# 0101 | 0011 → 0111 (7)
print(5 | 3) #7

#Este Devuelve 1 si los bits son diferentes
# 0101 ^ 0011 → 0110 (6)
print(5 ^ 3) #6

#Este invierte todos los bits del numero
# si 5 = 0101 → ~5 = ...1010 (en complemento a dos: -6)
print(~5) #-6

#Este desplaza todos los bits a la izquierda, agregando ceros. Multiplica por 2 por cada desplazamiento.
# 0101 → 1010 (10) → 5 * 2^1 = 10
print(5 << 1) #10

#Este desplaza todos los bits a la derecha. Divide entre 2 por cada desplazamiento.
# 0101 → 0010 (2) → 5 // 2 = 2
print(5 >> 1) # 2