a = b = 1
while True:
    print(f"? A {a}", flush=True)
    resp = int(input())
    if resp == 1: break
    a += 1
while True:
    print(f"? B {b}", flush=True)
    resp = int(input())
    if resp == 1: break
    b += 1
print(f"! {a + b}")