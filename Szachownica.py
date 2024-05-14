import random
running = True
k = 1
queens_coordinates = []
pawn_coordinates = []
#Funkcja sprawdzająca czy można zbić pionka
def can_pawn_be_taken(board):
    pawn_taken = False
    for row in board:
        if '[Q]' in row:
            pawn_taken = True
    if pawn_taken == True:
        print("Pionek może zostać zbity.")
    else:
        print("Pionek nie może zostać zbity.")
    return pawn_taken
#Funkcja generująca szachownice
def generate_chessboard():
    #Generowanie pustej szachownicy
    chessboard = [['[ ]' for space in range(8)] for rows in range(8)]
    queens = 0
    pawns = 0
    #Dodawanie Pionka
    while pawns < 1:
        pawn_x = random.randint(0,7)
        pawn_y = random.randint(0,7)
        if chessboard[pawn_x][pawn_y] == '[ ]':
            chessboard[pawn_x][pawn_y] = '[P]'
            pawns += 1
            pawn_coordinates.append(pawn_x)
            pawn_coordinates.append(pawn_y)
    #Dodawanie Hetmanów
    while queens < k:
        queen_x = random.randint(0,7)
        queen_y = random.randint(0,7)
        if chessboard[queen_x][queen_y] == '[ ]':
            if queen_x == pawn_x or queen_y == pawn_y or abs(pawn_x-queen_x) == abs(pawn_y-queen_y):
                chessboard[queen_x][queen_y] = '[Q]'
                queens_coordinates.append([queen_x,queen_y])
                print("Koordynaty Hetmana który może zbić pionka: rząd: ",queen_x," kolumna: ",queen_y)
            else:
                chessboard[queen_x][queen_y] = '[q]'
                queens_coordinates.append([queen_x,queen_y])
            queens += 1



    return chessboard
#Funkcja wyświetlająca szachownice
def print_chessboard(board):
    for row in board:
        print(''.join(row))
#Funkcja losująca nową pozycje pionka

chessboard = generate_chessboard()
print_chessboard(chessboard)
can_pawn_be_taken(chessboard)

def new_pawn(board):
    pawns = 0
    queens = 0
    board[pawn_coordinates[0]][pawn_coordinates[1]] = '[ ]'
    pawn_coordinates.remove(pawn_coordinates[0])
    pawn_coordinates.remove(pawn_coordinates[0])
    while pawns < 1:
        pawn_x = random.randint(0,7)
        pawn_y = random.randint(0,7)
        if chessboard[pawn_x][pawn_y] == '[ ]':
            chessboard[pawn_x][pawn_y] = '[P]'
            pawns += 1
            pawn_coordinates.append(pawn_x)
            pawn_coordinates.append(pawn_y)
    for cords in queens_coordinates:
        board[cords[0]][cords[1]] = '[q]'
        if cords[0] == pawn_x or cords[1] == pawn_y or abs(pawn_x-cords[0]) == abs(pawn_y-cords[1]):
            print("Koordynaty Hetmana który może zbić pionka: rząd: ",cords[0]," kolumna: ",cords[1])
            board[cords[0]][cords[1]] = '[Q]'
    return board

def delete_queen(board,x,y):
    if board[x][y] == '[Q]' or '[q]':
        board[x][y] = '[ ]'
        print("Usunięto królową.")
        queens_coordinates.remove([x,y])
    else:
        print("Podano błędne dane.")
while running == True:
    print("Wybierz jedną z opcji 1/2/3/4")
    print("1 - Wylosuj nową pozycje pionka z pozostawieniem pierwotnego układu hetmanów")
    print("2 - Usuń dowolnego hetmana")
    print("3 - Ponowna weryfikacja bicia po ustaleniu zmian")
    print("4 - Opuść program")
    choice = input()
    if choice == '1':
        chessboard = new_pawn(chessboard)
        print_chessboard(chessboard)
    if choice == '2':
        print("Podaj numer wiersza królowej do usunięcia (0-7)")
        cordx = int(input())
        print("Podaj numer kolumny królowej do usunięcia (0-7)")
        cordy = int(input())
        delete_queen(chessboard,cordx,cordy)
        print_chessboard(chessboard)
    if choice == '3':
        can_pawn_be_taken(chessboard)
    if choice == '4':
        running = False
    elif choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print("Wybierz właściwy numer.")

