#Shipping Cost Calculator

##Input package weighte and Shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

##Calculate Shipping cost 
shipping_cost = weight * rate

## Display the result 
print(f"Shipping Cost: {shipping_cost} USD")
