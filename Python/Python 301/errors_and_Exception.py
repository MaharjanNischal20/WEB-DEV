num = input("Enter a number")

try:
    num = int(num)

except Exception:
    num = "unknown"

print(num)
