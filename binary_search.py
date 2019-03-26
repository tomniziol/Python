def binary_search(value, data):  # value to szukana liczba, data to przeszukiwana lista
   
    start = 0  # lewa granica, pozycja początowa dla przeszukiwanej listy
    end = len(data) - 1  # prawa granica, numer ostatniej pozycji na przeszukiwanej liście

    while start < end:  # szukaj dopóki początek przeszukiwanej listy jest mniejszy od jej końca
        middle = (start + end) // 2  # oznaczamy pozycję elementu środkowego na przeszukiwanej liście
        if data[middle] < value:  # jeżeli element środkowy jest mniejszy od szukanego
            start = middle + 1  # to odrzuć lewą połowę bo nie ma w niej szukanej liczny i przesuwam lewą granice na początek prawej połowy
        else:  # w przeciwnym razie, jeżeli element środkowy jest większy od szukanej liczby to
            end = middle  # odrzuca prawą połowę bo nie ma w niej szukanej liczby (przesuwam prawą granice na środek)

    if data[end] == value:  # sprawdź czy znaleziona liczba to szukana wartość
        return "Szukana liczba {} jest na liście.".format(value)
    else:
        return "Nie ma szukanej liczby"

list = [0, 12, 2, 1, 3, 5, 11, 8, 9]
list.sort() # sortowanie liczb na przeszukiwaniej liście
print(binary_search(11,x))