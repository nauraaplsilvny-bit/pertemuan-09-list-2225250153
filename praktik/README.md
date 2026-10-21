
# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Naura Palisa Ilevani  
NIM: 2225250153
Kelas: 3F

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
Folder latihan berisi enam program:
1. `01_buat_list.py`: membuat list dan menghitung banyak data.
2. `02_indeks_slicing.py`: mengakses elemen menggunakan indeks dan slicing.
3. `03_manipulasi_list.py`: mengubah, menambah, menyisipkan, dan menghapus elemen.
4. `04_agregasi_nilai.py`: menghitung total, rata-rata, minimum, dan maksimum.
5. `05_filter_kelulusan.py`: menyaring nilai mahasiswa yang lulus.
6. `06_fungsi_statistik.py`: menghitung rata-rata menggunakan fungsi.

Folder praktik berisi `analisis_nilai_mahasiswa.py`, yaitu program untuk menganalisis nilai mahasiswa dan menentukan kelulusan.

## Cara Menjalankan
Jalankan setiap file dari terminal VS Code menggunakan perintah Python.

Contoh:

`python latihan/01_buat_list.py`

Untuk menjalankan program utama:

`python praktik/analisis_nilai_mahasiswa.py`

## Test Case

| Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|
| Rata-rata [60, 70, 80] | 70.00 | Sesuai jika hasil aktual cocok |
| Minimum dan maksimum | 60 dan 80 | Sesuai jika hasil aktual cocok |
| Jumlah lulus [60, 70, 80] | 3 | Sesuai jika hasil aktual cocok |
| Kelulusan [59, 60, 61] | 2 | Sesuai jika hasil aktual cocok |
| Rata-rata list kosong | Tidak error | Sesuai jika hasil aktual cocok |

## Refleksi
Saya memahami bahwa list dapat menyimpan banyak nilai dalam satu variabel. Indeks digunakan untuk mengakses elemen, sedangkan slicing digunakan untuk mengambil bagian list. Saya juga belajar mengolah data dengan perulangan dan fungsi. Salah satu hal yang perlu diperhatikan adalah indeks harus berada dalam rentang list dan list kosong perlu diperiksa sebelum menghitung rata-rata.
