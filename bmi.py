# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_float=float(height)
weight_float=float(weight)
bmi=weight_float/(height_float**2)
bmi_int=int(bmi)
print(bmi_int)