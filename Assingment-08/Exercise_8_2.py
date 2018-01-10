print("Please insert a valid german PLZ")
isZipCode = input()
y = int(isZipCode)

if y in range(73000,99999):
        print("This PLZ is located in the South of Germany")
else:
        print("This PLZ isn't located in the South of Germany")
