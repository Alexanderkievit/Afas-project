import pprint

# Dit is de testdata
data = {'object_name': 'KnEmployee', 'values': {'ViSe': ['20180901', '20190101', '20190301', '20200101', '20160101', '20140501', '20180101', '20190201', '20181101', '20181101', '20180501', '20180601', '20150801', '20170501', '19900301', '20191101', '20140101', '20060901', '20180415', '20190401', '20050501', '20141001', '20180101', '20170201', '20170901', '20181201', '20160415', '20180101', '20190101', '20160315', '20190101', '20180901', '20170501', '20200101', '20180501', '20170201', '20161001', '20180401', '20140201', '20150301', '20180101', '20180801', '20190101', '20150101', '20190301', '20190101', '20181001', '20190501', '20181201', '20171101', '20100501', '20100301', '20160401'], 'Bl': [3, 2, 1, 1, 1, 1, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}}

# Het ophalen van de keys in data
keys = []
for key in data['values']:
    keys.append(key)

# Vraag van eerste Values de lengte van het aantal datapunten op
itemcount = len(data['values'][keys[0]])

# Het ophalen van de values uit de dictionary en het stoppen in een nieuwe dictionary
data_list = []
for place in range(0,itemcount):
    data_item = {}
    for key in keys:
        data_item[key] = data['values'][key][place]
    data_list.append(data_item)

pprint.pprint(data_list)