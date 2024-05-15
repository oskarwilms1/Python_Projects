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




x = int(1)                  #Tworzę zmienną, która pozwoli mi na utworzenie pętli tworzącej zbiór liczb od 1 - n
list = []               #Tworze pustą listę, która będzie służyć jako zbiór liczbowy
xy = int(0)                 # Tworzę zmienną, która pozwoli mi na utworzenie pętli, w której będę wyświetlał po koleji wszystkie pozdbiory utworzonego zbioru
print("Podaj ilość elementu zbioru:\n")             #Proszę użytkownika o podanie ile elementów ma mieć zbiór.
n = int(input())                    #Oznaczam tą liczbę jako n
podzb = pow(2,n)                    # Liczba wszystkich pozdbiorów tego zbioru oznaczam jako podzb = n^2

while x <= n:
    list.append(x)
    x += 1
print("Twój zbiór: \n", list)           # Pętla służąca do stworzenia n elementowgo zbioru, gdzie liczba n jest podana przez użytkownika
print("Ilość podzbiorów dla tego zbiory wynosi: \n", podzb)     # Podaje wartość zmiennej podzb, która oznacza ilość podzbiorów tego zbioru
while xy <= podzb - 1:      
    xy1 = int(0)
    if xy == 0:
        print("[∅]")        # Pierwszy wyraz jest zbiorem pustym
        
    else:      
        binarne = bin(xy)   # zmieniam każdą zmienną xy na zapis binarny, zmienna xy który podzbiór jest teraz analizowany
        str1 = binarne[2:].zfill(n)     # zmieniam utworzony zapis binarny z standardowego 0b0001 na 0001. Komenda [2:] "ucina" mi znaki 0b a komenda zfill dopełnia mi wyraz zerami
        str2 = "{" # podzbiory chcę zapisać za pomocą znaków {}
        while xy1 <= n - 1:
            if str1[xy1:xy1+1] == "1":
               str2 = str2 + str(list[xy1]) + ","        # cała pętla polego na analizowaniu wrzucanego string w postaci np. 00010 tak, że jeśli jest 0 to przechodzi do kolejnego miejsca, a jeśli jest 1 to drukuję odpowiednią liczbę i dodaje ją do podzbioru
               
            
            xy1 += 1
        
        str2 = str2[:-1] + "}"
        print(str2)        #wyśwtl te podzbioru
        
    xy += 1
    







