RATE = 12.90
name = ""
while name == "":
  name = input("Please enter customer name: ")
  if name == "":
    print("Name cannot be  .")

previous = -1
while previous < 0:
  previous = float(input("Please enter previous meter reading: "))
  if previous < 0:
    print("Reading cannot be negative")

current = previous - 1
while current < previous:
  current = float(input("Please enter current meter reading: "))
  if current < 0:
    print("Reading cannot be negative")
  elif current < negative:
    print("Reading cannot be less than previous reading")

consumption = current - previous
totalBill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
