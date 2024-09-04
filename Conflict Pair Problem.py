def max_expertise(n, c, cons, exp):
    dp = [0]*(1<<n)
    con = [0]*n
    for i in range(c):
        con[cons[i][0]-1] |= (1<<(cons[i][1]-1))
        con[cons[i][1]-1] |= (1<<(cons[i][0]-1))
    for mask in range(1, 1<<n):
        not_in_mask = ((1<<n)-1)^mask
        for i in range(n):
            if (mask>>i)&1:
                new_mask = mask^(1<<i)
                if (not_in_mask & con[i]) == 0:
                    dp[mask] = max(dp[mask], dp[new_mask] + exp[i])
    return max(dp)

n, c = map(int, input().split())
cons = [list(map(int, input().split())) for _ in range(c)]
exp = list(map(int, input().split()))
print(max_expertise(n, c, cons, exp))



