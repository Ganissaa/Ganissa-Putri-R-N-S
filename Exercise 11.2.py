from city import format_city_country

def test_city_country():
    "Menguji format kota dan negara tanpa populasi."
    formatted_name = format_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    "Menguji format kota dan negara dengan menyertakan populasi."
    formatted_name = format_city_country('santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - population 5000000'