
cases = ((220,285,[(220,284)]),(123,225,[(125,127)]),(1184,1211,[(1184,1210)]),(220,1211,[(220,284),(1184,1210)]))


for case in cases:
    range_start = case[0]
    range_end = case[1]
    result = []
    for number in range(range_start,range_end):
        dzielnik = 1
        dzielniki1 = []
        while dzielnik < number:
            if number%dzielnik == 0:
                dzielniki1.append(dzielnik)
                dzielnik += 1
            else:
                dzielnik += 1
        for number2 in range(range_start+1,range_end+1):
            dzielniki2 = []
            dzielnik2 = 1
            while dzielnik2 < number2:
                if number2%dzielnik2 == 0:
                    dzielniki2.append(dzielnik2)
                    dzielnik2 += 1
                else:
                    dzielnik2 += 1
            if sum(dzielniki2) == number and sum(dzielniki1) == number2 and number < number2 :
                result.append((number,number2))
                
    print(case, ' : ', result==case[2],' : ',result)
