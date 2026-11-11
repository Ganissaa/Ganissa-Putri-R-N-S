# Mengimpor kelas Admin dari modul Admin9.py
from Admin9 import Admin

print(" Imported Admin ")
# Membuat instance Admin
admin_baru = Admin("Rara", "Putri", 26, "rara_admin", "Surabaya")

# Menampilkan informasi dan hak akses
admin_baru.describe_user()
admin_baru.privileges.show_privileges()