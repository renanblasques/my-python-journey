freq = float(input())
p1 = float(input())
p2 = float(input())
work = float(input())

ms = 0.4 * p1 + 0.4 * p2 + 0.2 * work

if ms >= 5 and freq >= 0.7:
    mf = ms
    print(f"Aprovado com média final {mf:.1f}")
elif ms >= 3 and freq >= 0.7:
    mr = float(input())
    if mr > (10 - ms):
        mf = (ms + mr) / 2
    elif mr >= 5 and mr <= (10 - ms):
        mf = 5
    else:
        mf = ms
    if mf >= 5:
        print(f"Aprovado com média final {mf:.1f}")
    else:
        print(f"Reprovado com média final {mf:.1f}")
else:
    mf = ms
    print(f"Reprovado com média final {mf:.1f}")