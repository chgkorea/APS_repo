def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)

    return parents, ranks

def find_set(n):
    if n == parents[n]:
        return n
    
    parents[n] = find_set(parents[n])
    return parents[n]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    rank_x = ranks[rep_x]
    rank_y = ranks[rep_y]
    
    if rep_x == rep_y:
        return
    if rank_x > rank_y:
        parents[rep_y] = rep_x
    elif rank_y > rank_x:
        parents[rep_x] = rep_y
    else:  # rank 같은 경우
        parents[rep_x] = rep_y
        ranks[rep_y] += 1







parents, ranks = make_set(10)

print(parents)
print(ranks)
print()
print(find_set(5))
print()
union(1,5)
print(find_set(5))
print(parents)
print(ranks)
print()

union(5, 10)
print(find_set(10))
print(parents)
print(ranks)
print()


union(1, 9)
print(parents)
print(ranks)
print(ranks[1])