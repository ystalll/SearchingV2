library = {}

def input_data():
    for i in range(5):
        penulis = input(f"Masukkan nama penulis ke-{i+1}: ")
        buku = []
        for j in range(3):
            judul_buku = input(f"Masukkan judul buku ke-{j+1} dari {penulis}: ")
            buku.append(judul_buku)
        library[penulis] = buku
    print("Data telah dimasukkan!")

def search_data():
    penulis_cari = input("Masukkan nama penulis yang ingin dicari: ")
    if penulis_cari in library:
        print(f"Buku-buku dari {penulis_cari}:")
        for buku in library[penulis_cari]:
            print(f"- {buku}")
    else:
        print(f"Penulis {penulis_cari} tidak ditemukan!")

while True:
    print("Menu Perpustakaan")
    print("1. Masukkan Data Penulis dan Bukunya ")
    print("2. Cari Data Penulis")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        input_data()
    elif pilihan == "2":
        search_data()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid, coba lagi.")