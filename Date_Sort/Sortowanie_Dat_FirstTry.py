
cases = ((['10.3.2000','22.6.2023','12.2.2023'],['10.3.2000','12.2.2023','22.6.2023'],True),(['12.2.2023','12.10.1976','17.2.1984'],['12.10.1976','17.2.1984','12.2.2023'],True),(['5.3.1234'],[],False))

for case in cases:
    Date_Dictionary = {'Day' : [], 'Month' : [],'Year' : [], 'numeric_value' : []}
    Sorted_Dates = []
    i = 0
    while i < len(case[0]):
        list = case[0]
        Date_list = list[i].split('.')
        Date_Dictionary['Day'].append(Date_list[0])
        Date_Dictionary['Month'].append(Date_list[1])
        Date_Dictionary['Year'].append(Date_list[2])
        # date_numeric_value zawiera ilość dni które mineło od daty : 1.01.0001. Źródło wzoru: https://en.wikipedia.org/wiki/Julian_day
        date_numeric_value = 367 * int(Date_list[2]) - (7 * (int(Date_list[2]) + 5001 + (int(Date_list[1]) - 9)/7))/4 + (275 * int(Date_list[1]))/9 + int(Date_list[0]) + 1729777
        Date_Dictionary['numeric_value'].append(date_numeric_value)
        i += 1
    i = 0
    while len(Date_Dictionary['numeric_value']) != 0:
        if i < len(Date_Dictionary['numeric_value']):
            if Date_Dictionary['numeric_value'][i] == min(Date_Dictionary['numeric_value']):
                Sorted_Dates.append(str(Date_Dictionary['Day'][i]+'.'+Date_Dictionary['Month'][i]+'.'+Date_Dictionary['Year'][i]))
                Date_Dictionary['Day'].remove(Date_Dictionary['Day'][i])
                Date_Dictionary['Month'].remove(Date_Dictionary['Month'][i])
                Date_Dictionary['Year'].remove(Date_Dictionary['Year'][i])
                Date_Dictionary['numeric_value'].remove(Date_Dictionary['numeric_value'][i])
            else:
                i += 1
        else:
            i = 0
    print(case, ' : ', Sorted_Dates == case[1],' ', Sorted_Dates)



