import getpass

print("program login polda")
print("----------------------")

username_1 = input("buat username anda: ")
password_1 = input("buat password anda: ")
print("\n----------DATA DIKONFIRMASI---------")

username_2 = input("\n masukan username anda: ")
password_2 = getpass.getpass("masukan kata sandi: ")

if username_2 == username_1 and password_2 == password_1:
    print("-------------------------------------------------")
    print("Login diterima, selamat datang " + username_1 + "..")
    print("-------------------------------------------------")
else: 
    print("-------------------------------------------------")
    print("Login ditolak, silahkan coba lagi ")
    print("-------------------------------------------------")

from prettytable import PrettyTable

tabel = PrettyTable()
tabel.tittle = "Pendataan Laporan kasus"
tabel.field_names = ["Nomor Kasus", "Jenis Kasus", "Nama Pelapor", "Tanggal Pelaporan"]

tabel.add_row(["123401", "Pembunuhan berencana", "Obama", "10/10/2024"])
tabel.add_row(["123402", "korupsi", "Oggy", "12/10/2024"])
tabel.add_row(["123403", "Penganiayaan", "Nisa", "13/10/2024"])
tabel.add_row(["123404", "Begal", "Osamu", "15/10/2024"])

print(tabel)

# create
list_kasus = []
def tampilkan_tabel(list_kasus):
    tabel = PrettyTable()
    tabel.field_names = ["Nomor Kasus", "Jenis Kasus", "Nama Pelapor", "Tanggal Pelaporan"]
    for kasus in list_kasus:
        tabel.add_row(["nomor"], kasus["jenis"], kasus["pelapor"], kasus["tanggal"])
    print(tabel)

def tambah_kasus():
    nomor_kasus = input("Masukan nomor kasus: ")
    jenis_kasus = input("Masukan jenis kasus: ")
    nama_pelapor = input("Masukan nama pelapor: ")
    tanggal_pelaporan = input("Masukan tanggal pelaporan")
    list_kasus.append({"nomor kasus": nomor_kasus, "jenis kasus": jenis_kasus, "nama pelapor": nama_pelapor, "tanggal pelaporan": tanggal_pelaporan})
    print(f"kasus dengan nomor {nomor_kasus} telah di tambahkan")

# update
def update_kasus():
    nomor_kasus = input("Masukan nomor kasus yang ingin anda update: ")
    for kasus in list_kasus:
        if nomor_kasus == kasus["nomorkasus"]:
            kasus["jenis kasus"] = input(f"jenis kasus baru")
            kasus["nama pelapor"] = input(f"nama pelapor baru")
            kasus["tanggal pelaporan"] = input(f"tanggal pelaporan baru")
            print(f"kasus dengan nomor{nomor_kasus} telah di update")
            return
    print("kasus tidak ditemukan")

# delete
def hapus_kasus():
    nomor_kasus = input("masukan nomor kasus yang ingin anda hapus: ")
    for kasus in list_kasus:
        if kasus["nomor kasus"] == nomor_kasus:
            list_kasus.pop(kasus)
            print(f"kasus dengan nomor {nomor_kasus} berhasil di hapus")
            return
        print("kasus tidak ditemukan")

# menu utama
def main():
    while True:
        print("\n===Menu===")
        print("1.tampilkan tabel")
        print("2.tambah kasus")
        print("3.update kasus")
        print("4.hapus kasus")
        print("5.keluar")

        pilihan = input("silahkan pilih menu: ")
        if pilihan == "1":
            tampilkan_tabel(list_kasus)
        elif pilihan == "2":
            tambah_kasus()
        elif pilihan == "3":
            update_kasus()
        elif pilihan == "4":
            hapus_kasus()
        elif pilihan == "5":
            print("Program Selesai")
            break
        else:
            print("pilihan tidak tersedia")

main()