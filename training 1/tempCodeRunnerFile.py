from collections import Counter
n = int(input())
all = list(map(int, input().split()))
if n==2:
    print(max(all) - min(all))
    exit()
V = [all[i] for i in range(len(all)) if i % 2 == 0]
M = [all[i] for i in range(len(all)) if i % 2 == 1]
V_count = Counter(V)
M_count = Counter(M)

v_min = min(V_count)
m_max = max(M_count)

V_count[m_max] += 1
V_count[v_min] -= 1
if V_count[v_min] == 0:
    del V_count[v_min]
M_count[v_min] += 1
M_count[m_max] -= 1
if M_count[m_max] == 0:
    del M_count[m_max]
total = 0
for key, value in V_count.items():
    total += key * value
for key, value in M_count.items():
    total -= key * value
print(total)