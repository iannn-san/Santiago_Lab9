g_items = []
g_prices = []

for i in range(5):
    name = input(f"enter name of grocery item {i + 1}: ")
    price = float(input(f"enter the price of {name}: "))
    g_items.append(name)
    g_prices.append(price)

averagep = sum(g_prices) / len(g_prices)

print(f"\naverage price of the grocery items is: {averagep:.2f}")

print("\ngrocery items with prices above/equal to average:")
for i in range(5):
    if g_prices[i] >= averagep:
        print(f"this {g_items[i]} has (₱{g_prices[i]:.2f})")