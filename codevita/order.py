# taking input
n = int(input())

input()  # blank line
shuffle = []
for i in range(n):
    shuffle.append(input())   

input()  # blank line
original = []
for i in range(n):
    original.append(input())

# mapping
sdi = {inst: i for i, inst in enumerate(shuffle)}

# original index    :   position of shuffled instruction
position = [sdi[inst] for inst in original]


# finding LIS l ongest increasing subsequence
import bisect
lis = []
for x in position:
    idx = bisect.bisect_left(lis, x)
    if idx == len(lis):
        lis.append(x)
    else:
        lis[idx] = x
l = len(lis)

# elements required to be moved
if l == n:
    # alreeady in order
    print(0)
    exit()
else:
    def get_lis_idx(arr):
        import bisect
        lis = []
        parent = [-1] * len(arr)
        lis_idx = []

        for i, x in enumerate(arr):
            idx = bisect.bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
                lis_idx.append(i)
            else:
                lis[idx] = x
                lis_idx[idx] = i
            if idx > 0:
                parent[i] = lis_idx[idx - 1]

        res = []
        k = lis_idx[-1]

        while k >= 0:
            res.append(k)
            k = parent[k]
        return set(res[::-1])

lis_indexes = get_lis_idx(position)
to_move = []
for i in range(n):
    if i not in lis_indexes:
        to_move.append(i)

# check for contiguity
is_continuous = True
for i in range(len(to_move) - 1):
    if to_move[i] + 1 != to_move[i + 1]:
        is_continuous = False
        break

is_continuous_shuffled = True

to_move_shuffled_indices = [sdi[original[i]] for i in to_move]
to_move_shuffled_indices.sort()

for i in range(len(to_move_shuffled_indices) - 1):
        if to_move_shuffled_indices[i+1] - to_move_shuffled_indices[i] != 1:
            is_contiguous_shuffled = False
            break

# cost calculation
if is_continuous and is_continuous_shuffled:
    cost = 1
else:
    cost = n-l
print(cost)