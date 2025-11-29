def main():
    s = set()
    n = int(input())
    for _ in range(n):
        s.update(list(map(int, input().split())))
    print(len(s))


if __name__ == "__main__":
    main()
