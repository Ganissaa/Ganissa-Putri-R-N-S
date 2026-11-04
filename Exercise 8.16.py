# 1 lengkap
import greeting
greeting.greet("yusrina")

# 2 fungsi tertentu
from greeting import greet
greet("ael")

# 3 fungsi dengan alias
from greeting import greet as d
d("domi")

# 4 modul dengan alias
import greeting as l
l.greet("lana")

# 5 semua fungsi
from greeting import *
greet("aul")