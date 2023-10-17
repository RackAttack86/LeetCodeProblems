from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    commonPrefix = ""
    if not strs: return commonPrefix
    shortest_str = min(strs, key=len)
    for i in range(len(shortest_str)):
        if all([x.startswith(shortest_str[:i+1]) for x in strs]):
            commonPrefix = shortest_str[:i+1]
        else:
            break
    return commonPrefix

result = longestCommonPrefix(["flower","flow","flight"])
print(result)
assert(result == "fl")

result = longestCommonPrefix(["dog","racecar","car"])
print(result)
assert (result == "")