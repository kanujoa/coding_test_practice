N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

if N > M :
  smaller = M_list
  bigger = N_list
else:
  smaller = N_list
  bigger = M_list

insert_idx = 0
for n in smaller:
  for idx in range(insert_idx, len(bigger)):
    if n <= bigger[idx]:
      bigger.insert(idx, n)
      insert_idx = idx
      break
for num in bigger:
  print(num, end=" ")