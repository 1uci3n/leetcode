iclass Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        result = 0
        while i < len(s):
            if s[i] == 'V':
                result += 5
                i += 1
                continue
            elif s[i] == 'L':
                result += 50
                i += 1
                continue
            elif s[i] == 'D':
                result += 500
                i += 1
                continue
            elif s[i] == 'M':
                result += 1000
                i += 1
                continue
            elif s[i] == 'I':
                if i == len(s) - 1:
                    result += 1
                    break
                elif s[i + 1] == 'V':
                    result += 4
                    i += 2
                    continue
                elif s[i + 1] == 'X':
                    result += 9
                    i += 2
                    continue
                else:
                    result += 1
                    i += 1
                    continue
            elif s[i] == 'X':
                if i == len(s) - 1:
                    result += 10
                    break
                elif s[i + 1] == 'L':
                    result += 40
                    i += 2
                    continue
                elif s[i + 1] == 'C':
                    result += 90
                    i += 2
                    continue
                else:
                    result += 10
                    i += 1
                    continue
                    
            elif s[i] == 'C':
                if i == len(s) - 1:
                    result += 100
                    break
                elif s[i + 1] == 'D':
                    result += 400
                    i += 2
                    continue
                elif s[i + 1] == 'M':
                    result += 900
                    i += 2
                    continue
                else:
                    result += 100
                    i += 1
                    continue
        return result
