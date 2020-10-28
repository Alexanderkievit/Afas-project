# Dit is de testdata 
data = {
    "data": {
        "procurementAnalysisID": "12",
        "products": [
            {
                "ID": "2",
                "description": "Brood",
                "nourishmentType": {
                    "ID": "3",
                    "description": "Tarwe"
                },
                "procurementVolumeInEuros": 12
            },
            {
                "ID": "4555",
                "description": "Kaas",
                "nourishmentType": {
                    "ID": "34444",
                    "description": "Melk"
                },
                "procurementVolumeInEuros": 24
            },
            {
                "ID": "4525",
                "description": "Snoep",
                "nourishmentType": {
                    "ID": "344",
                    "description": "Zoet"
                },
                "procurementVolumeInEuros": 13
            }
        ]
    }
}

dictionary_of_products = {
    'soort product (keuzelijst)': '',
    'productgroep (keuzelijst)': '',
    'inkoopvolume': '' 
}
# Het halen van values uit de dictiornary en stoppen in een nieuwe dictionary
for item in data.values():
    next_layer = item['products']
    for products in next_layer:

        productomschrijving = products['description']
        waarde = products['procurementVolumeInEuros']
        productgroepen = (products['nourishmentType']['description'])
        

        new_list = [productomschrijving, productgroepen, waarde]
        new_dict = dict(zip(dictionary_of_products, new_list))
        print(new_dict)