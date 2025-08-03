#["a","a","b","b","c","c","c"]
#["a",2,"b",2,"c",3]

from collections import Counter
class Solution(object):
    def compress(self, chars):
        count=Counter(chars)
        chars=[]
        for item , freq in count.items():
            if freq>1 and freq<11:
                #print(f"'{item}': '{freq}'")

                chars.append(item)
                chars.append(str(freq))
            elif freq==1:
                chars.append(item)
            elif freq>10:
                chars.append(item)
                chars.append(str(freq//10))
                chars.append(str(freq%10))
            else:
                chars.append(item)
                chars.append(str(freq))
        print(chars)
        return len(chars)

s=Solution()
a=["a","a","b","b","c","c"]
print(s.compress(a))