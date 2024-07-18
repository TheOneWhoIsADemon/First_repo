print("ЛАСКАВО ПРОСИМО")

n = 5000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

print(hours)
print(minutes)
print(seconds)
