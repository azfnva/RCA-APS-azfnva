from kalkulator import Kalkulator

print("=== Kalkulator Sederhana ===")
print("1. Tambah")
print("2. Kurangi")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilih operasi (1-4): ")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print("Hasil:", Kalkulator.tambah(a, b))
elif pilihan == "2":
    print("Hasil:", Kalkulator.kurangi(a, b))
elif pilihan == "3":
    print("Hasil:", Kalkulator.kali(a, b))
elif pilihan == "4":
    try:
        print("Hasil:", Kalkulator.bagi(a, b))
    except ValueError as e:
        print("Error:", e)
else:
    print("Pilihan tidak valid!")