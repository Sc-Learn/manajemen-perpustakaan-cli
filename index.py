import json
import os
import sys
import time
import datetime
import colorama 
from colorama import Fore, Back, Style
import getpass
import inquirer
from prettytable import PrettyTable

#Inisialisasi colorama
colorama.init(autoreset=True)

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

# Mendefinisikan path file JSON untuk buku, anggota, dan peminjaman
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
    
# fungsi mengubah data file JSON
def ubah_file_json(lokasi_file, data):
  with open(lokasi_file, 'w') as f:
    json.dump(data, f)
    
# Fungsi clear screen terminal
def clear_screen(tampilkan_header_aplikasi=True):
  command = 'clear'
  if os.name in ('nt', 'dos'):
      command = 'cls'
  os.system(command)
  
  if tampilkan_header_aplikasi:
    header()
  
# Fungsi keluar aplikasi
def keluar_aplikasi():
  print(f"{Fore.GREEN}Terima kasih telah menggunakan program ini{Style.RESET_ALL}")
  time.sleep(2)
  clear_screen(False)
  sys.exit()

# Fungsi validasi inputan tidak boleh kosong inquirer
def validasi_inputan_tidak_kosong(_, x):
  if x == "":
    raise inquirer.errors.ValidationError('', reason='Inputan tidak boleh kosong')
  
  return True
  
