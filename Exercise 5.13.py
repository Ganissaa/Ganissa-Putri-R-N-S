nilai_ujian = 85

if nilai_ujian >= 90:
    predikat = "A (Sangat Baik)"
elif nilai_ujian >= 75:
    predikat = "B (Baik)"
elif nilai_ujian >= 60:
    predikat = "C (Cukup)"
else:
    predikat = "D (Kurang / Perlu Belajar Lagi)"

print(f"Nilai Anda adalah {nilai_ujian}, predikat Anda: {predikat}")