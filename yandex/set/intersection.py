def main():
    s = set()
    n = int(input())
    for i in range(n):
        if i == 0:
            s = set(map(int, input().split()))
        else:
            s = s.intersection(set(map(int, input().split())))
            print(s)
    print(len(s))


if __name__ == "__main__":
    main()
