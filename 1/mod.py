import datetime

a, b, c = map(int, input().split())
d = datetime.date(a, b, c)
n = int(input())
y = datetime.timedelta(days=n)
dx = d + y
print(dx)
