import json
import sys
import time
import datetime

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
  clear(50)
  sys.exit()

# Fungsi login
def login(max_login = 3):
  global user_login
  username = input("\n> Username: ")
  password = input("> Password: ")
  
  if username == admin["username"] and password == admin["password"]:
    user_login = True
    
    print(f'\nLogin berhasil! Selamat datang {username}')
    loading(1.5, "Menuju menu utama")
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
    clear(16 if error else 12)
    menu_lihat_buku()
  elif pilihan == "3":
    clear(16 if error else 12)
    menu_edit_buku()
  elif pilihan == "4":
    clear(16 if error else 12)
    menu_hapus_buku()
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
# Fungsi menambahkan buku
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
      try:
        stok = int(stok)
      except:
        clear(14 if error else 10)
        print("!"*56)
        print(f'!! {"Stok harus berupa angka":^50} !!')
        print("!"*56)
        
        menu_tambah_buku(error=True)
      
      clear(15 if error else 11)
      buku_baru["stok"] = stok
      menu_tambah_buku(error=False)
  else:
    print("Stok:", buku_baru["stok"])

  simpan = input("\n> Simpan buku (y/n): ").lower()
  
  if simpan == "y":
    list_buku.insert(0, buku_baru)
    with open(path_buku, "w") as f:
      json.dump(list_buku, f)
      
    print("\nBuku berhasil disimpan!")
    time.sleep(2.5)
    
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

# Fungsi menampilkan buku
def menu_lihat_buku(error = False, halaman = 1):
  print(f'{"="*56}\n= {" List Buku":^52} =\n{"="*56}\n')
  
  total_buku = len(list_buku)
  total_halaman = total_buku // 5 + 1 if total_buku % 5 != 0 else total_buku // 5
  skip = (halaman - 1) * 5
  
  print(f'{"="*148}\n= {" Halaman " + str(halaman) + " dari " + str(total_halaman):^144} =\n{"="*148}')
  print(f'| {"No":^4} | {"ISBN":<13} | {"Judul":<25} | {"Pengarang":<25} | {"Penerbit":<25} | {"Tahun Terbit":^12} | {"Jumlah Halaman":^15} | {"Stok":^4} |')
  print(f'{"="*148}')
  
  for i in range(skip, skip + 5):
    if i < total_buku:
      print(f'| {i+1:<4} | {list_buku[i]["ISBN"]:<13} | {list_buku[i]["judul"]:<25} | {list_buku[i]["pengarang"]:<25} | {list_buku[i]["penerbit"]:<25} | {list_buku[i]["tahun_terbit"]:^12} | {list_buku[i]["jumlah_halaman"]:^15} | {list_buku[i]["stok"]:^4} |')
    else:
      print(f'| {"":<4} | {"":<13} | {"":<25} | {"":<25} | {"":<25} | {"":^12} | {"":<15} | {"":^4} |')
      
  print(f'{"="*148}\n\n{"="*56}')
  
  if halaman > 1:
    print(f'| {"(1) Halaman Sebelumnya":<52} |')
  
  if halaman < total_halaman:
    print(f'| {"(2) Halaman Selanjutnya":<52} |')
    
  print(f'| {"(3) Kembali Ke Menu Kelola Buku":<52} |')
  print(f'| {"(4) Keluar Aplikasi":<52} |')
  
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-4): ")
  
  if pilihan == "1":
    clear(27 if error else 23)

    if halaman > 1:
      menu_lihat_buku(error=False, halaman=halaman-1)
    else:
      menu_lihat_buku(error=False, halaman=halaman)
  elif pilihan == "2":
    clear(27 if error else 23)

    if halaman < total_halaman:
      menu_lihat_buku(error=False, halaman=halaman+1)
    else:
      menu_lihat_buku(error=False, halaman=halaman)
  elif pilihan == "3":
    clear(27 if error else 23)
    menu_kelola_buku()
  elif pilihan == "4":
    keluar_aplikasi()
  else:
    clear(26 if error else 22)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_lihat_buku(error=True, halaman=halaman)

