print("Please insert a valid german PLZ")
isZipCode = input()
y = int(isZipCode)

if y in range(10000,99999):
        print("True")
else:
        print("False")

