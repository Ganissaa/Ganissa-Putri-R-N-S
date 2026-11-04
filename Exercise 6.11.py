cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': '100 juta jiwa',
        'fact': 'kaya tapi dikorupsi.'
    },
    'tokyo': {
        'country': 'jepang',
        'population': '104 juta jiwa',
        'fact': 'Canggih dan modern.'
    },
    'paris': {
        'country': 'perancis',
        'population': '20 juta jiwa',
        'fact': 'Negara keren.'
    }
}

for kota, info in cities.items():
    print(f"\nKota: {kota.title()}")
    print(f"Negara: {info['country'].title()}")
    print(f"Perkiraan Populasi: {info['population']}")
    print(f"Fakta Unik: {info['fact']}")