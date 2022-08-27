f = open('test.txt')
n = int(f.readline())
m = [float('inf')] * 1000
ms = 0
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 1000 == 0:
        ms = max(ms, s)
    ms = max(ms, s - m[s % 1000])
    m[s % 1000] = min(m[s % 1000], s)
print(ms)