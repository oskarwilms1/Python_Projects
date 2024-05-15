cases =((1,14,[2,3,5,7,11,13]),(20,30,[23,29]),(100,1050,[101,102,103]),(100,120,[101,103,107,109,113]),(7727,7790,[7727,7741,7753,7757,7759,7789]))

for case in cases:
    result_list = []
    poczatek_zakresu = case[0]
    koniec_zakresu = case[1]
    result = case[2]
    for number in range(poczatek_zakresu,koniec_zakresu):
        if number > 1:
            for i in range(2,(number//2)+1):
                #jeżeli liczba jest podzielna przez jakikolwiek numer od 2 do n/2 to nie jest liczbą pierwszą
                if (number%i) == 0:
                    break
            else:
                result_list.append(number)
    print(case, ": ", result == result_list, " Liczby z zakresu od ",poczatek_zakresu," do ", koniec_zakresu," to: ", result_list)
