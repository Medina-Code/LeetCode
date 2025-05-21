# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

import os # Importar módulo del sistema operativo
os.system("cls")

class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    # La longitud de la lista entre 1 y 200
    if len(strs) < 1 or len(strs) > 200:
      return None

    # La longitud de cada cadena de la lista entre 1 y 200
    min_len = len(strs[0])
    for cadena in strs:
      if min_len > len(cadena):
        min_len = len(cadena)
      if len(cadena) < 1 or len(cadena) > 200:
        return None

    result = ""
    for index in range(min_len):
        letra = strs[0][index]
        for cadena in strs:
          if letra != cadena[index]:
            break
        result = result + letra
           
solution = Solution()
print(solution.longestCommonPrefix(strs=["flower","flow","flight"]))
print(solution.longestCommonPrefix(strs=["dog","racecar","car"]))
