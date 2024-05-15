
cases = ((5,[3],True),(15,[15],True),(4,[2],False),(7,[7],True),(30,[29],True))

for case in cases:
    army_count = case[0]
    list_count = army_count
    wynik = int()
    kolo = []
    i = 1
    while i <= army_count:
        kolo.append(i)
        i += 1
    while len(kolo) != 1:
        if len(kolo) % 2 == 0:
            i = 0
            while i < list_count/2:
                if len(kolo) != 1:
                    del(kolo[i+1])
                    i += 1
                else:
                    break
            list_count = len(kolo)
        if len(kolo) % 2 != 0:
            if len(kolo) != 1:
                i = 0
                del(kolo[0])
            else:
                break
            while i < (int(list_count/2)):
                if len(kolo) != 1:
                    del(kolo[i])
                    i += 1
                else:
                    break
            list_count = len(kolo)
    print(case, ' : ', kolo == case[1],',',' Correct position:', kolo[0])



