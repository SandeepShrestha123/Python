# <20 → Left-align the text in a field of 20 characters.
# <10 → Left-align the text in a field of 10 characters.

products = {
    "milk": 50,
    "cheese": 100,
    "lays": 200,
    "cheese balls": 50,
    "bread": 60,
    "egg": 15
}

print("========== Available Products ==========")
for product, price in products.items():
    print(f"{product} : Rs. {price}")

n = int(input("\nEnter the number of products you want to buy: "))

p = []

for i in range(n):
    name = input("Enter product name: ").lower()
    if name in products:
        quantity = int(input("Enter quantity: "))
        price = products[name]
        total = price * quantity
        p.append([name.title(), price, quantity, total])
    else:
        print("Product not available!")

print("\n----------------------------------------------------------")
print(f"{'Name':<20}{'Price':<10}{'Quantity':<10}{'Total':<10}")
print("----------------------------------------------------------")

for item in p:
    print(f"{item[0]:<20}{item[1]:<10}{item[2]:<10}{item[3]:<10}")

print("----------------------------------------------------------")

grand_total = 0
for item in p:
    grand_total += item[3]

print(f"{'Total Bill':<40}Rs. {grand_total}")
print("----------------------------------------------------------")
