class Solution:
    def romanToInt(self, s: str) -> int:
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000
        numero=0
        for rom in range(len(s)):
            numNew=s[rom]
            if numNew == "I":
                numero+=I
            elif numNew == "V":
                numero+=V
            elif numNew == "X":
                numero+=X
            elif numNew == "L":
                numero+=L
            elif numNew == "C":
                numero+=C
            elif numNew == "D":
                numero+=D
            elif numNew == "M":
                numero+=M
        return numero
romano=Solution()
print(romano.romanToInt("III"))

                