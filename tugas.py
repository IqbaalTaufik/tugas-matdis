def inputNumb ():
    while True:
        try:
            angka = int(input("masukkan nominal uang :"(inputan)))
        except ValueError:
            print("nilai masukkan harus nilai bulat")
            continue
        else:
            return angka
            break

#program utama
nilai = int(input("masukkan nominal uang :"))
if (nilai < 0):
    print("angka tidak boleh negatif")
else:
    hasil = nilai % 100000
    hasil1 = nilai // 100000
    print(hasil1,"jumlah pecahan Rp. 100.000")

    hasil2 = hasil % 50000
    hasil3 = hasil // 50000
    print(hasil3,"jumlah pecahan Rp. 50.000")

    hasil4 = hasil2 % 20000
    hasil5 = hasil2 // 20000
    print(hasil5,"jumlah pecahan Rp. 20.000")

    hasil6 = hasil4 % 10000
    hasil7 = hasil4 // 10000
    print(hasil7,"jumlah pecahan Rp. 10.000")

    hasil8 = hasil6 % 5000
    hasil9 = hasil6 // 5000
    print(hasil9,"jumlah pecahan Rp. 5.000")

    hasil10 = hasil8 % 2000
    hasil11 = hasil8 // 2000
    print(hasil11,"jumlah pecahan Rp. 2.000")

    hasil12 = hasil10 % 1000
    hasil13 = hasil10 // 1000
    print(hasil13,"jumlah pecahan Rp. 1.000")

    hasil14 = hasil12 % 500
    hasil15 = hasil12 // 500
    print(hasil15,"jumlah pecahan Rp. 500")

    hasil16 = hasil14 % 100
    hasil17 = hasil14 // 100
    print(hasil17,"jumlah pecahan Rp. 100")
    print("")
    print(hasil16,"sisa uang")
