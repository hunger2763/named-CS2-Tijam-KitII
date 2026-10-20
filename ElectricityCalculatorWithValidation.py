RATE = 12.90
name = ""
while name.strip() == "":
  name = input("Please enter customer name: ")
  if name == "":
    print("Name cannot be  .")

previous = -1
while previous.isdigit() < 0:
  previous = float(input("Please enter previous meter reading: "))
  if previous < 0:
    print("Reading cannot be negative")

current = previous - 1
while current.isdigit() < previous:
  current = float(input("Please enter current meter reading: "))
  if current < 0:
    print("Reading cannot be negative")
  if current < previous:
    print("Reading cannot be less than previous reading")

consumption = current - previous
totalBill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(totalBill, 2))
