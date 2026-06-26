n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
total_price = sum(product['price'] for product in products)
print(total_price)
