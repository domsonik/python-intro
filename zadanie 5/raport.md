# Raport - Biblioteki Python do analizy i wizualizacji danych

## Wybrana dziedzina

**Analiza i wizualizacja danych** - jedna z najważniejszych dziedzin w dzisiejszym świecie data science, obejmująca przetwarzanie, analizę i prezentację danych w sposób zrozumiały i użyteczny.

## Wybrane biblioteki

### 1. pandas

**Przeznaczenie**: Manipulacja i analiza danych strukturalnych

**Główne funkcje**:

- Tworzenie i manipulacja struktur DataFrame i Series
- Wczytywanie i zapisywanie danych w formatach CSV, Excel, JSON, SQL
- Filtrowanie, grupowanie i agregacja danych
- Obsługa brakujących wartości i czyszczenie danych
- Operacje na indeksach, kolumnach i wierszach
- Łączenie i scalanie zbiorów danych
- Analiza statystyczna i opisowa

**Zalety**:

- **Intuicyjna składnia** podobna do SQL i R
- **Doskonała wydajność** przy średnich i dużych zbiorach danych
- **Bogata funkcjonalność** do czyszczenia i przekształcania danych
- **Seamless integracja** z NumPy, matplotlib i innymi bibliotekami
- **Obszerna dokumentacja** z licznymi przykładami
- **Aktywna społeczność** i regularne aktualizacje
- **Wsparcie dla różnych formatów** plików

**Ograniczenia**:

- **Większe zużycie pamięci** niż podstawowe struktury Pythona
- **Może być wolniejsza** od NumPy przy prostych operacjach numerycznych
- **Krzywa uczenia** dla zaawansowanych funkcji jak MultiIndex
- **Problemy z bardzo dużymi danymi** (powyżej dostępnej pamięci RAM)

### 2. matplotlib

**Przeznaczenie**: Tworzenie statycznych, animowanych i interaktywnych wizualizacji

**Główne funkcje**:

- Wykresy liniowe, słupkowe, punktowe, kołowe
- Histogramy, wykresy pudełkowe, violin plots
- Subploty i złożone układy wielopanelowe
- Pełna kontrola nad stylami, kolorami i formatowaniem
- Eksport do formatów PNG, PDF, SVG, EPS
- Tworzenie animacji i wykresów interaktywnych
- Obsługa LaTeX do renderowania tekstu matematycznego

**Zalety**:

- **Maksymalna elastyczność** i kontrola nad każdym elementem
- **Publikacyjna jakość** wykresów
- **Kompatybilność** z pandas, NumPy i SciPy
- **Podstawa dla innych bibliotek** wizualizacyjnych (seaborn, plotly)
- **Bogata galeria przykładów** w dokumentacji
- **Stabilność** i długa historia rozwoju
- **Wsparcie dla różnych backend-ów** renderowania

**Ograniczenia**:

- **Skomplikowana składnia** dla początkujących
- **Domyślne style** nie zawsze estetyczne
- **Ograniczona interaktywność** bez dodatkowych narzędzi
- **Może być wolna** przy bardzo złożonych wizualizacjach
- **Wymaga więcej kodu** do osiągnięcia efektów niż nowsze biblioteki

### 3. seaborn (biblioteka dodatkowa)

**Przeznaczenie**: Statystyczna wizualizacja danych oparta na matplotlib

**Główne funkcje**:

- Wykresy statystyczne (heatmapy, box plots, violin plots)
- Automatyczne obliczanie i wizualizacja korelacji
- Integracja z pandas DataFrame
- Wbudowane tematy i palety kolorów
- Funkcje do wizualizacji rozkładów i relacji

**Zalety**:

- **Prostsza składnia** niż matplotlib
- **Piękne domyślne style** i palety kolorów
- **Automatyczne obliczenia statystyczne**
- **Doskonała integracja** z pandas
- **Mniej kodu** do tworzenia złożonych wizualizacji

**Ograniczenia**:

- **Mniejsza elastyczność** niż matplotlib
- **Ograniczona do analiz statystycznych**
- **Zależność od matplotlib** może powodować konflikty wersji

## Przykłady zastosowań

### pandas

1. **Analiza sprzedażowa** - przetwarzanie danych miesięcznych, obliczanie zysków, identyfikacja trendów
2. **Analiza HR** - grupowanie pracowników, statystyki działów, kategoryzacja wiekowa

### matplotlib

1. **Dashboard sprzedażowy** - wykresy liniowe, słupkowe, obszarowe i punktowe w jednym układzie
2. **Analiza zasobów ludzkich** - wykresy kołowe, histogramy, scatter plots i wykresy poziome

### seaborn

1. **Analiza korelacji** - heatmapy, box plots, scatter plots z dodatkowymi wymiarami

## Instalacja

pip install pandas matplotlib seaborn numpy

## Linki do dokumentacji

- **pandas**: https://pandas.pydata.org/docs/
- **matplotlib**: https://matplotlib.org/stable/contents.html
- **seaborn**: https://seaborn.pydata.org/

## Repozytoria GitHub

- **pandas**: https://github.com/pandas-dev/pandas
- **matplotlib**: https://github.com/matplotlib/matplotlib
- **seaborn**: https://github.com/mwaskom/seaborn

## Podsumowanie

Wybrane biblioteki tworzą kompletny ekosystem do analizy i wizualizacji danych. **pandas** zapewnia potężne narzędzia do manipulacji danych, **matplotlib** oferuje maksymalną kontrolę nad wizualizacjami, a **seaborn** upraszcza tworzenie wykresów statystycznych. Razem umożliwiają realizację pełnego cyklu analizy danych - od wczytania i przetworzenia po prezentację wyników w formie profesjonalnych wykresów.

Te biblioteki są standardem w branży data science i stanowią fundament dla bardziej zaawansowanych narzędzi. Ich znajomość jest niezbędna dla każdego, kto pracuje z danymi w Pythonie.
