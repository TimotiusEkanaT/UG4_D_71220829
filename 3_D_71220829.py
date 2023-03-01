def cari_kata_terpanjang(kalimat):
    kata_terpanjang = max(kalimat.split(" "))
    return kata_terpanjang

aiojgas = input("Masukkan sebuah kalimat: ")
barbnetmj = cari_kata_terpanjang(aiojgas)
print("Kata terpanjang dalam kalimat adalah:", barbnetmj)
