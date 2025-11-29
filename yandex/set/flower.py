def main():
    n = int(input())
    sets = [None for _ in range(n)]
    for i in range(n):
        sets[i] = set(map(int, input().split()[1:]))
    if n < 2:
        print("NO")
        return

    C = sets[0].intersection(sets[1])
    P_lengths = []
    if len(C) >= 1:
        for i in range(n):
            if C.intersection(sets[i]) != C:
                print("NO")
                return
        for idx in range(n):
            next_idx = idx + 1 if idx < n - 1 else 0
            P_1 = sets[idx] - C
            P_2 = sets[next_idx] - C
            P_lengths.append(len(P_1))
            if len(P_1.intersection(P_2)) > 0:
                print("NO")
                return
    print("YES")
    print(len(C))
    print(*P_lengths)


if __name__ == "__main__":
    main()
