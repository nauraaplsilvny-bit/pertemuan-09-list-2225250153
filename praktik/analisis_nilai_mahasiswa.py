
# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi untuk mengambil nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil


# Data nilai 10 mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengambil nilai yang lulus
lulus = nilai_lulus(nilai)

# Menampilkan ringkasan data
print(f"Data           : {nilai}")
print(f"Banyak data    : {len(nilai)}")
print(f"Total          : {sum(nilai)}")
print(f"Rata-rata      : {rata_rata(nilai):.2f}")
print(f"Minimum        : {min(nilai)}")
print(f"Maksimum       : {max(nilai)}")
print(f"Nilai lulus    : {lulus}")
print(f"Jumlah lulus   : {len(lulus)}")
print(f"Belum lulus    : {len(nilai) - len(lulus)}")
