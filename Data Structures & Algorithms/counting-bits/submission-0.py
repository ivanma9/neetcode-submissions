class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        bit_offset = 1
        for i in range(1,n+1):
            if bit_offset * 2 == i:
                bit_offset = i
            output[i] = 1 + output[i-bit_offset]
            
        return output

        # 00000 0
        # 00001 1
        # 00010 1
        # 00011 2
        # 00100 1 -> powers of 2 is 1
        # 00101 2 
        # 00110 2
        # 00111 3
        # 01000 1 ->
        # 01001 2
        # 01010 2
        # 01011 3
        # 01100 2
        # 01101 3
        # 01110 3
        # 01111 4