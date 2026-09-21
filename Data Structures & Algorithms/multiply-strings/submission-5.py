class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        res = 0
        for i in range(n1-1,-1,-1):
            carry = 0
            for j in range(n2-1, -1, -1):
                 # for jth digit in num2
                 # multiply by ith digit in num1
                 # multiply by n2-1 -j + i  2- 1 -1 +0*10
                 # if carry still has some add carry bit with offset +1
                                            # 2 -1-0 + 1 * 10 = 10

                product = (int(num1[i]) * int(num2[j])) + carry
                digit = product % 10
                carry = product // 10
                print((n2-1 - j + n1-1-i))
                res += digit * (10 ** (n2-1 - j + n1-1-i)) 
                print(digit, carry, res)

            if (carry > 0):
                res += carry * (10 ** (n2-1 + n1-1-i +1))
        
        return str(res)

