
# Membuat list nilai mahasiswa
nilai = [75, 55, 80, 60, 45, 90]

# Menyiapkan list nilai yang lulus
lulus = []

# Memeriksa setiap nilai
for x in nilai:
    if x >= 60:
        lulus.append(x)

# Menampilkan nilai yang lulus dan jumlahnya
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
