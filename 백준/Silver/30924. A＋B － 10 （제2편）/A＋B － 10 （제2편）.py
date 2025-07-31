import random
x = list(range(1, 10001))
random.shuffle(x)

for i in x:
    print(f"? A {i}", flush=True)
    resp = int(input())
    if resp == 1: a = i; break
for i in x:
    print(f"? B {i}", flush=True)
    resp = int(input())
    if resp == 1: b = i; break
print(f"! {a + b}")