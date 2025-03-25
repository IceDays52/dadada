import  math #importuje biblioteke math do obliczen z uzyciem sqrt czyli pierwiastka

def nwd(a, b):  # funkcja nwd 
   if b == 0 : # jezeli b=0 to dalej robimy
       return a #zwraca a 

   else: 
        
       return nwd(b, a % b) # rekurencja dzieje tu to ze jezeli b nie jest rowne 0 to zwraca nwd z b i reszta z dzielenia a przez b i znow zachodzi funckja i tak w kolko dopoki nie osiagniemy b = 0 bo szukamy najwiekszego wspolneg dzielnika


    
   pary_liczb = [(56,98), (48,180), (21,35)] #wartosc uzyte


for a, b in pary_liczb: #petla dla kazdej pary liczb gdzie przypisuje do a i b przykladwe wartosci z pary_liczb
    print(f"NWD({a}, {b}) = {nwd(a, b)}") #wypisuje wynik nwd dla kazdej pary liczb
 

  
          
def miejscazerowe(a, b, c): #wytworzenie funkcji z 3 wartosciami a,b,c
   
  delta =(b*b) - (4*a*c) #liczenie delty
  if delta > 0: #jezeli delta jest wieksza od 0 to robi x1 i x2 i zwraca 
      x1 = (-b + math.sqrt(delta))/(2 * a) #obliczenia
      x2 = (-b - math.sqrt(delta))/(2 * a) #obliczenia
      return f"sa miejsca zerowe {round(x1,2)} i {round(x2,2)}" #zwraca wynik x1 i x2 zaokraglone do 2 liczb
  elif delta == 0: # sprawdza jest z warunkow delta =0 jestli tak to robi
  
     x3 = (-b/(2*a)) # x3 obliczenia
  
    return round(x3,2) #wyrzuca wynik x3 zaokrglony do 2 liczb
    
if delta < 0: #spprawdze delte 

return "brak miejsc zerowych" # wyrzuca dane w kwestii braku miejsc

# funkcje = [[1,2,-4],[5,9,2],[4,6,8],]
# for (a,b,c) in funkcje: 
#    print(miejscazerowe(a,b,c))
   
def funkcja_skrotu(liczba): # funkcja utworzna z zawartoscia liczba 
    try:  #try i excep to blok ktory sprawdza czy liczba jest liczba jesli nie jest literkami to wypisuje blad ale uzywamy tego dlatego zeby program nie przestal dzialac
        liczba = int(liczba)  # Zamiana stringa na liczbê
    except ValueError:
        print(f"Blad: '{liczba}' nie jest liczba!")
        return -1  # Zwracamy -1 w przypadku b³êdu

    while liczba >= 10:  # Dopóki liczby ktora sa dodawane sa wiekszy badz rowne 10
        liczba = sum(int(i) for i in str(liczba))  #sumuje roZczepione liczby ze soba
    return liczba   # zwraca liczbe


testwartosci = ["9875","a1b2", "44141481", "414718", "12", "41841"] # testowe wartosci dla tej fukncji
for liczba in testwartosci: # dla kazdej wartosc z testwartosci zeby srawdzic czy dziala
    wynik = funkcja_skrotu(liczba) # wynik funkcji
   # if wynik != -1: # jesli wynik nie jest -1 to wypisuje wartosc
print(f"Wartosc {liczba} -> {wynik}") # koniec wartosc dane