cases = ([{'day': 12, 'month': 3, 'year': 2023},{'day': 25, 'month': 6, 'year': 2022},{'day': 5, 'month': 11, 'year': 2023},{'day': 8, 'month': 6, 'year': 2022}],
         [{'day': 15, 'month': 2, 'year': 2020},{'day': 5, 'month': 6, 'year': 1999},{'day': 10, 'month': 1, 'year': 2000},{'day': 20, 'month': 12, 'year': 2022}])

for case in cases:
    daty = case
    length = len(case)
    for liczba in range(length):
        for liczba2 in range(0, length-liczba-1):
            data1 = daty[liczba2]
            data2 = daty[liczba2 + 1]
            if data1['year'] != data2['year']:
                if data1['year'] > data2['year']:
                    daty[liczba2], daty[liczba2+1] = daty[liczba2+1], daty[liczba2]
            elif data1['month'] != data2['month']:
                if data1['month'] > data2['month']:
                    daty[liczba2], daty[liczba2+1] = daty[liczba2+1], daty[liczba2]
            elif data1['day'] != data2['day']:
                if data1['day'] > data2['day']:
                    daty[liczba2], daty[liczba2+1] = daty[liczba2+1], daty[liczba2]


    for date in daty:
        print("{}/{}/{}".format(date['day'], date['month'], date['year']))
    print("End of case")
