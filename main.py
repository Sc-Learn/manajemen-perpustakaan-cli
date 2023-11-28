import json
import sys
import time
import copy

# Maksimal percobaan login
MAX_LOGIN = 3

# credetial admin
admin = {
  "username": "123",
  "password": "123"
}

# struktur buku
buku = {
  "ISBN": None,
  "judul": None,
  "pengarang": None,
  "penerbit": None,
  "tahun_terbit": None,
  "jumlah_halaman": None,
  "stok": None,
}

# struktur anggota
anggota = {
  "NIM": None,
  "nama": None,
  "jurusan": None,
  "jenis_kelamin": None,
  "no_telepon": None,
  "alamat": None,
}

# struktur peminjaman
peminjaman = {
  "NIM": None,
  "ISBN": None,
  "tanggal_pinjam": None,
  "tanggal_kembali": None,
  "status": None,
  "denda": None,
}
  

# Mendefinisikan path file JSON
path_buku = "data/buku.json"
path_anggota = "data/anggota.json"
path_peminjaman = "data/peminjaman.json"

# Membaca data buku dari file JSON
with open(path_buku) as f:
    list_buku = json.load(f)

# Membaca data anggota dari file JSON
with open(path_anggota) as f:
    list_anggota = json.load(f)

# Membaca data peminjaman dari file JSON
with open(path_peminjaman) as f:
    list_peminjaman = json.load(f)

# Fungsi utama
def main():
  # Menampilkan selamat datang dan judul program
  print("="*56)
  print(f'= {"Selamat Datang di Program Perpustakaan":^52} =')
  print("="*56)
  print(f'= {"Silahkan Login terlebih dahulu":^52} =')
  print("="*56, end="\n")
  
  login(MAX_LOGIN)

# Fungsi clear terminal
def clear(jumlah_line_yang_dihapus = 1):
  for _ in range(jumlah_line_yang_dihapus):
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

# Fungsi loading
def loading(waktu_loading = 1, teks_loading = "Loading"):
  for i in range(1, 101):
    print(f'\r{teks_loading}: {i}%', end="")
    time.sleep(waktu_loading / 100)
  print()

# Fungsi keluar aplikasi
def keluar_aplikasi():
  print("Terima kasih telah menggunakan program ini")
  time.sleep(2)
  clear(20)
  sys.exit()

# Fungsi login
def login(max_login = 3):
  global user_login
  username = input("\n> Username: ")
  password = input("> Password: ")
  
  if username == admin["username"] and password == admin["password"]:
    user_login = True
    
    print(f'\nLogin berhasil! Selamat datang {username}')
    loading(0.1, "Menuju menu utama")
    clear(9 if max_login == MAX_LOGIN else 12)
    
    menu_utama()
  else:
    clear(3 if max_login == MAX_LOGIN else 6)
    
    print("!"*56)
    print(f'!! {"Username atau Password salah":^50} !!')
    print("!"*56)

    login(max_login - 1) if max_login > 1 else sys.exit("Terlalu banyak percobaan login")

# Fungsi menampilkan menu utama
def menu_utama(error = False):
  print(f'{"="*56}\n= {" Menu Utama":^52} =\n{"="*56}')
  print(f'| {"(1) Kelola Buku":<52} |')
  print(f'| {"(2) Kelola Anggota":<52} |')
  print(f'| {"(3) Kelola Peminjaman dan Pengembalian":<52} |')
  print(f'| {"(4) Keluar Aplikasi":<52} |')
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-4): ")
  
  if pilihan == "1":
    clear(14 if error else 10)
    menu_kelola_buku()
  elif pilihan == "2":
    clear(14 if error else 10)
    menu_kelola_anggota()
  elif pilihan == "3":
    clear(14 if error else 10)
    menu_kelola_peminjaman_dan_pengembalian()
  elif pilihan == "4":
    keluar_aplikasi()
  else:
    clear(13 if error else 9)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_utama(error=True)

# Fungsi menampilkan menu kelola buku
def menu_kelola_buku(error = False):
  print(f'{"="*56}\n= {"Menu Kelola Buku":^52} =\n{"="*56}')
  print(f'| {"(1) Tambah Buku":<52} |')
  print(f'| {"(2) Lihat Buku":<52} |')
  print(f'| {"(3) Edit Buku":<52} |')
  print(f'| {"(4) Hapus Buku":<52} |')
  print(f'| {"(5) Kembali Ke Menu Utama":<52} |')
  print(f'| {"(6) Keluar Aplikasi":<52} |')
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-6): ")
  
  if pilihan == "1":
    clear(16 if error else 12)
    menu_tambah_buku()
  elif pilihan == "2":
    pass
  elif pilihan == "3":
    pass
  elif pilihan == "4":
    pass
  elif pilihan == "5":
    clear(16 if error else 12)
    menu_utama()
  elif pilihan == "6":
    keluar_aplikasi()
  else:
    clear(15 if error else 11)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_kelola_buku(error=True)
    
