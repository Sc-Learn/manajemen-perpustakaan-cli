import json
import sys
import time

# Maksimal percobaan login
MAX_LOGIN = 3

# credetial admin
admin = {
  "username": "123",
  "password": "123"
}

# Mendefinisikan path file JSON
path_buku = "data/buku.json"
path_anggota = "data/anggota.json"
path_peminjaman = "data/peminjaman.json"

# Membaca data buku dari file JSON
with open(path_buku) as f:
    buku = json.load(f)

# Membaca data anggota dari file JSON
with open(path_anggota) as f:
    anggota = json.load(f)

# Membaca data peminjaman dari file JSON
with open(path_peminjaman) as f:
    peminjaman = json.load(f)

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
  username = input("> Username: ")
  password = input("> Password: ")
  
  if username == admin["username"] and password == admin["password"]:
    user_login = True
    
    print(f'\nLogin berhasil! Selamat datang {username}')
    loading(0.1, "Menuju menu utama")
    clear(8 if max_login == MAX_LOGIN else 10)
    
    menu_utama()
  else:
    clear(3 if max_login == MAX_LOGIN else 5)
    
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
  print(f'{"="*56}\n= {" Menu Kelola Buku":^52} =\n{"="*56}')
  print(f'| {"(1) Tambah Buku":<52} |')
  print(f'| {"(2) Lihat Buku":<52} |')
  print(f'| {"(3) Edit Buku":<52} |')
  print(f'| {"(4) Hapus Buku":<52} |')
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
 