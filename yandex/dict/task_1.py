def main():
    n = int(input())
    result = {}
    for _ in range(n):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            result[inp[1]] = inp[2]
        else:
            x = result.get(inp[1], -1)
            print(x)


if __name__ == "__main__":
    main()
