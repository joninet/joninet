class Solution:
    def plusOne(self, digits):
        result = []
        carry = 1  # Inicializamos el acarreo con 1, ya que estamos sumando 1

        for x in range(len(digits) - 1, -1, -1):
            num = digits[x]
            
            if carry:
                num += carry
                carry = 0  # Reseteamos el acarreo después de sumar

            if num == 10:
                carry = 1
                result.insert(0, 0)
            else:
                result.insert(0, num)

        if carry:
            result.insert(0, carry)

        return result

# Ejemplo de uso:
ejer = Solution()
print(ejer.plusOne([9, 9]))
