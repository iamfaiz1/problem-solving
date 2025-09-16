

# instrutive approach
class Solution:
    def sortVowels(self, s: str) -> str:
        queue = []
        st = set(list("aeiouAEIOU"))
        for i in s:
            if i in st:
                queue.append(i)
        
        queue.sort()
        t = []
        for i in s:
            if i in st:
                t.append(queue.pop(0))
            else:
                t.append(i)
        # print(t)
        # print(queue)
        return "".join(t)


# faster approach (no asymptotic change)
# storing frequency of vowels and replacing them in order
from collections import Counter
class Solution:
    def sortVowels(self, s: str) -> str:
        queue = []
        st = set(['a','e','i','o','u','A','E','I','O','U'])
        count = Counter(s)

        for i in count.keys():
            if i in st:
                queue.append(i)
                s = s.replace(i, '#')
        
        queue.sort()

        for q in queue:
            if q in count:
                s = s.replace('#', q, count[q])
        return s