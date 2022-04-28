class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            short = num1
            long = num2
        else:
            short = num2
            long = num1
        
        output = 0
        for i in range(len(short)-1, -1, -1):
            temp = self.helper(long, short[i])
            # print(temp)
            output += temp * 10 ** (len(short) -1 - i)
        return str(output)
            
        
    def helper(self, long: str, char: str):
        carry = 0
        ans = 0
        n = len(long)
        short_int = ord(char) - ord('0')
        for i in range(n-1, -1, -1):
            prod = ((ord(long[i]) - ord('0')) * short_int + carry)
            carry = prod // 10
            ans += (prod % 10) * 10 ** (n-1-i)
        
        if carry != 0:
            ans += carry*10**n
        return ans
    