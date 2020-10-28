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
            }
        ]
    }
}

data = data

dictionary = {
    'soort product (keuzelijst)': '',
    'productgroep (keuzelijst)': '',
    'inkoopvolume': '' 
}

for item in data.values():
    eersteID = item['procurementAnalysisID']
    goede = item['products']
    # print(eersteID)
    # print(goede[1])
    for products in goede:

        productomschrijving = products['description']
        waarde = products['procurementVolumeInEuros']
        productgroepen = (products['nourishmentType']['description'])
        

        new_list = [productomschrijving, productgroepen, waarde]
        new_dict = dict(zip(dictionary, new_list))
        print(new_dict
