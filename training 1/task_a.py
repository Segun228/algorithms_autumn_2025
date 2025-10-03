from collections import Counter
n = int(input())
all = list(map(int, input().split()))
V = [all[i] for i in range(n) if i % 2 == 0]
M = [all[i] for i in range(n) if i % 2 == 1]
V_count = Counter(V)
M_count = Counter(M)
v_min = min(V_count)
m_max = max(M_count)
if v_min < m_max:
    V_count[m_max] += 1
    V_count[v_min] -= 1
    M_count[v_min] += 1
    M_count[m_max] -= 1
total = 0
for key, value in V_count.items():
    total += key * value
for key, value in M_count.items():
    total -= key * value
print(total)