# Fungsi validasi inputan harus angka inquirer
def validasi_inputan_harus_angka(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  if x.isdigit():
    return True
  else:
    raise inquirer.errors.ValidationError('', reason='Inputan harus angka')

# Fungsi validasi buku baru ISBN inquirer
def validasi_buku_baru_isbn(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  # cari apakah ISBN sudah ada di list buku
  for buku in list_buku:
    if buku["ISBN"] == x:
      raise inquirer.errors.ValidationError('', reason='Buku sudah terdaftar')
    
  return True

# Fungsi validasi ubah buku ISBN inquirer
def validasi_ubah_buku_isbn(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  for buku in list_buku:
    if buku["ISBN"] == x:
      return True
    
  raise inquirer.errors.ValidationError('', reason='ISBN tidak ditemukan')

# Fungsi validasi anggota baru NIM inquirer
def validasi_anggota_baru_nim(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  # cari apakah NIM sudah ada di list anggota
  for anggota in list_anggota:
    if anggota["NIM"] == x:
      raise inquirer.errors.ValidationError('', reason='Anggota sudah terdaftar')
    
  return True

# Fungsi validasi ubah anggota NIM inquirer
def validasi_ubah_anggota_nim(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  for anggota in list_anggota:
    if anggota["NIM"] == x:
      return True
    
  raise inquirer.errors.ValidationError('', reason='NIM tidak ditemukan')

# Fungsi validasi tanggal inquirer
def validasi_tanggal(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  try:
    datetime.datetime.strptime(x, '%d-%m-%Y')
  except ValueError:
    raise inquirer.errors.ValidationError('', reason='Format tanggal salah')
    
  return True

# fungsi validasi tanggal pinjam inquirer (ketika kembalikan buku)
def validasi_tanggal_pinjam(_, x):
  validasi_tanggal(_, x)

  # cari data peminjaman berdasarkan NIM dan ISBN daan tanggal pinjam
  for peminjaman in list_peminjaman:
    if peminjaman["NIM"] == _["NIM"] and peminjaman["ISBN"] == _["ISBN"] and peminjaman["tanggal_pinjam"] == x:
      return True
    
  raise inquirer.errors.ValidationError('', reason='Data peminjaman tidak ditemukan')
  
# Fungsi validasi tanggal kembali inquirer
def validasi_tanggal_kembali(_, x):
  validasi_tanggal(_, x)
  
  tanggal_pinjam = _["tanggal_pinjam"]
  tanggal_kembali = x
  
  tanggal_pinjam = datetime.datetime.strptime(tanggal_pinjam, '%d-%m-%Y')
  tanggal_kembali = datetime.datetime.strptime(tanggal_kembali, '%d-%m-%Y')
  
  if tanggal_kembali < tanggal_pinjam:
    raise inquirer.errors.ValidationError('', reason='Tanggal kembali harus lebih besar dari tanggal pinjam')
    
  return True

# Fungsi validasi buku tersedia inquirer
def validasi_buku_tersedia(_, x):
  validasi_inputan_tidak_kosong(_, x)
  
  # cari apakah ISBN sudah ada di list buku
  for buku in list_buku:
    if buku["ISBN"] == x:
      if buku["stok"] > 0:
        return True
      else:
        raise inquirer.errors.ValidationError('', reason='Buku tidak tersedia')
    
  raise inquirer.errors.ValidationError('', reason='ISBN tidak ditemukan')

# Fungsi untuk menampilkan header aplikasi
def header():
  print("="*56)
  print(f'= {Fore.CYAN}{"Selamat Datang di Program Perpustakaan":^52}{Style.RESET_ALL} =')
  print("="*56)
  
# Fungsi menampilkan pesan error
def tampikan_pesan_error(pesan_error):
  print("!"*56)
  print(f'!! {Fore.RED}{pesan_error:^50}{Style.RESET_ALL} !!')
  print("!"*56)
  print("="*56)
  
# Fungsi Utama
def main():
  clear_screen()
  
  # Login
  user_login = False
  percobaaan_login = 1
  pesan_error = None
  while not user_login:
    user_login, pesan_error = login(pesan_error)
    
    if not user_login and percobaaan_login < MAX_LOGIN:
      clear_screen()
      percobaaan_login += 1
    elif not user_login and percobaaan_login >= MAX_LOGIN:
      print(f'\n{Fore.RED}Terlalu banyak percobaan login{Style.RESET_ALL}')
      time.sleep(2)
      clear_screen(False)
      sys.exit()
    else:
      print(f'\n{Fore.GREEN}Login berhasil! Selamat datang admin{Style.RESET_ALL}')
      time.sleep(2)
      clear_screen()
      break 
    
  # Menu Utama
  keluar = False
  while not keluar:
    pilihan_menu = menu_utama()
    
    if pilihan_menu == "Buku":
      menu_kelola_buku()     
    elif pilihan_menu == "Anggota":
      menu_kelola_anggota()
    elif pilihan_menu == "Peminjaman":
      menu_kelola_peminjaman()
    elif pilihan_menu == "Keluar":
      keluar = True
      
  keluar_aplikasi()

# Fungsi Login
def login(pesan_error=None):
  if pesan_error:
    tampikan_pesan_error(pesan_error)
  
  print(f'= {Fore.BLUE}{"Silahkan Login terlebih dahulu":^52}{Style.RESET_ALL} =')
  print("="*56, end="\n\n")
  
  username = input(f"> {Fore.MAGENTA}Username:{Style.RESET_ALL} ")
  password = getpass.getpass(prompt=f"> {Fore.MAGENTA}Password:{Style.RESET_ALL} ")
  
  if username == admin["username"] and password == admin["password"]:    
    return True, None
  else:
    return False, "Username atau Password salah"

# Fungsi menampilkan menu utama
def menu_utama():
  print(f'= {Fore.LIGHTBLUE_EX}{" Menu Utama":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  pilihan_menu = inquirer.prompt([
    inquirer.List('menu',
                  message="Silahkan pilih menu",
                  choices=['Buku', 'Anggota', 'Peminjaman', 'Keluar'],
              ),
  ])
  
  clear_screen()
  return pilihan_menu["menu"]
  
# Fungsi kelola buku
def menu_kelola_buku():
  while True:
    print(f'= {Fore.LIGHTBLUE_EX}{" Menu Kelola Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
    
    pilihan_menu = inquirer.prompt([
      inquirer.List('menu',
                    message="Silahkan pilih menu",
                    choices=['Tambah Buku', 'Ubah Buku', 'Hapus Buku', 'Lihat Buku', 'Kembali'],
                ),
    ])["menu"]
    
    clear_screen()
    
    if pilihan_menu == "Tambah Buku":
      tambah_buku = True
      while tambah_buku:
        tambah_buku = menu_tambah_buku()     
    elif pilihan_menu == "Ubah Buku":
      ubah_buku = True
      while ubah_buku:
        ubah_buku = menu_ubah_buku()
    elif pilihan_menu == "Hapus Buku":
      hapus_buku = True
      while hapus_buku:
        hapus_buku = menu_hapus_buku()
    elif pilihan_menu == "Lihat Buku":
      lihat_buku = True
      halaman = 1
      while lihat_buku:
        pilihan_menu_lihat_buku = menu_lihat_buku(halaman)
        
        if pilihan_menu_lihat_buku == "Halaman Sebelumnya":
          halaman -= 1
        elif pilihan_menu_lihat_buku == "Halaman Selanjutnya":
          halaman += 1
        elif pilihan_menu_lihat_buku == "Kembali":
          lihat_buku = False
    else:
      break
  
# Fungsi tambah buku
def menu_tambah_buku():
  print(f'= {Fore.LIGHTBLUE_EX}{" Tambah Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  pertanyaan = [
    inquirer.Text('ISBN',
                  message="ISBN",
                  validate=validasi_buku_baru_isbn
              ),
    inquirer.Text('judul',
                  message="Judul",
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.Text('pengarang',
                  message="Pengarang",
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.Text('penerbit',
                  message="Penerbit",
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.Text('tahun_terbit',
                  message="Tahun Terbit",
                  validate=validasi_inputan_harus_angka
              ),
    inquirer.Text('jumlah_halaman',
                  message="Jumlah Halaman",
                  validate=validasi_inputan_harus_angka
              ),
    inquirer.Text('stok',
                  message="Stok",
                  validate=validasi_inputan_harus_angka
              ),
  ]  
  
  data_buku = inquirer.prompt(pertanyaan)
  simpan_buku = inquirer.prompt([
    inquirer.Confirm('simpan',
                  message="Simpan data buku?"
              ),
  ])

  if simpan_buku["simpan"]:    
    list_buku.insert(0, data_buku)
    ubah_file_json(path_buku, list_buku)
    
    print(f'\n{Fore.GREEN}Buku berhasil disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
    tambah_buku_lagi = inquirer.prompt([
      inquirer.Confirm('tambah',
                    message="Tambah buku lagi?"
                ),
    ])
    
    if tambah_buku_lagi["tambah"]:
      return True
  else:
    print(f'\n{Fore.RED}Buku tidak disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen() 
  return False

# Fungsi ubah buku
def menu_ubah_buku():
  print(f'= {Fore.LIGHTBLUE_EX}{" Ubah Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  isbn = inquirer.prompt([
    inquirer.Text('ISBN',
                  message="ISBN",
                  validate=validasi_ubah_buku_isbn
              ),
  ])["ISBN"]
  
  # cari buku dan index buku berdasarkan ISBN
  buku = None
  index_buku = None
  for i, item in enumerate(list_buku):
    if item["ISBN"] == isbn:
      buku = item
      index_buku = i
      break
  
  pertanyaan = [
    inquirer.Text('judul',
                  message="Judul",
                  default=buku["judul"],
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.Text('pengarang',
                  message="Pengarang",
                  default=buku["pengarang"],
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.Text('penerbit',
                  message="Penerbit",
                  default=buku["penerbit"],
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.Text('tahun_terbit',
                  message="Tahun Terbit",
                  default=buku["tahun_terbit"],
                  validate=validasi_inputan_harus_angka
              ),
    inquirer.Text('jumlah_halaman',
                  message="Jumlah Halaman",
                  default=buku["jumlah_halaman"],
                  validate=validasi_inputan_harus_angka
              ),
    inquirer.Text('stok',
                  message="Stok",
                  default=buku["stok"],
                  validate=validasi_inputan_harus_angka
              ),
  ] 
  
  data_buku = inquirer.prompt(pertanyaan)
  simpan_buku = inquirer.prompt([
    inquirer.Confirm('simpan',
                  message="Simpan data buku?"
              ),
  ])
  
  if simpan_buku["simpan"]:    
    list_buku[index_buku] = data_buku
    list_buku[index_buku]["ISBN"] = isbn
    ubah_file_json(path_buku, list_buku)
    
    print(f'\n{Fore.GREEN}Buku berhasil disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
    ubah_buku_lagi = inquirer.prompt([
      inquirer.Confirm('ubah',
                    message="Ubah buku lagi?"
                ),
    ])
    
    if ubah_buku_lagi["ubah"]:
      return True
  else:
    print(f'\n{Fore.RED}Buku tidak disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False  

# Fungsi hapus buku
def menu_hapus_buku():
  print(f'= {Fore.LIGHTBLUE_EX}{" Hapus Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  isbn = inquirer.prompt([
    inquirer.Text('ISBN',
                  message="ISBN",
                  validate=validasi_ubah_buku_isbn
              ),
  ])["ISBN"]
  
  # cari buku dan index buku berdasarkan ISBN
  buku = None
  index_buku = None
  for i, item in enumerate(list_buku):
    if item["ISBN"] == isbn:
      buku = item
      index_buku = i
      break
    
  print(f'\n{Fore.YELLOW}Data buku yang akan dihapus:{Style.RESET_ALL}')
  print(f'ISBN: {buku["ISBN"]}')
  print(f'Judul: {buku["judul"]}')
  print(f'Pengarang: {buku["pengarang"]}')
  print(f'Penerbit: {buku["penerbit"]}')
  print(f'Tahun Terbit: {buku["tahun_terbit"]}')
  print(f'Jumlah Halaman: {buku["jumlah_halaman"]}')
  print(f'Stok: {buku["stok"]}\n\n')
  
  hapus_buku = inquirer.prompt([
    inquirer.Confirm('hapus',
                  message="Hapus data buku?"
              ),
  ])
  
  if hapus_buku["hapus"]:    
    list_buku.pop(index_buku)
    ubah_file_json(path_buku, list_buku)
    
    print(f'\n{Fore.GREEN}Buku berhasil dihapus{Style.RESET_ALL}')
    time.sleep(2)
    
    hapus_buku_lagi = inquirer.prompt([
      inquirer.Confirm('hapus',
                    message="Hapus buku lagi?"
                ),
    ])
    
    if hapus_buku_lagi["hapus"]:
      return True
  else:
    print(f'\n{Fore.RED}Buku tidak dihapus{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False

# Fungsi lihat buku
def menu_lihat_buku(halaman=1):
  print(f'= {Fore.LIGHTBLUE_EX}{" Lihat Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  total_buku = len(list_buku)
  total_halaman = total_buku // 5 + 1 if total_buku % 5 != 0 else total_buku // 5
  skip = (halaman - 1) * 5
  
  table = PrettyTable()
  table.title = f"Halaman {halaman} dari {total_halaman}"
  table.field_names = ["No", "ISBN", "Judul", "Pengarang", "Penerbit", "Tahun Terbit", "Jumlah Halaman", "Stok"]
  
  for i, item in enumerate(list_buku[skip:skip+5]):
    table.add_row([i+1+skip, item["ISBN"], item["judul"], item["pengarang"], item["penerbit"], item["tahun_terbit"], item["jumlah_halaman"], item["stok"]])
    
  print(table)
  
  menu = []
  if halaman > 1:
    menu.append("Halaman Sebelumnya")
  
  if halaman < total_halaman:
    menu.append("Halaman Selanjutnya") 
    
  menu.append("Kembali") 
  
  pilihan_menu = inquirer.prompt([
    inquirer.List('menu',
                    message="Silahkan pilih menu",
                    choices=menu,
                ),
  ])["menu"]
  
  clear_screen()
  
  return pilihan_menu
  
# Fungsi kelola anggota
def menu_kelola_anggota():
  while True:
    print(f'= {Fore.LIGHTBLUE_EX}{" Menu Kelola Anggota":^52}{Style.RESET_ALL} =\n{"="*56}')
  
    pilihan_menu = inquirer.prompt([
      inquirer.List('menu',
                    message="Silahkan pilih menu",
                    choices=['Tambah Anggota', 'Ubah Anggota', 'Hapus Anggota', 'Lihat Anggota', 'Kembali'],
                ),
    ])["menu"]
    
    clear_screen()
    
    if pilihan_menu == "Tambah Anggota":
      tambah_anggota = True
      while tambah_anggota:
        tambah_anggota = menu_tambah_anggota()
    elif pilihan_menu == "Ubah Anggota":
      ubah_anggota = True
      while ubah_anggota:
        ubah_anggota = menu_ubah_anggota()
    elif pilihan_menu == "Hapus Anggota":
      hapus_anggota = True
      while hapus_anggota:
        hapus_anggota = menu_hapus_anggota()
    elif pilihan_menu == "Lihat Anggota":
      lihat_anggota = True
      halaman = 1
      while lihat_anggota:
        pilihan_menu_lihat_anggota = menu_lihat_anggota(halaman)
        
        if pilihan_menu_lihat_anggota == "Halaman Sebelumnya":
          halaman -= 1
        elif pilihan_menu_lihat_anggota == "Halaman Selanjutnya":
          halaman += 1
        elif pilihan_menu_lihat_anggota == "Kembali":
          lihat_anggota = False
    else:
      break

# Fungsi tambah anggota
def menu_tambah_anggota():
  print(f'= {Fore.LIGHTBLUE_EX}{" Tambah Anggota":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  pertanyaan = [
    inquirer.Text('NIM',
                  message="NIM",
                  validate=validasi_anggota_baru_nim
              ),
    inquirer.Text('nama',
                  message="Nama",
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.List('jurusan',
                  message="Jurusan",
                  choices=['Teknik Informatika', 'Sistem Informasi', 'Teknik Komputer', 'Manajemen Informatika'],
              ),
    inquirer.List('jenis_kelamin',
                  message="Jenis Kelamin",
                  choices=['Laki-laki', 'Perempuan'],
              ),
    inquirer.Text('no_telepon',
                  message="No Telepon",
                  validate=validasi_inputan_harus_angka
              ),
    inquirer.Text('alamat',
                  message="Alamat",
                  validate=validasi_inputan_tidak_kosong
              ),
  ]
  
  data_anggota = inquirer.prompt(pertanyaan)
  simpan_anggota = inquirer.prompt([
    inquirer.Confirm('simpan',
                  message="Simpan data anggota?"
              ),
  ])
  
  if simpan_anggota["simpan"]:
    list_anggota.insert(0, data_anggota)
    ubah_file_json(path_anggota, list_anggota)
    
    print(f'\n{Fore.GREEN}Anggota berhasil disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
    tambah_anggota_lagi = inquirer.prompt([
      inquirer.Confirm('tambah',
                    message="Tambah anggota lagi?"
                ),
    ])
    
    if tambah_anggota_lagi["tambah"]:
      return True
  else:
    print(f'\n{Fore.RED}Anggota tidak disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False

# Fungsi ubah anggota
def menu_ubah_anggota():
  print(f'= {Fore.LIGHTBLUE_EX}{" Ubah Anggota":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  nim = inquirer.prompt([
    inquirer.Text('NIM',
                  message="NIM",
                  validate=validasi_ubah_anggota_nim
              ),
  ])["NIM"]
  
  # cari anggota dan index anggota berdasarkan NIM
  anggota = None
  index_anggota = None
  for i, item in enumerate(list_anggota):
    if item["NIM"] == nim:
      anggota = item
      index_anggota = i
      break
  
  pertanyaan = [
    inquirer.Text('nama',
                  message="Nama",
                  default=anggota["nama"],
                  validate=validasi_inputan_tidak_kosong
              ),
    inquirer.List('jurusan',
                  message="Jurusan",
                  default=anggota["jurusan"],
                  choices=['Teknik Informatika', 'Sistem Informasi', 'Teknik Komputer', 'Manajemen Informatika'],
              ),
    inquirer.List('jenis_kelamin',
                  message="Jenis Kelamin",
                  default=anggota["jenis_kelamin"],
                  choices=['Laki-laki', 'Perempuan'],
              ),
    inquirer.Text('no_telepon',
                  message="No Telepon",
                  default=anggota["no_telepon"],
                  validate=validasi_inputan_harus_angka
              ),
    inquirer.Text('alamat',
                  message="Alamat",
                  default=anggota["alamat"],
                  validate=validasi_inputan_tidak_kosong
              ),
  ]
  
  data_anggota = inquirer.prompt(pertanyaan)
  simpan_anggota = inquirer.prompt([
    inquirer.Confirm('simpan',
                  message="Simpan data anggota?"
              ),
  ])
  
  if simpan_anggota["simpan"]:
    list_anggota[index_anggota] = data_anggota
    list_anggota[index_anggota]["NIM"] = nim
    ubah_file_json(path_anggota, list_anggota)
    
    print(f'\n{Fore.GREEN}Anggota berhasil disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
    ubah_anggota_lagi = inquirer.prompt([
      inquirer.Confirm('ubah',
                    message="Ubah anggota lagi?"
                ),
    ])
    
    if ubah_anggota_lagi["ubah"]:
      return True
  else:
    print(f'\n{Fore.RED}Anggota tidak disimpan{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False

# Fungsi hapus anggota
def menu_hapus_anggota():
  print(f'= {Fore.LIGHTBLUE_EX}{" Hapus Anggota":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  nim = inquirer.prompt([
    inquirer.Text('NIM',
                  message="NIM",
                  validate=validasi_ubah_anggota_nim
              ),
  ])["NIM"]
  
  # cari anggota dan index anggota berdasarkan NIM
  anggota = None
  index_anggota = None
  for i, item in enumerate(list_anggota):
    if item["NIM"] == nim:
      anggota = item
      index_anggota = i
      break
    
  print(f'\n{Fore.YELLOW}Data anggota yang akan dihapus:{Style.RESET_ALL}')
  print(f'NIM: {anggota["NIM"]}')
  print(f'Nama: {anggota["nama"]}')
  print(f'Jurusan: {anggota["jurusan"]}')
  print(f'Jenis Kelamin: {anggota["jenis_kelamin"]}')
  print(f'No Telepon: {anggota["no_telepon"]}')
  print(f'Alamat: {anggota["alamat"]}\n\n')
  
  hapus_anggota = inquirer.prompt([
    inquirer.Confirm('hapus',
                  message="Hapus data anggota?"
              ),
  ])
  
  if hapus_anggota["hapus"]:    
    list_anggota.pop(index_anggota)
    ubah_file_json(path_anggota, list_anggota)
    
    print(f'\n{Fore.GREEN}Anggota berhasil dihapus{Style.RESET_ALL}')
    time.sleep(2)
    
    hapus_anggota_lagi = inquirer.prompt([
      inquirer.Confirm('hapus',
                    message="Hapus anggota lagi?"
                ),
    ])
    
    if hapus_anggota_lagi["hapus"]:
      return True
  else:
    print(f'\n{Fore.RED}Anggota tidak dihapus{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False

# Fungsi lihat anggota
def menu_lihat_anggota(halaman=1):
  print(f'= {Fore.LIGHTBLUE_EX}{" Lihat Anggota":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  total_anggota = len(list_anggota)
  total_halaman = total_anggota // 5 + 1 if total_anggota % 5 != 0 else total_anggota // 5
  skip = (halaman - 1) * 5
  
  table = PrettyTable()
  table.title = f"Halaman {halaman} dari {total_halaman}"
  table.field_names = ["No", "NIM", "Nama", "Jurusan", "Jenis Kelamin", "No Telepon", "Alamat"]
  
  for i, item in enumerate(list_anggota[skip:skip+5]):
    table.add_row([i+1+skip, item["NIM"], item["nama"], item["jurusan"], item["jenis_kelamin"], item["no_telepon"], item["alamat"]])
    
  print(table)
  
  menu = []
  if halaman > 1:
    menu.append("Halaman Sebelumnya")
  
  if halaman < total_halaman:
    menu.append("Halaman Selanjutnya") 
    
  menu.append("Kembali") 
  
  pilihan_menu = inquirer.prompt([
    inquirer.List('menu',
                    message="Silahkan pilih menu",
                    choices=menu,
                ),
  ])["menu"]
  
  clear_screen()
  return pilihan_menu

# Fungsi kelola peminjaman
def menu_kelola_peminjaman():
  while True:
    print(f'= {Fore.LIGHTBLUE_EX}{" Menu Kelola Peminjaman":^52}{Style.RESET_ALL} =\n{"="*56}')
  
    pilihan_menu = inquirer.prompt([
      inquirer.List('menu',
                    message="Silahkan pilih menu",
                    choices=['Pinjam Buku', 'Kembalikan Buku', 'Lihat Riwayat Peminjaman', 'Kembali'],
                ),
    ])["menu"]
    
    clear_screen()
    
    if pilihan_menu == "Pinjam Buku":
      tambah_peminjaman = True
      while tambah_peminjaman:
        tambah_peminjaman = menu_tambah_peminjaman()
    elif pilihan_menu == "Kembalikan Buku":
      kembalikan_peminjaman = True
      while kembalikan_peminjaman:
        kembalikan_peminjaman = menu_kembalikan_peminjaman()
    elif pilihan_menu == "Lihat Riwayat Peminjaman":
      lihat_peminjaman = True
      halaman = 1
      while lihat_peminjaman:
        pilihan_menu_lihat_peminjaman = menu_lihat_peminjaman(halaman)
        if pilihan_menu_lihat_peminjaman == "Halaman Sebelumnya":
          halaman -= 1
        elif pilihan_menu_lihat_peminjaman == "Halaman Selanjutnya":
          halaman += 1
        elif pilihan_menu_lihat_peminjaman == "Kembali":
          lihat_peminjaman = False
    else:
      break
    
# fungsi pinjam buku
def menu_tambah_peminjaman():
  print(f'= {Fore.LIGHTBLUE_EX}{" Pinjam Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  pertanyaan = [
    inquirer.Text('NIM',
                  message="NIM",
                  validate=validasi_ubah_anggota_nim
              ),
    inquirer.Text('ISBN',
                  message="ISBN",
                  validate=validasi_buku_tersedia
              ),
    inquirer.Text('tanggal_pinjam',
                  message="Tanggal Pinjam (dd-mm-yyyy)",
                  validate=validasi_tanggal
              ),
  ]
  
  data_peminjaman = inquirer.prompt(pertanyaan)
  simpan_peminjaman = inquirer.prompt([
    inquirer.Confirm('simpan',
                  message="Pinjam buku?"
              ),
  ])
  
  if simpan_peminjaman["simpan"]:
    list_peminjaman.insert(0, data_peminjaman)
    ubah_file_json(path_peminjaman, list_peminjaman)
    
    print(f'\n{Fore.GREEN}Buku berhasil dipinjam{Style.RESET_ALL}')
    time.sleep(2)
    
    tambah_peminjaman_lagi = inquirer.prompt([
      inquirer.Confirm('tambah',
                    message="Pinjam buku lagi?"
                ),
    ])
    
    if tambah_peminjaman_lagi["tambah"]:
      return True
  else:
    print(f'\n{Fore.RED}Buku gagal dipinjam{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False

# fungsi kembalikan buku
def menu_kembalikan_peminjaman():
  print(f'= {Fore.LIGHTBLUE_EX}{" Kembalikan Buku":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  pertanyaan = [
    inquirer.Text('NIM',
                  message="NIM",
                  validate=validasi_ubah_anggota_nim
              ),
    inquirer.Text('ISBN',
                  message="ISBN",
                  validate=validasi_ubah_buku_isbn
              ),
    inquirer.Text('tanggal_pinjam',
                  message="Tanggal Pinjam (dd-mm-yyyy)",
                  validate=validasi_tanggal_pinjam
              ),
    inquirer.Text('tanggal_kembali', 
                  message="Tanggal Kembali (dd-mm-yyyy)",
                  validate=validasi_tanggal_kembali
              ),
  ]
  
  data_peminjaman = inquirer.prompt(pertanyaan)
  
  # cari peminjaman dan index peminjaman berdasarkan NIM, ISBN, dan tanggal pinjam
  index_peminjaman = None
  for i, item in enumerate(list_peminjaman):
    if item["NIM"] == data_peminjaman["NIM"] and item["ISBN"] == data_peminjaman["ISBN"] and item["tanggal_pinjam"] == data_peminjaman["tanggal_pinjam"]:
      index_peminjaman = i
      break
    
  simpan_peminjaman = inquirer.prompt([
    inquirer.Confirm('simpan',
                  message="Kembalikan buku?"
              ),
  ])
  
  if simpan_peminjaman["simpan"]:
    list_peminjaman[index_peminjaman] = data_peminjaman
    ubah_file_json(path_peminjaman, list_peminjaman)
    
    print(f'\n{Fore.GREEN}Buku berhasil dikembalikan{Style.RESET_ALL}')
    time.sleep(2)
    
    kembalikan_peminjaman_lagi = inquirer.prompt([
      inquirer.Confirm('kembalikan',
                    message="Kembalikan buku lagi?"
                ),
    ])
    
    if kembalikan_peminjaman_lagi["kembalikan"]:
      return True
  else:
    print(f'\n{Fore.RED}Buku gagal dikembalikan{Style.RESET_ALL}')
    time.sleep(2)
    
  clear_screen()
  return False

# Fungsi lihat peminjaman
def menu_lihat_peminjaman(halaman=1):
  print(f'= {Fore.LIGHTBLUE_EX}{" Lihat Riwayat Peminjaman":^52}{Style.RESET_ALL} =\n{"="*56}')
  
  total_peminjaman = len(list_peminjaman)
  total_halaman = total_peminjaman // 5 + 1 if total_peminjaman % 5 != 0 else total_peminjaman // 5
  skip = (halaman - 1) * 5
  
  table = PrettyTable()
  table.title = f"Halaman {halaman} dari {total_halaman}"
  table.field_names = ["No", "NIM", "ISBN", "Tanggal Pinjam", "Tanggal Kembali"]
  
  for i, item in enumerate(list_peminjaman[skip:skip+5]):
    table.add_row([i+1+skip, item["NIM"], item["ISBN"], item["tanggal_pinjam"], item["tanggal_kembali"]])
    
  print(table)
  
  menu = []
  if halaman > 1:
    menu.append("Halaman Sebelumnya")
    
  if halaman < total_halaman:
    menu.append("Halaman Selanjutnya")
    
  menu.append("Kembali")
  
  pilihan_menu = inquirer.prompt([
    inquirer.List('menu',
                    message="Silahkan pilih menu",
                    choices=menu,
                ),
  ])["menu"]
  
  clear_screen()
  return pilihan_menu  

# Menjalankan fungsi utama
main()