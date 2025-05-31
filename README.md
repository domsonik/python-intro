# Data Science Toolkit

Kompleksowa biblioteka Python dostarczająca narzędzia do analizy danych, operacji matematycznych i przetwarzania tekstu powszechnie używanych w projektach data science.

## 🚀 Opis

Data Science Toolkit to profesjonalna biblioteka Python stworzona zgodnie z najlepszymi praktykami programistycznymi. Biblioteka oferuje trzy główne moduły funkcjonalności:

- **Przetwarzanie danych** - narzędzia do ładowania, czyszczenia i transformacji danych
- **Operacje matematyczne** - zaawansowane obliczenia statystyczne i analiza numeryczna
- **Przetwarzanie tekstu** - funkcje NLP do analizy i czyszczenia tekstu

## 📦 Funkcjonalności

### 📊 Moduł Danych (`data_utils`)

- **DataProcessor** - kompleksowa klasa do przetwarzania danych z walidacją
- **load_csv_safe** - bezpieczne ładowanie plików CSV z wykrywaniem kodowania
- **normalize_data** - normalizacja danych (MinMax, Z-score, Robust)

### 🧮 Moduł Matematyczny (`math_tools`)

- **StatisticalCalculator** - zaawansowana analiza statystyczna i testowanie hipotez
- **advanced_mean** - obliczenia różnych typów średnich (arytmetyczna, geometryczna, harmoniczna, kwadratowa)
- **correlation_matrix** - analiza korelacji z metodami Pearson, Spearman, Kendall
- **moving_average** - średnie ruchome (proste i wykładnicze)

### 📝 Moduł Tekstowy (`text_processing`)

- **TextAnalyzer** - kompleksowa analiza tekstu i ekstrakcja cech
- **clean_text** - zaawansowane czyszczenie i preprocessing tekstu
- **extract_keywords** - ekstrakcja słów kluczowych na podstawie częstotliwości
- **text_similarity** - podobieństwo tekstu (Jaccard, Cosine)

## 🛠️ Instalacja

### Wymagania

- Python 3.8+
- numpy >= 1.21.0
- pandas >= 1.3.0
- scipy >= 1.7.0

### Instalacja ze źródła

git clone https://github.com/domsonik/data-science-toolkit.git
cd data-science-toolkit
pip install -e .

### Instalacja zależności

pip install -r requirements.txt

## 📁 Struktura Projektu

data_science_toolkit/
├── data_science_toolkit/ # Główny pakiet biblioteki
│ ├── init.py # Inicjalizacja pakietu
│ ├── data_utils.py # Narzędzia do przetwarzania danych
│ ├── math_tools.py # Narzędzia matematyczne i statystyczne
│ └── text_processing.py # Narzędzia do przetwarzania tekstu
├── tests/ # Testy jednostkowe
│ ├── init.py
│ ├── test_data_utils.py
│ ├── test_math_tools.py
│ └── test_text_processing.py
├── README.md # Dokumentacja projektu
├── setup.py # Konfiguracja instalacji
├── requirements.txt # Zależności
├── .gitignore # Pliki ignorowane przez Git
└── LICENSE # Licencja MIT

## 📄 Licencja

Ten projekt jest licencjonowany na **licencji MIT** - zobacz plik [LICENSE](LICENSE) dla szczegółów.

## 👥 Autorzy

- **Dominik** - _Autor główny_ - [GitHub](https://github.com/domsonik)

### 🔄 Planowane funkcjonalności

- [ ] Obsługa więcej formatów danych (JSON, XML)
- [ ] Zaawansowane algorytmy ML
- [ ] Wizualizacja danych
- [ ] Optymalizacja wydajności
- [ ] Integracja z Jupyter Notebook

## 🆘 Wsparcie

Jeśli napotkasz problemy lub masz pytania:

1. Sprawdź [Issues](https://github.com/domsonik/data-science-toolkit/issues)
2. Stwórz nowy Issue z opisem problemu
3. Skontaktuj się: naworskidominik@gmail.com

---

**Data Science Toolkit** - Twoje narzędzie do profesjonalnej analizy danych w Python! 🐍📊