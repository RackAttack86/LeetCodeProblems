
def romanToInt(s: str) -> int:
    d = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    i = 0
    total = 0
    while i < len(s):
        if i+1<len(s):
            if (d[s[i]] < d[s[i+1]]):
                total += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                total += d[s[i]]
                i += 1
        else:
            #print(i)
            total+=d[s[i]]
            i+=1
    return total

result = romanToInt("III")
print(result)
assert(result == 3)

result = romanToInt("IV")
print(result)
assert(result == 4)

result = romanToInt("LVIII")
print(result)
assert(result == 58)

result = romanToInt("MCMXCIV")
print(result)
assert(result == 1994)