# projek python
while True:
    print("Apakah anda Pembeli atau Penjual ? ")
    openp = str(input())
    if openp in ["Pembeli", "Pembeli"]:
        print("="*60)
        print("\tSelamat Datang Di Toko furniture\n\t\tSelamat Berbelanja")
        print("="*60)
        print("↓ Tulis Nomor Dibawah Ini Untuk Melakukan Aksi ↓ ")
        print("1. Melihat Tampilan Barang\n2. Mencari Barang\n3. Keluar Aplikasi")
        aksi_beli = int(input("➥  "))
        if aksi_beli == 1:
            with open("Deskripsiread.txt", 'r') as f:
                baca_brng = f.read()
                print(baca_brng)

        # elif aksi_beli == 2:

        elif aksi_beli == 3:
            break
        else:
            print('Inputan salah, Coba lagi')

    elif openp in ["Penjual", "Penjual"]:
        print("="*60)
        print("\tSelamat Datang Penjual Terhormat")
        print("="*60)
        print("↓ Tulis Nomor Dibawah Ini Untuk Melakukan Aksi ↓")
        print("1. Menambah/ menjual barang\n2. Keluar Aplikasi")
        aksi_jual = int(input('➥  '))
        if aksi_jual == 1:
            f = open('Deskripsiread.txt', 'a')
            nama_brng = str(input('Masukkan Nama Barang : '))
            harga_brng = int(input('Masukkan Harga Barang : '))
            material_brng = str(input('Masukkan Material Barang : '))
            deskrip_read = "\nNama Barang : {}\nHarga Barang : {}\nMaterial : {}\n".format(
                nama_brng, harga_brng, material_brng)
            f.write("="*60)
            f.write(deskrip_read)
            f.close()

            with open('deskripsi.txt', 'a') as file:
                deskrip_baru = "{},{},{}, \n".format(
                    nama_brng, harga_brng, material_brng)
                file.write(deskrip_baru)
            keluar2 = str(
                input("Apakah Anda Ingin Kembali Ke Halaman Utama?(Ya/Tidak) : "))
            if keluar2 in ["Ya", "ya", "y"]:
                print('Data Akan Disimpan Setelah Keluar Aplikasi')
                continue
            else:
                print('Data Sudah Dismpan')
                break
        elif aksi_jual == 2:
            print('no')
        elif aksi_jual == 3:
            pass
        else:
            print('Inputan salah, Coba lagi')
    else:
        print("Input salah, Masukkan jawaban dengan benar")
