f=open('../inputs/5.in').read().split('\n')
for w in f:
    a,b=[-float(x.strip('-')[::-1]) if '-' in x else float(x[::-1]) for x in w.split(' ')]
    print(a if a>b else b)