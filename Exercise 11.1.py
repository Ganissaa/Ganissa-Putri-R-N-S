from city2 import format_city_country

def test_city_country():
    """Menguji format kota dan negara (Latihan 11-1)."""
    formatted_name = format_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    """Menguji format kota, negara, dan populasi (Latihan 11-2)."""
    formatted_name = format_city_country('santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - population 5000000'
