from collections import defaultdict

def convertDecimal(date):
    base = date[0]
    n = date[1]
    
    if base <=1:
        return -1
    
    decimal = 0
    d = 1
    while(n):
        r = n%10
        if r>=base:
            return -1
        decimal += r*d
        d*= base
        n = n//10
    return decimal

def solve(dates):
    # Write your code here
    count = 0
    ans = 0
    # dates = list(set(tuple (d) for d in dates))
    di = defaultdict(int)
    for date in dates:
        x = convertDecimal(date)
        if x ==-1:
            continue
        di[x] += 1
    
    ans = 0
    for freq in di.values():
        ans += (freq * (freq - 1)) // 2
    
    return ans