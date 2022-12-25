print(" SATE KARI'AM ".center(60, "*"))
print("-".center(60, '-'))
print("Kode             Jenis Sate              Harga per Tusuk")
print("-".center(60, '-'))
print("A                Sate Ayam               Rp. 1.000")
print("K                Sate Kambing            Rp. 1.500")
print("S                Sate Sapi               Rp. 2.000")
print("-".center(60, '-'))

banyakSate = int(input("\nMau beli berapa jenis sate : "))

kodeSate    = []
banyakTusuk = []

for i in range(banyakSate) :
    print("\nData ke - ", i+1)
    kode1 = input("Kode Sate [A/K/S] : ")
    kodeSate.append(kode1)
    
    lanjut = input("\nApakah Sudah yakin dengan kode yang di input?\nIngin Lanjut? [Y/N] : ")
    if lanjut == "n" or lanjut == "N" :
        break

    kode2 = int(input("Banyak Tusuk : "))
    banyakTusuk.append(kode2)

print(" SATE KARI'AM ".center(60, "*"))
print("-".center(60, '-'))
print("NO.    Jenis            Harga        Banyak     Jumlah")
print("       Sate             per tusuk    Tusuk      Harga")
print("-".center(60, '-'))

total = 0
for a in range(banyakSate) :
    if (kodeSate[a] == "a" or kodeSate[a] == "A"):
        jenisSate = "Sate Ayam   "
        harga = 1000
    elif (kodeSate[a] == "k" or kodeSate[a] == "K"):
        jenisSate = "Sate Kambing"
        harga = 1500
    elif (kodeSate[a] == "s" or kodeSate[a] == "S"):
        jenisSate = "Sate Sapi   "
        harga = 2000
    else :
        jenisSate = "Kode Invalid. Kode yang tersedia [A/K/S], Silakan Coba input ulang"
        harga = 0

    subTotal = harga * banyakTusuk[a]
    total = total + subTotal
    print(a+1, "    ", jenisSate, "   ", harga, "        ", banyakTusuk[a], "       Rp.", subTotal)

if total > 50000 :
    diskon = 0.1 * total
else :
    diskon = 0

totalBayar = total - diskon


print("-".center(60, '-'))
print("                                 Jumlah Bayar : Rp. ", total)
print("                                 Diskon 10%   : Rp. ", diskon)
print("                                 Total Bayar  : Rp. ", totalBayar)