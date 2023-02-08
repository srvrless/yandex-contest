n = 3
x = 19
t = 32
sculptures = [36, 10, 72, 4, 50]

sculpt = sorted(sculptures, key=lambda s: abs(s - x))
min_diff = abs(sculpt[0] - x)
s = [n for n in sculpt if abs(n - x) <= min_diff or abs(n - x) >= min_diff]


def react_new_year():
    count = t
    count1 = 0
    for i in s:
        if i > x:
            count -= (i - count)
            count1 += 1
        if i <= x:
            count -= (i + count)
            count1 += 1

        count1 += 1
        if count <= 0:
            break
    return count1  # Возвращает сколько скульптур будет готово


happy_new_year = react_new_year()


def find_indices():
    genadiy = s[:react_new_year()]
    return [i + 1 for i, n in enumerate(sculptures) if n in genadiy]
