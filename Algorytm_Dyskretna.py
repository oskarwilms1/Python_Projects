#Algorytm generowania podzbiorów zbioru {1,2,3,....,n}:
    #Pierwszy podzbiór A to zbiór pusty oznaczony ∅
    #Kolejny podzbiór po podzbiorze A:
        #Znajdujemy największy element a nienależący do A czyli

        # a = max{i ∉ A : i ∈ {1,2,3,....,n}}
        # Jeżeli nie ma takiego a, to rozważany pozdbiór A jest ostatnim - Koniec
        # W przeciwnym przypadku, dodajemy a do zbioru A i usuwamy z A wszystkie elementy większe od a.

# Na przykładzie:

# Mamy zbiór czteroelementowy {1,2,3,4}
    #Zgodnie z algorytmem, wypisuje wszystkie możliwe jego podzbiory:
    # {∅};{4};{3};{3,4};{2};{2,4};{2,3};{2,3,4};{1};{1,4};{1,3};{1,3,4};{1,2};{1,2,4};{1,2,3};{1,2,3,4}
    #Jeżeli miejsca w których znajdują się liczby w zbiorze zastąpie zerami i jedynkami,
    #Tak, że 0 oznacza, że liczba nie należy do tego podzbioru, a 1 że należy, można uzyskać taki ciąg liczb:
    #Zbiór pusty: 0000
    #Zbiór pierwszy: 0001 (pierwszy podzbiór składa się tylko z 4)
    #Zbiór drugi: 0010 (drugi podzbiór składa się tylko z 3)
    #Zbiór trzeci: 0011 (trzeci podzbiór składa się z 3,4)
    #Zbiór czwarty: 0100 (czwarty podzbiór składa się z 2)
    #I tak dalej...
    #Można zauważyć że oznaczenie w ten sposób podzbiorów, tworzy nam ciąg kolejnych liczb w systemie binarnym.

#Zadanie: Napisz program, który dla n-elementowego zbioru, gdzie n jest liczbą wybraną przez użytkownika wypisze wszystkie możliwe jego podzbiory zgodnie z tym algorytemem.
x = int(1)
list = []
    print("Podaj ilość elementu zbioru:\n")
n = int(input())

while x <= n:
    list.append(x)
    x += 1
print("Twój zbiór: \n", list)           #Tutaj pytam użytkownika ile elementów ma zbiór, i tworze ten zbiór






