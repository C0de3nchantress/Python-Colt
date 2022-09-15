kms = input("How many kilometres do you want to convert: ")
miles =  float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was {miles}mi long")