# Fungsi mengedit buku
buku_edit = buku.copy()
def menu_edit_buku(error = False, buku_terpilih = None):
  global buku_edit
  
  print(f'{"="*56}\n= {" Edit Buku":^52} =\n{"="*56}\n')
  
  if buku_terpilih == None:
    isbn = input("> ISBN: ")
    if isbn == "":
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"ISBN tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_edit_buku(error=True)
    else:
      clear(9 if error else 5)
      menu_edit_buku(error=False, buku_terpilih=isbn)
    
  if buku_terpilih != None:
    for i in range(len(list_buku)):
      if list_buku[i]["ISBN"] == buku_terpilih:
        print("ISBN:", list_buku[i]["ISBN"], " | Judul:", list_buku[i]["judul"], " | Pengarang:", list_buku[i]["pengarang"], " | Penerbit:", list_buku[i]["penerbit"], " | Tahun Terbit:", list_buku[i]["tahun_terbit"], " | Jumlah Halaman:", list_buku[i]["jumlah_halaman"], " | Stok:", list_buku[i]["stok"], end="\n\n")
        
        if buku_edit["judul"] == None:
          judul = input("> Judul: ")
          if judul == "":
            clear(10 if error else 6)
            print("!"*56)
            print(f'!! {"Judul tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
          else:
            clear(11 if error else 7)
            buku_edit["judul"] = judul
            menu_edit_buku(error=False, buku_terpilih=buku_terpilih)
        else:
          print("Judul:", buku_edit["judul"])
        
        if buku_edit["pengarang"] == None:
          pengarang = input("> Pengarang: ")
          if pengarang == "":
            clear(11 if error else 7)
            print("!"*56)
            print(f'!! {"Pengarang tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
          else:
            clear(12 if error else 8)
            buku_edit["pengarang"] = pengarang
            menu_edit_buku(error=False, buku_terpilih=buku_terpilih)
        else:
          print("Pengarang:", buku_edit["pengarang"])
          
        if buku_edit["penerbit"] == None:
          penerbit = input("> Penerbit: ")
          if penerbit == "":
            clear(12 if error else 8)
            print("!"*56)
            print(f'!! {"Penerbit tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
          else:
            clear(13 if error else 9)
            buku_edit["penerbit"] = penerbit
            menu_edit_buku(error=False, buku_terpilih=buku_terpilih)
        else:
          print("Penerbit:", buku_edit["penerbit"])
          
        if buku_edit["tahun_terbit"] == None:
          tahun_terbit = input("> Tahun Terbit: ")
          if tahun_terbit == "":
            clear(13 if error else 9)
            print("!"*56)
            print(f'!! {"Tahun Terbit tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
          else:
            clear(14 if error else 10)
            buku_edit["tahun_terbit"] = tahun_terbit
            menu_edit_buku(error=False, buku_terpilih=buku_terpilih)
        else:
          print("Tahun Terbit:", buku_edit["tahun_terbit"])
          
        if buku_edit["jumlah_halaman"] == None:
          jumlah_halaman = input("> Jumlah Halaman: ")
          if jumlah_halaman == "":
            clear(14 if error else 10)
            print("!"*56)
            print(f'!! {"Jumlah Halaman tidak boleh kosong":^50} !!')
            print("!"*56)
          
            menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
          else:
            clear(15 if error else 11)
            buku_edit["jumlah_halaman"] = jumlah_halaman
            menu_edit_buku(error=False, buku_terpilih=buku_terpilih)
        else:
          print("Jumlah Halaman:", buku_edit["jumlah_halaman"])
          
        if buku_edit["stok"] == None:
          stok = input("> Stok: ")
          if stok == "":
            clear(15 if error else 11)
            print("!"*56)
            print(f'!! {"Stok harus diisi":^50} !!')
            print("!"*56)
            
            menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
          else:
            try:
              stok = int(stok)
            except:
              clear(15 if error else 11)
              print("!"*56)
              print(f'!! {"Stok harus berupa angka":^50} !!')
              print("!"*56)
              
              menu_edit_buku(error=True, buku_terpilih=buku_terpilih)
            
            clear(16 if error else 12)
            buku_edit["stok"] = stok
            menu_edit_buku(error=False, buku_terpilih=buku_terpilih)
        else:
          print("Stok:", buku_edit["stok"])
          
        ubah = input("\n> Ubah buku (y/n): ").lower()
        
        if ubah == "y":
          list_buku[i] = buku_edit
          list_buku[i]["ISBN"] = buku_terpilih
          with open(path_buku, "w") as f:
            json.dump(list_buku, f)
            
          print("\nBuku berhasil diubah!")
          time.sleep(2.5)
          
          clear(17 if error else 13)
          
          ubah_lagi = input("\n> Ubah buku lagi (y/n): ").lower()
          buku_edit = buku.copy()
          clear(5)
          
          if ubah_lagi == "y":
            menu_edit_buku(error=False, buku_terpilih=None)
          else:
            menu_kelola_buku(error=False)
        else:
          print("\nBatal!\n")
          buku_edit = buku.copy()
          loading(1, "Menuju menu kelola buku")
          clear(22 if error else 18)
          menu_kelola_buku(error=False)      
  
  print("Buku tidak ditemukan!")
  loading(1, "Menuju menu kelola buku")
  clear(10 if error else 6)
  menu_kelola_buku(error=False)

# Fungsi menghapus buku
def menu_hapus_buku(error = False):
  print(f'{"="*56}\n= {" Hapus Buku":^52} =\n{"="*56}\n')
  
  isbn = input("> ISBN: ")
  if isbn == "":
    clear(8 if error else 4)
    print("!"*56)
    print(f'!! {"ISBN tidak boleh kosong":^50} !!')
    print("!"*56)
    
    menu_hapus_buku(error=True)
  else:
    clear(5 if error else 1)
    
    for i in range(len(list_buku)):
      if list_buku[i]["ISBN"] == isbn:
        print("ISBN:", list_buku[i]["ISBN"], " | Judul:", list_buku[i]["judul"], " | Pengarang:", list_buku[i]["pengarang"], " | Penerbit:", list_buku[i]["penerbit"], " | Tahun Terbit:", list_buku[i]["tahun_terbit"], " | Jumlah Halaman:", list_buku[i]["jumlah_halaman"], " | Stok:", list_buku[i]["stok"], end="\n\n")
        
        hapus = input("\n> Hapus buku (y/n): ").lower()
        
        if hapus == "y":
          list_buku.pop(i)
          with open(path_buku, "w") as f:
            json.dump(list_buku, f)
            
          print("\nBuku berhasil dihapus!")
          time.sleep(2.5)
          
          clear(11 if error else 7)
          
          hapus_lagi = input("\n> Hapus buku lagi (y/n): ").lower()
          clear(5)
          
          if hapus_lagi == "y":
            menu_hapus_buku(error=False)
          else:
            menu_kelola_buku(error=False)
        else:
          print("\nBatal!\n")
          loading(1, "Menuju menu kelola buku")
          clear(16 if error else 12)
          menu_kelola_buku(error=False)
      
  print("Buku tidak ditemukan!")
  loading(1, "Menuju menu kelola buku")
  clear(10 if error else 6)
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
    clear(16 if error else 12)
    menu_tambah_anggota()
  elif pilihan == "2":
    clear(16 if error else 12)
    menu_lihat_anggota()
  elif pilihan == "3":
    clear(16 if error else 12)
    menu_edit_anggota()
  elif pilihan == "4":
    clear(16 if error else 12)
    menu_hapus_anggota()
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
    
# Fungsi menambahkan anggota 
anggota_baru = anggota.copy()
def menu_tambah_anggota(error = False):
  global anggota_baru
  
  print(f'{"="*56}\n= {" Tambah Anggota":^52} =\n{"="*56}\n')
  
  if anggota_baru["NIM"] == None:
    nim = input("> NIM: ")
    if nim == "":
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"NIM tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_anggota(error=True)
    else:
      clear(9 if error else 5)
      anggota_baru["NIM"] = nim
      menu_tambah_anggota(error=False)
  else:
    print("NIM:", anggota_baru["NIM"])
    
  if anggota_baru["nama"] == None:
    nama = input("> Nama: ")
    if nama == "":
      clear(9 if error else 5)
      print("!"*56)
      print(f'!! {"Nama tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_anggota(error=True)
    else:
      clear(10 if error else 6)
      anggota_baru["nama"] = nama
      menu_tambah_anggota(error=False)
      
  else:
    print("Nama:", anggota_baru["nama"])
    
  if anggota_baru["jurusan"] == None:
    jurusan = input("> Jurusan: ")
    if jurusan == "":
      clear(10 if error else 6)
      print("!"*56)
      print(f'!! {"Jurusan tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_anggota(error=True)
    else:
      clear(11 if error else 7)
      anggota_baru["jurusan"] = jurusan
      menu_tambah_anggota(error=False)
  else:
    print("Jurusan:", anggota_baru["jurusan"])
    
  if anggota_baru["jenis_kelamin"] == None:
    jenis_kelamin = input("> Jenis Kelamin: ")
    if jenis_kelamin == "":
      clear(11 if error else 7)
      print("!"*56)
      print(f'!! {"Jenis Kelamin tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_anggota(error=True)
    else:
      clear(12 if error else 8)
      anggota_baru["jenis_kelamin"] = jenis_kelamin
      menu_tambah_anggota(error=False)
  else:
    print("Jenis Kelamin:", anggota_baru["jenis_kelamin"])
    
  if anggota_baru["no_telepon"] == None:
    no_telepon = input("> No Telepon: ")
    if no_telepon == "":
      clear(12 if error else 8)
      print("!"*56)
      print(f'!! {"No Telepon tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_anggota(error=True)
    else:
      clear(13 if error else 9)
      anggota_baru["no_telepon"] = no_telepon
      menu_tambah_anggota(error=False)
  else:
    print("No Telepon:", anggota_baru["no_telepon"])
    
  if anggota_baru["alamat"] == None:
    alamat = input("> Alamat: ")
    if alamat == "":
      clear(13 if error else 9)
      print("!"*56)
      print(f'!! {"Alamat tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_tambah_anggota(error=True)
    else:
      clear(14 if error else 10)
      anggota_baru["alamat"] = alamat
      menu_tambah_anggota(error=False)
  else:
    print("Alamat:", anggota_baru["alamat"])
    
  simpan = input("\n> Simpan anggota (y/n): ").lower()
  
  if simpan == "y":
    list_anggota.insert(0, anggota_baru)
    with open(path_anggota, "w") as f:
      json.dump(list_anggota, f)
      
    print("\nAnggota berhasil disimpan!")
    time.sleep(2.5)
    
    clear(15 if error else 11)
    
    tambah_lagi = input("\n> Tambah anggota lagi (y/n): ").lower()
    anggota_baru = anggota.copy()
    clear(5)
    
    if tambah_lagi == "y":
      menu_tambah_anggota(error=False)
    else:
      menu_kelola_anggota(error=False) 
  else:
    print("\nBatal!\n")
    anggota_baru = anggota.copy()
    loading(1, "Menuju menu kelola anggota")
    clear(21 if error else 17)
    menu_kelola_anggota(error=False)

# Fungsi menampilkan anggota
def menu_lihat_anggota(error = False, halaman = 1):
  print(f'{"="*56}\n= {" List Anggota":^52} =\n{"="*56}\n')
  
  total_anggota = len(list_anggota)
  total_halaman = total_anggota // 5 + 1 if total_anggota % 5 != 0 else total_anggota // 5
  skip = (halaman - 1) * 5
  
  print(f'{"="*134}\n= {" Halaman " + str(halaman) + " dari " + str(total_halaman):^130} =\n{"="*134}')
  print(f'| {"No":^4} | {"NIM":<10} | {"Nama":<25} | {"Jurusan":<20} | {"Jenis Kelamin":<10} | {"No Telepon":<15} | {"Alamat":<25} |')
  print(f'{"="*134}')
  
  for i in range(skip, skip + 5):
    if i < total_anggota:
      print(f'| {i+1:<4} | {list_anggota[i]["NIM"]:<10} | {list_anggota[i]["nama"]:<25} | {list_anggota[i]["jurusan"]:<20} | {list_anggota[i]["jenis_kelamin"]:<13} | {list_anggota[i]["no_telepon"]:<15} | {list_anggota[i]["alamat"]:<25} |')
    else:
      print(f'| {"":<4} | {"":<10} | {"":<25} | {"":<20} | {"":<13} | {"":<15} | {"":<25} |')
      
  print(f'{"="*134}\n\n{"="*56}')
  
  if halaman > 1:
    print(f'| {"(1) Halaman Sebelumnya":<52} |')
    
  if halaman < total_halaman:
    print(f'| {"(2) Halaman Selanjutnya":<52} |')
    
  print(f'| {"(3) Kembali Ke Menu Kelola Anggota":<52} |')
  print(f'| {"(4) Keluar Aplikasi":<52} |')
  
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-4): ")
  
  if pilihan == "1":
    clear(27 if error else 23)

    if halaman > 1:
      menu_lihat_anggota(error=False, halaman=halaman-1)
    else:
      menu_lihat_anggota(error=False, halaman=halaman)
  elif pilihan == "2":
    clear(27 if error else 23)
    
    if halaman < total_halaman:
      menu_lihat_anggota(error=False, halaman=halaman+1)
    else:
      menu_lihat_anggota(error=False, halaman=halaman)
  elif pilihan == "3":
    clear(27 if error else 23)
    menu_kelola_anggota()
  elif pilihan == "4":
    keluar_aplikasi()
  else:
    clear(26 if error else 22)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_lihat_anggota(error=True, halaman=halaman)

# Fungsi mengedit anggota
anggota_edit = anggota.copy()
def menu_edit_anggota(error = False, anggota_terpilih = None):
  global anggota_edit
  
  print(f'{"="*56}\n= {" Edit Anggota":^52} =\n{"="*56}\n')
  
  if anggota_terpilih == None:
    nim = input("> NIM: ")
    if nim == "":
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"NIM tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_edit_anggota(error=True)
    else:
      clear(9 if error else 5)
      menu_edit_anggota(error=False, anggota_terpilih=nim)
    
  if anggota_terpilih != None:
    for i in range(len(list_anggota)):
      if list_anggota[i]["NIM"] == anggota_terpilih:
        print("NIM:", list_anggota[i]["NIM"], " | Nama:", list_anggota[i]["nama"], " | Jurusan:", list_anggota[i]["jurusan"], " | Jenis Kelamin:", list_anggota[i]["jenis_kelamin"], " | No Telepon:", list_anggota[i]["no_telepon"], " | Alamat:", list_anggota[i]["alamat"], end="\n\n")
        
        if anggota_edit["nama"] == None:
          nama = input("> Nama: ")
          if nama == "":
            clear(10 if error else 6)
            print("!"*56)
            print(f'!! {"Nama tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_anggota(error=True, anggota_terpilih=anggota_terpilih)
          else:
            clear(11 if error else 7)
            anggota_edit["nama"] = nama
            menu_edit_anggota(error=False, anggota_terpilih=anggota_terpilih)
        else:
          print("Nama:", anggota_edit["nama"])
        
        if anggota_edit["jurusan"] == None:
          jurusan = input("> Jurusan: ")
          if jurusan == "":
            clear(11 if error else 7)
            print("!"*56)
            print(f'!! {"Jurusan tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_anggota(error=True, anggota_terpilih=anggota_terpilih)
          else:
            clear(12 if error else 8)
            anggota_edit["jurusan"] = jurusan
            menu_edit_anggota(error=False, anggota_terpilih=anggota_terpilih)
        else:
          print("Jurusan:", anggota_edit["jurusan"])
          
        if anggota_edit["jenis_kelamin"] == None:
          jenis_kelamin = input("> Jenis Kelamin: ")
          if jenis_kelamin == "":
            clear(12 if error else 8)
            print("!"*56)
            print(f'!! {"Jenis Kelamin tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_anggota(error=True, anggota_terpilih=anggota_terpilih)
          else:
            clear(13 if error else 9)
            anggota_edit["jenis_kelamin"] = jenis_kelamin
            menu_edit_anggota(error=False, anggota_terpilih=anggota_terpilih)
        else:
          print("Jenis Kelamin:", anggota_edit["jenis_kelamin"])
          
        if anggota_edit["no_telepon"] == None:
          no_telepon = input("> No Telepon: ")
          if no_telepon == "":
            clear(13 if error else 9)
            print("!"*56)
            print(f'!! {"No Telepon tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_anggota(error=True, anggota_terpilih=anggota_terpilih)
          else:
            clear(14 if error else 10)
            anggota_edit["no_telepon"] = no_telepon
            menu_edit_anggota(error=False, anggota_terpilih=anggota_terpilih)
        else:
          print("No Telepon:", anggota_edit["no_telepon"])
          
        if anggota_edit["alamat"] == None:
          alamat = input("> Alamat: ")
          if alamat == "":
            clear(14 if error else 10)
            print("!"*56)
            print(f'!! {"Alamat tidak boleh kosong":^50} !!')
            print("!"*56)
            
            menu_edit_anggota(error=True, anggota_terpilih=anggota_terpilih)
          else:
            clear(15 if error else 11)
            anggota_edit["alamat"] = alamat
            menu_edit_anggota(error=False, anggota_terpilih=anggota_terpilih)
        else:
          print("Alamat:", anggota_edit["alamat"])
          
        ubah = input("\n> Ubah anggota (y/n): ").lower()
        
        if ubah == "y":
          list_anggota[i] = anggota_edit
          list_anggota[i]["NIM"] = anggota_terpilih
          with open(path_anggota, "w") as f:
            json.dump(list_anggota, f)
            
          print("\nAnggota berhasil diubah!")
          time.sleep(2.5)
          
          clear(16 if error else 12)
          
          ubah_lagi = input("\n> Ubah anggota lagi (y/n): ").lower()
          anggota_edit = anggota.copy()
          clear(5)
          
          if ubah_lagi == "y":
            menu_edit_anggota(error=False, anggota_terpilih=None)
          else:
            menu_kelola_anggota(error=False)
        else:
          print("\nBatal!\n")
          anggota_edit = anggota.copy()
          loading(1, "Menuju menu kelola anggota")
          clear(22 if error else 18)
          menu_kelola_anggota(error=False)
          
  print("Anggota tidak ditemukan!")
  loading(1, "Menuju menu kelola anggota")
  clear(10 if error else 6)
  menu_kelola_anggota(error=False)

# Fungsi menghapus anggota
def menu_hapus_anggota(error = False):
  print(f'{"="*56}\n= {" Hapus Anggota":^52} =\n{"="*56}\n')
  
  nim = input("> NIM: ")
  if nim == "":
    clear(8 if error else 4)
    print("!"*56)
    print(f'!! {"NIM tidak boleh kosong":^50} !!')
    print("!"*56)
    
    menu_hapus_anggota(error=True)
  else:
    clear(5 if error else 1)
    
    for i in range(len(list_anggota)):
      if list_anggota[i]["NIM"] == nim:
        print("NIM:", list_anggota[i]["NIM"], " | Nama:", list_anggota[i]["nama"], " | Jurusan:", list_anggota[i]["jurusan"], " | Jenis Kelamin:", list_anggota[i]["jenis_kelamin"], " | No Telepon:", list_anggota[i]["no_telepon"], " | Alamat:", list_anggota[i]["alamat"], end="\n\n")
        
        hapus = input("\n> Hapus anggota (y/n): ").lower()
        
        if hapus == "y":
          list_anggota.pop(i)
          with open(path_anggota, "w") as f:
            json.dump(list_anggota, f)
            
          print("\nAnggota berhasil dihapus!")
          time.sleep(2.5)
          
          clear(11 if error else 7)
          
          hapus_lagi = input("\n> Hapus anggota lagi (y/n): ").lower()
          clear(5)
          
          if hapus_lagi == "y":
            menu_hapus_anggota(error=False)
          else:
            menu_kelola_anggota(error=False)
        else:
          print("\nBatal!\n")
          loading(1, "Menuju menu kelola anggota")
          clear(16 if error else 12)
          menu_kelola_anggota(error=False)

  print("Anggota tidak ditemukan!")
  loading(1, "Menuju menu kelola anggota")
  clear(10 if error else 6)
  menu_kelola_anggota(error=False)

# Fungsi menampilkan menu kelola peminjaman dan pengembalian
def menu_kelola_peminjaman_dan_pengembalian(error = False):
  print(f'{"="*56}\n= {" Menu Kelola Peminjaman dan Pengembalian":^52} =\n{"="*56}')
  print(f'| {"(1) Pinjam Buku":<52} |')
  print(f'| {"(2) Kembalikan Buku":<52} |')
  print(f'| {"(3) Lihat Riwayat Peminjaman":<52} |')
  print(f'| {"(4) Kembali Ke Menu Utama":<52} |')
  print(f'| {"(5) Keluar Aplikasi":<52} |')
  print("="*56, end="\n\n")
  
  pilihan = input("> Pilih menu (1-6): ")
  
  if pilihan == "1":
    clear(15 if error else 11)
    menu_pinjam()
  elif pilihan == "2":
    clear(15 if error else 11)
    menu_kembalikan_buku()
  elif pilihan == "3":
    clear(15 if error else 11)
    menu_riwayat_peminjaman()
  elif pilihan == "4":
    clear(15 if error else 11)
    menu_utama()
  elif pilihan == "5":
    keluar_aplikasi()
  else:
    clear(15 if error else 11)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_kelola_buku(error=True)

# Fungsi pinjam
peminjaman_baru = peminjaman.copy()
anggota_terpilih = None
buku_terpilih = None
def menu_pinjam(error = False):
  global peminjaman_baru, anggota_terpilih, buku_terpilih
  
  print(f'{"="*56}\n= {" Pinjam Buku":^52} =\n{"="*56}\n')
  
  if anggota_terpilih == None:
    nim = input("> NIM: ")
    if nim == "":
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"NIM tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_pinjam(error=True)
    else:
      for i in range(len(list_anggota)):
        if list_anggota[i]["NIM"] == nim:
          anggota_terpilih = list_anggota[i]
          clear(9 if error else 5)
          menu_pinjam(error=False)
      
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"Anggota tidak ditemukan":^50} !!')
      print("!"*56)
      
      menu_pinjam(error=True)
  else:
    print("NIM:", anggota_terpilih["NIM"], " | Nama:", anggota_terpilih["nama"], " | Jurusan:", anggota_terpilih["jurusan"], " | Jenis Kelamin:", anggota_terpilih["jenis_kelamin"], " | No Telepon:", anggota_terpilih["no_telepon"], " | Alamat:", anggota_terpilih["alamat"], end="\n")
      
  if buku_terpilih == None:
    isbn = input("> ISBN: ")
    if isbn == "":
      clear(9 if error else 5)
      print("!"*56)
      print(f'!! {"ISBN tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_pinjam(error=True)
    else:
      for i in range(len(list_buku)):
        if list_buku[i]["ISBN"] == isbn:
          if list_buku[i]["stok"] == 0:
            clear(9 if error else 5)
            print("!"*56)
            print(f'!! {"Stok buku habis":^50} !!')
            print("!"*56)
            
            menu_pinjam(error=True)
          else:
            buku_terpilih = list_buku[i]
            clear(10 if error else 6)
            menu_pinjam(error=False)
      
      clear(9 if error else 5)
      print("!"*56)
      print(f'!! {"Buku tidak ditemukan":^50} !!')
      print("!"*56)
      
      menu_pinjam(error=True)
  else:
    print("ISBN:", buku_terpilih["ISBN"], " | Judul:", buku_terpilih["judul"], " | Pengarang:", buku_terpilih["pengarang"], " | Penerbit:", buku_terpilih["penerbit"], " | Tahun Terbit:", buku_terpilih["tahun_terbit"], " | Jumlah Halaman:", buku_terpilih["jumlah_halaman"], " | Stok:", buku_terpilih["stok"], end="\n")
          
  pinjam = input("\n> Pinjam buku (y/n): ").lower()
  if pinjam == 'y':
    peminjaman_baru["NIM"] = anggota_terpilih["NIM"]
    peminjaman_baru["ISBN"] = buku_terpilih["ISBN"]
    peminjaman_baru["tanggal_pinjam"] = datetime.datetime.now().strftime("%d/%m/%Y")
    
    for i in range(len(list_peminjaman)):
      if list_peminjaman[i]["NIM"] == peminjaman_baru["NIM"] and list_peminjaman[i]["ISBN"] == peminjaman_baru["ISBN"] and list_peminjaman[i]["tanggal_pinjam"] == peminjaman_baru["tanggal_pinjam"]:
        clear(11 if error else 7)
        print("!"*56)
        print(f'!! {"Anggota sudah meminjam buku ini":^50} !!')
        print("!"*56)
        
        menu_pinjam(error=True)
    
    peminjaman_baru["status"] = "Dipinjam"
    
    list_peminjaman.insert(0, peminjaman_baru)
    with open(path_peminjaman, "w") as f:
      json.dump(list_peminjaman, f)
      
    for i in range(len(list_buku)):
      if list_buku[i]["ISBN"] == buku_terpilih["ISBN"]:
        list_buku[i]["stok"] -= 1
        with open(path_buku, "w") as f:
          json.dump(list_buku, f)
      
    print("\nBuku berhasil dipinjam!")
    time.sleep(2.5)
    
    clear(11 if error else 7)
    
    pinjam_lagi = input("\n> Pinjam buku lagi (y/n): ").lower()
    peminjaman_baru = peminjaman.copy()
    anggota_terpilih = None
    buku_terpilih = None
    clear(5)
    
    if pinjam_lagi == "y":
      menu_pinjam(error=False)
    else:
      menu_kelola_peminjaman_dan_pengembalian(error=False)
  else:
    print("\nBatal!\n")
    peminjaman_baru = peminjaman.copy()
    anggota_terpilih = None
    buku_terpilih = None
    loading(1, "Menuju menu kelola peminjaman dan pengembalian")
    clear(16 if error else 12)
    menu_kelola_peminjaman_dan_pengembalian(error=False)

peminjaman_edit = peminjaman.copy()
anggota_terpilih = None
buku_terpilih = None
# Fungsi mengembalikan buku
def menu_kembalikan_buku(error = False):
  global peminjaman_edit, anggota_terpilih, buku_terpilih
  
  print(f'{"="*56}\n= {" Kembalikan Buku":^52} =\n{"="*56}\n')
  
  if anggota_terpilih == None:
    nim = input("> NIM: ")
    if nim == "":
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"NIM tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_kembalikan_buku(error=True)
    else:
      for i in range(len(list_anggota)):
        if list_anggota[i]["NIM"] == nim:
          anggota_terpilih = list_anggota[i]
          clear(9 if error else 5)
          menu_kembalikan_buku(error=False)
      
      clear(8 if error else 4)
      print("!"*56)
      print(f'!! {"Anggota tidak ditemukan":^50} !!')
      print("!"*56)
      
      menu_kembalikan_buku(error=True)
  else:
    print("NIM:", anggota_terpilih["NIM"], " | Nama:", anggota_terpilih["nama"], " | Jurusan:", anggota_terpilih["jurusan"], " | Jenis Kelamin:", anggota_terpilih["jenis_kelamin"], " | No Telepon:", anggota_terpilih["no_telepon"], " | Alamat:", anggota_terpilih["alamat"], end="\n")
      
  if buku_terpilih == None:
    isbn = input("> ISBN: ")
    if isbn == "":
      clear(9 if error else 5)
      print("!"*56)
      print(f'!! {"ISBN tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_kembalikan_buku(error=True)
    else:
      for i in range(len(list_buku)):
        if list_buku[i]["ISBN"] == isbn:
          buku_terpilih = list_buku[i]
          clear(10 if error else 6)
          menu_kembalikan_buku(error=False)
      
      clear(9 if error else 5)
      print("!"*56)
      print(f'!! {"Buku tidak ditemukan":^50} !!')
      print("!"*56)
      
      menu_kembalikan_buku(error=True)
  else:
    print("ISBN:", buku_terpilih["ISBN"], " | Judul:", buku_terpilih["judul"], " | Pengarang:", buku_terpilih["pengarang"], " | Penerbit:", buku_terpilih["penerbit"], " | Tahun Terbit:", buku_terpilih["tahun_terbit"], " | Jumlah Halaman:", buku_terpilih["jumlah_halaman"], " | Stok:", buku_terpilih["stok"], end="\n")

  if peminjaman_edit["tanggal_pinjam"] == None:
    tanggal_pinjam = input("> Tanggal Pinjam (dd/mm/yyyy): ")
  
    if tanggal_pinjam == "":
      clear(10 if error else 6)
      print("!"*56)
      print(f'!! {"Tanggal Pinjam tidak boleh kosong":^50} !!')
      print("!"*56)
      
      menu_kembalikan_buku(error=True)
    else:
      for i in range(len(list_peminjaman)):
        if list_peminjaman[i]["NIM"] == anggota_terpilih["NIM"] and list_peminjaman[i]["ISBN"] == buku_terpilih["ISBN"] and list_peminjaman[i]["tanggal_pinjam"] == tanggal_pinjam:
          if list_peminjaman[i]["status"] == "Dikembalikan":
            clear(11 if error else 7)
            print("!"*56)
            print(f'!! {"Buku sudah dikembalikan":^50} !!')
            print("!"*56)
            
            menu_kembalikan_buku(error=True)
          else:
            peminjaman_edit = list_peminjaman[i]
            clear(11 if error else 7)
            menu_kembalikan_buku(error=False)
      
      clear(10 if error else 6)
      print("!"*56)
      print(f'!! {"Peminjaman tidak ditemukan":^50} !!')
      print("!"*56)
      
      menu_kembalikan_buku(error=True)
  else:
    print("Tanggal Pinjam:", peminjaman_edit["tanggal_pinjam"])
      
  kembalikan = input("\n> Kembalikan buku (y/n): ").lower()
  
  if kembalikan == "y":
    peminjaman_edit["status"] = "Dikembalikan"
    peminjaman_edit["tanggal_kembali"] = datetime.datetime.now().strftime("%d/%m/%Y")
    
    for i in range(len(list_peminjaman)):
      if list_peminjaman[i]["NIM"] == peminjaman_edit["NIM"] and list_peminjaman[i]["ISBN"] == peminjaman_edit["ISBN"] and list_peminjaman[i]["tanggal_pinjam"] == peminjaman_edit["tanggal_pinjam"]:
        list_peminjaman[i] = peminjaman_edit
        with open(path_peminjaman, "w") as f:
          json.dump(list_peminjaman, f)
      
    for i in range(len(list_buku)):
      if list_buku[i]["ISBN"] == buku_terpilih["ISBN"]:
        list_buku[i]["stok"] += 1
        with open(path_buku, "w") as f:
          json.dump(list_buku, f)
      
    print("\nBuku berhasil dikembalikan!")
    time.sleep(2.5)
    
    clear(11 if error else 7)
    
    kembalikan_lagi = input("\n> Kembalikan buku lagi (y/n): ").lower()
    peminjaman_edit = peminjaman.copy()
    anggota_terpilih = None
    buku_terpilih = None
    clear(6)
    
    if kembalikan_lagi == "y":
      menu_kembalikan_buku(error=False)
    else:
      menu_kelola_peminjaman_dan_pengembalian(error=False)    
  else:
    print("\nBatal!\n")
    peminjaman_edit = peminjaman.copy()
    anggota_terpilih = None
    buku_terpilih = None
    loading(1, "Menuju menu kelola peminjaman dan pengembalian")
    clear(17 if error else 13)
    menu_kelola_peminjaman_dan_pengembalian(error=False)
    
# Fungsi riwayat peminjaman
def menu_riwayat_peminjaman(error = False, halaman = 1):
  print(f'{"="*56}\n= {" Riwayat Peminjaman":^52} =\n{"="*56}\n')
  
  total_peminjaman = len(list_peminjaman)
  total_halaman = total_peminjaman // 5 + 1 if total_peminjaman % 5 != 0 else total_peminjaman // 5
  skip = (halaman - 1) * 5
  
  print(f'{"="*88}\n= {" Halaman " + str(halaman) + " dari " + str(total_halaman):^84} =\n{"="*88}')
  print(f'| {"No":^4} | {"NIM":<10} | {"ISBN":<10} | {"Tanggal Pinjam":<15} | {"Tanggal Kembali":<15} | {"Status":<15} |')
  print(f'{"="*88}')
  
  for i in range(skip, skip + 5):
    if i < total_peminjaman:
      tanggal_kembali = list_peminjaman[i]["tanggal_kembali"] if list_peminjaman[i]["tanggal_kembali"] != None else "-"
      print(f'| {i+1:^4} | {list_peminjaman[i]["NIM"]:<10} | {list_peminjaman[i]["ISBN"]:<10} | {list_peminjaman[i]["tanggal_pinjam"]:<15} | {tanggal_kembali:<15} | {list_peminjaman[i]["status"]:<15} |')
    else:
      print(f'| {"":^4} | {"":<10} | {"":<10} | {"":<15} | {"":<15} | {"":<15} |')
      
  print(f'{"="*88}\n\n{"="*59}')
  
  if halaman > 1:
    print(f'| {"(1) Halaman Sebelumnya":<55} |')
  
  if halaman < total_halaman:
    print(f'| {"(2) Halaman Selanjutnya":<55} |')
    
  print(f'| {"(3) Kembali Ke Menu Kelola Peminjaman dan Pengembalian":<55} |')
  print(f'| {"(4) Keluar Aplikasi":<55} |')
  
  print("="*59, end="\n\n")
  
  pilihan = input("> Pilih menu (1-4): ")
  
  if pilihan == "1":
    clear(27 if error else 23)
    
    if halaman > 1:
      menu_riwayat_peminjaman(error=False, halaman=halaman-1)
    else:
      menu_riwayat_peminjaman(error=False, halaman=halaman)
  elif pilihan == "2":
    clear(27 if error else 23)
    
    if halaman < total_halaman:
      menu_riwayat_peminjaman(error=False, halaman=halaman+1)
    else:
      menu_riwayat_peminjaman(error=False, halaman=halaman)
  elif pilihan == "3":
    clear(27 if error else 23)
    menu_kelola_peminjaman_dan_pengembalian()
  elif pilihan == "4":
    keluar_aplikasi()
  else:
    clear(26 if error else 22)
    print("!"*56)
    print(f'!! {"Pilihan tidak tersedia":^50} !!')
    print("!"*56)
    
    menu_riwayat_peminjaman(error=True, halaman=halaman)
  

# Menjalankan program
main()