class Solution:
    def romanToInt(self, s: str) -> int:
        str = list(s)
        i = len(s)
        str.append("0")

        count = 0
        for i in range(0,i):
            if str[i] == 'I' and (str[i+1] == 'V' or str[i+1] == 'X'):
                count -= 1
            elif str[i] == 'I' and str[i+1] != 'X':
                count += 1
            elif str[i] == 'V':
                count += 5
            elif str[i] == 'X' and (str[i+1] == 'L' or str[i+1] == 'C'):
                count -= 10
            elif str[i] == 'X' and str[i+1] != 'C' and str[i+1] != 'L':
                count += 10
            elif str[i] == 'L':
                count += 50
            elif str[i] == 'C' and (str[i+1] == 'D' or str[i+1] == 'M'):
                count -= 100
            elif str[i] == 'C' and str[i+1] != 'M' and str[i+1] != 'D':
                count += 100

            elif str[i] == 'D':
                count += 500
            elif str[i] == 'M':
                count += 1000
            print(count)





if __name__ == '__main__':
    romanToInt = Solution.romanToInt('"MCDLXXVI"',"MCDLXXVI",)

  #  "MCDLXXVI"