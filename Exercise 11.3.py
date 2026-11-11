from Employee import Employee

def employee_umum():
    "Membuat fixture untuk objek Employee agar bisa dipakai berulang kali."
    return Employee("Budi", "Santoso", 60000)

def test_give_default_raise(employee_umum):
    "Menguji kenaikan gaji default sebesar $5,000."
    employee_umum.give_raise()
    assert employee_umum.annual_salary == 65000

def test_give_custom_raise(employee_umum):
    "Menguji kenaikan gaji dengan nominal khusus (misal $10,000)."
    employee_umum.give_raise(10000)
    assert employee_umum.annual_salary == 70000