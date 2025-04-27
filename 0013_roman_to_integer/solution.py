# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

import os # Importar módulo del sistema operativo
os.system("cls")

class Solution:
    def romanToInt(self, s: str) -> int:
        # La longitud de la cadena debe ser entre 1 y 15
        if len(s) < 1 or len(s) > 15:
            return None

        # diccionario con los valores de las distintas letras romanas
        roman_to_int = {
          "I":1,
          "V":5,
          "X":10,
          "L":50,
          "C":100,
          "D":500,
          "M":1000
        }

        # Comprobar si todos los caracteres son correctos
        for letra in s:
           if letra not in roman_to_int:
              return None 

        s = reversed(s)
        result = 0
        lentra_anterior = ''
        for letra in s:
            if lentra_anterior != '' and (roman_to_int[letra] < roman_to_int[lentra_anterior]):
              result -= roman_to_int[letra]
            else:
              result += roman_to_int[letra]
            lentra_anterior = letra
        return result

solution = Solution()
print(solution.romanToInt("III")) # 3
print(solution.romanToInt("LVIII")) # 58
print(solution.romanToInt("MCMXCIV")) # 1994
print(solution.romanToInt("D")) # 1900
