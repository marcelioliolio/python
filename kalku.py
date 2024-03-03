def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa dibagi dengan nol"

#masukkan input
operasi = input("Masukkan operasi bilangan (+, -, *, /): ")
num1 = float(input("Masukkan nilai pertama: "))
num2 = float(input("Masukkan nilai kedua: "))

#operasi perhitungan
if operasi == "+":
    hasil = add(num1, num2)
elif operasi == "-":
    hasil = subtract(num1, num2)
elif operasi == "*":
    hasil = multiply(num1, num2)
elif operasi == "/":
    hasil = divide(num1, num2)
else:
    hasil = "Operasi bilangan tidak valid"

#Print hasil
print(f"Hasil: {hasil}")
