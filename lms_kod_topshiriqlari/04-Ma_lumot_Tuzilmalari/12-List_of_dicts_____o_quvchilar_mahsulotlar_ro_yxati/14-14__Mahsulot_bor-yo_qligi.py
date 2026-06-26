n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
if any(product['name'] == x for product in products):
    print("YES")
else:
    print("NO")