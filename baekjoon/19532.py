import sys

def soluation(a:int, b:int, c:int, d: int, e:int, f:int) -> (int, int):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
                return x,y

if __name__ == "__main__":
    a,b,c,d,e,f = map(int, sys.stdin.readline().strip().split())
    x, y = soluation(a,b,c,d,e,f)
    print(f"{x} {y}")