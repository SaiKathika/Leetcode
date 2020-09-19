def getHint(secret, guess):
    bulls = cows = 0
    s, g = secret, guess

    for i, j in zip(secret, guess):
        if i == j:
            bulls += 1
            s = s.replace(i, '', 1)
            g = g.replace(i, '', 1)
    print(s, g)
    for i in s:
        if i in g:
            cows += 1
            g = g.replace(i, '', 1)

    return f'{bulls}A{cows}B'

print(getHint("1122", "0001"))