buku_baru = buku.copy()
def menu_tambah_buku(error = False):
  global buku_baru

  print(f'{"="*56}\n= {"Tambah Buku":^52} =\n{"="*56}\n')
  if buku_baru["judul"] == None:
    judul = input("> Judul: ")
    if judul == "":
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"Judul tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(9 if error else 5)
      buku_baru["judul"] = judul
      menu_tambah_buku(error=False)
  else:
    print("Judul:", buku_baru["judul"])
    
  if buku_baru["ISBN"] == None:
    isbn = input("> ISBN: ")
    if isbn == "":
      clear(9 if error else 5)
      print("!"*56)
      print(f'!! {"ISBN tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(10 if error else 6)
      buku_baru["ISBN"] = isbn
      menu_tambah_buku(error=False)
  else:
    print("ISBN:", buku_baru["ISBN"])
  
  if buku_baru["pengarang"] == None:
    pengarang = input("> Pengarang: ")
    if pengarang == "":
      clear(10 if error else 6)
      print("!"*56)
      print(f'!! {"Pengarang tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(11 if error else 7)
      buku_baru["pengarang"] = pengarang
      menu_tambah_buku(error=False)
  else:
    print("Pengarang:", buku_baru["pengarang"])
  
  if buku_baru["penerbit"] == None:
    penerbit = input("> Penerbit: ")
    if penerbit == "":
      clear(11 if error else 7)
      print("!"*56)
      print(f'!! {"Penerbit tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(12 if error else 8)
      buku_baru["penerbit"] = penerbit
      menu_tambah_buku(error=False)
  else:
    print("Penerbit:", buku_baru["penerbit"])
  
  if buku_baru["tahun_terbit"] == None:
    tahun_terbit = input("> Tahun Terbit: ")
    if tahun_terbit == "":
      clear(12 if error else 8)
      print("!"*56)
      print(f'!! {"Tahun Terbit tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(13 if error else 9)
      buku_baru["tahun_terbit"] = tahun_terbit
      menu_tambah_buku(error=False)
  else:
    print("Tahun Terbit:", buku_baru["tahun_terbit"])
  
  if buku_baru["jumlah_halaman"] == None:
    jumlah_halaman = input("> Jumlah Halaman: ")
    if jumlah_halaman == "":
      clear(13 if error else 9)
      print("!"*56)
      print(f'!! {"Jumlah Halaman tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(14 if error else 10)
      buku_baru["jumlah_halaman"] = jumlah_halaman
      menu_tambah_buku(error=False)
  else:
    print("Jumlah Halaman:", buku_baru["jumlah_halaman"])
      
  if buku_baru["stok"] == None:
    stok = input("> Stok: ")
    if stok == "":
      clear(14 if error else 10)
      print("!"*56)
      print(f'!! {"Stok harus diisi":^50} !!')
      print("!"*56)
      
      menu_tambah_buku(error=True)
    else:
      clear(15 if error else 11)
      buku_baru["stok"] = stok
      menu_tambah_buku(error=False)
  else:
    print("Stok:", buku_baru["stok"])

  simpan = input("\n> Simpan buku (y/n): ").lower()
  
  if simpan == "y":
    list_buku.append(buku_baru)
    with open(path_buku, "w") as f:
      json.dump(list_buku, f)
      
    print("\nBuku berhasil disimpan!")
    time.sleep(1)
    
    clear(16 if error else 12)
    
    tambah_lagi = input("\n> Tambah buku lagi (y/n): ").lower()
    buku_baru = buku.copy()
    clear(5)
    
    if tambah_lagi == "y":
      menu_tambah_buku(error=False)
    else:
      menu_kelola_buku(error=False)
  else:
    print("\nBatal!\n")
    buku_baru = buku.copy()
    
    loading(1, "Menuju menu kelola buku")

    clear(21 if error else 17)

    menu_kelola_buku(error=False)

# Fungsi menampilkan menu kelola anggota
def menu_kelola_anggota(error = False):
  print(f'{"="*56}\n= {" Menu Kelola Anggota":^52} =\n{"="*56}')
  print(f'| {"(1) Tambah Anggota":<52} |')
  print(f'| {"(2) Lihat Anggota":<52} |')
  print(f'| {"(3) Edit Anggota":<52} |')
  print(f'| {"(4) Hapus Anggota":<52} |')
  print(f'| {"(5) Kembali Ke Menu Utama":<52} |')
  print(f'| {"(6) Keluar Aplikasi":<52} |')
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-6): ")
  
  if pilihan == "1":
    pass
  elif pilihan == "2":
    pass
  elif pilihan == "3":
    pass
  elif pilihan == "4":
    pass
  elif pilihan == "5":
    clear(16 if error else 12)
    menu_utama()
  elif pilihan == "6":
    keluar_aplikasi()
  else:
    clear(15 if error else 11)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_kelola_buku(error=True)

# Fungsi menampilkan menu kelola peminjaman dan pengembalian
def menu_kelola_peminjaman_dan_pengembalian(error = False):
  print(f'{"="*56}\n= {" Menu Kelola Peminjaman dan Pengembalian":^52} =\n{"="*56}')
  print(f'| {"(1) Pinjam Buku":<52} |')
  print(f'| {"(2) Kembalikan Buku":<52} |')
  print(f'| {"(3) Lihat Buku yang dipinjam":<52} |')
  print(f'| {"(4) Lihat Riwayat Peminjaman":<52} |')
  print(f'| {"(5) Kembali Ke Menu Utama":<52} |')
  print(f'| {"(6) Keluar Aplikasi":<52} |')
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-6): ")
  
  if pilihan == "1":
    pass
  elif pilihan == "2":
    pass
  elif pilihan == "3":
    pass
  elif pilihan == "4":
    pass
  elif pilihan == "5":
    clear(16 if error else 12)
    menu_utama()
  elif pilihan == "6":
    keluar_aplikasi()
  else:
    clear(15 if error else 11)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_kelola_buku(error=True)


# Menjalankan program
main()