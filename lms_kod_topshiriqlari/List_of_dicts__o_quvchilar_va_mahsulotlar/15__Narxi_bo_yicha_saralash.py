n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
products.sort(key=lambda x: x['price'])
for p in products:
    print(p['name'],p['price'])
