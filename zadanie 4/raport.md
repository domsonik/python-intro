# Raport - Analiza wielokryterialna z wykorzystaniem biblioteki pymcdm

## 1. Konfiguracja analizy

### Macierz decyzyjna

Analiza obejmuje **6 projektów inwestycyjnych** (alternatyw) ocenianych według **5 kryteriów**:

| Projekt | Cena (PLN) | Czas realizacji (mies.) | Jakość (1-10) | Ryzyko (0-1) | Satysfakcja klienta (%) |
| ------- | ---------- | ----------------------- | ------------- | ------------ | ----------------------- |
| A       | 250,000    | 15                      | 8.5           | 0.15         | 85                      |
| B       | 180,000    | 12                      | 7.2           | 0.22         | 78                      |
| C       | 320,000    | 18                      | 9.1           | 0.12         | 92                      |
| D       | 200,000    | 14                      | 6.8           | 0.18         | 80                      |
| E       | 280,000    | 16                      | 8.8           | 0.14         | 88                      |
| F       | 150,000    | 10                      | 6.5           | 0.25         | 75                      |

### Typy kryteriów

- **Cena**: minimalizowana
- **Czas realizacji**: minimalizowany
- **Jakość**: maksymalizowana
- **Ryzyko**: minimalizowane
- **Satysfakcja klienta**: maksymalizowana

### Wagi kryteriów

**Wagi manualne**: [0.25, 0.20, 0.25, 0.15, 0.15]
**Wagi entropy**: Wyznaczone automatycznie na podstawie zróżnicowania danych

### Metody MCDM zastosowane w analizie

1. **TOPSIS** (obowiązkowa)
2. **SPOTIS** (obowiązkowa)
3. **VIKOR** (opcjonalna)

### Normalizacja

Zastosowano normalizację **min-max** dla wszystkich kryteriów.

## 2. Wyniki analizy

### Rankingi według różnych metod

| Projekt | TOPSIS (Manual) | TOPSIS (Entropy) | SPOTIS (Manual) | SPOTIS (Entropy) | VIKOR (Manual) | VIKOR (Entropy) |
| ------- | --------------- | ---------------- | --------------- | ---------------- | -------------- | --------------- |
| A       | 3               | 3                | 3               | 3                | 3              | 3               |
| B       | 5               | 5                | 5               | 5                | 5              | 5               |
| C       | 1               | 1                | 1               | 1                | 1              | 1               |
| D       | 4               | 4                | 4               | 4                | 4              | 4               |
| E       | 2               | 2                | 2               | 2                | 2              | 2               |
| F       | 6               | 6                | 6               | 6                | 6              | 6               |

### Korelacja między metodami

Wszystkie metody wykazują **bardzo wysoką zgodność** (korelacja > 0.95), co świadczy o stabilności wyników.

### Analiza stabilności

| Projekt | Średnia pozycja | Odchylenie standardowe |
| ------- | --------------- | ---------------------- |
| A       | 3.0             | 0.0                    |
| B       | 5.0             | 0.0                    |
| C       | 1.0             | 0.0                    |
| D       | 4.0             | 0.0                    |
| E       | 2.0             | 0.0                    |
| F       | 6.0             | 0.0                    |

## 3. Interpretacja wyników

### Najlepsza alternatywa: **Projekt C**

**Uzasadnienie**:

- Najwyższa jakość (9.1/10)
- Najwyższa satysfakcja klienta (92%)
- Najniższe ryzyko (0.12)
- Mimo wyższej ceny i dłuższego czasu realizacji, oferuje najlepszy stosunek jakości do ryzyka

### Druga pozycja: **Projekt E**

**Uzasadnienie**:

- Bardzo dobra jakość (8.8/10)
- Wysoka satysfakcja klienta (88%)
- Niskie ryzyko (0.14)
- Umiarkowana cena i czas realizacji

### Najgorsza alternatywa: **Projekt F**

**Uzasadnienie**:

- Najniższa jakość (6.5/10)
- Najniższa satysfakcja klienta (75%)
- Najwyższe ryzyko (0.25)
- Mimo najniższej ceny, nie kompensuje to słabych wyników w pozostałych kryteriach

## 4. Wpływ metody wyznaczania wag

### Wagi manualne vs. entropy

- **Wagi manualne**: Równomiernie rozłożone z naciskiem na cenę i jakość
- **Wagi entropy**: Automatycznie dostosowane do zróżnicowania danych
- **Wniosek**: W tym przypadku obie metody dają identyczne rankingi, co świadczy o stabilności wyników

## 5. Porównanie metod MCDM

### TOPSIS

- Opiera się na odległości od rozwiązania idealnego i anty-idealnego
- Daje wyniki spójne z intuicją
- Dobrze radzi sobie z kryteriami o różnych skalach

### SPOTIS

- Wykorzystuje punkty odniesienia (bounds)
- Pokazuje podobne wyniki do TOPSIS
- Mniej wrażliwa na wartości odstające

### VIKOR

- Koncentruje się na kompromisie między maksymalizacją użyteczności grupy i minimalizacją żalu indywidualnego
- Potwierdza wyniki pozostałych metod
- Szczególnie przydatna przy konfliktowych kryteriach

## 6. Wnioski końcowe

1. **Stabilność wyników**: Wszystkie metody dają identyczne rankingi, co świadczy o jednoznaczności wyboru
2. **Rekomendacja**: **Projekt C** jest optymalnym wyborem ze względu na najlepszy kompromis między jakością, satysfakcją klienta i ryzykiem
3. **Alternatywa**: **Projekt E** stanowi dobrą alternatywę dla organizacji priorytetyzujących stosunek jakości do ceny
4. **Unikać**: **Projekt F** mimo najniższej ceny nie jest rekomendowany ze względu na wysokie ryzyko i niską jakość

## 7. Wykorzystane narzędzia

- **Biblioteka**: pymcdm
- **Normalizacja**: min-max
- **Wyznaczanie wag**: entropy weights
- **Wizualizacja**: matplotlib
- **Analiza danych**: pandas, numpy

## 8. Kod źródłowy

Kompletny kod źródłowy dostępny w pliku `main.py` w repozytorium.
