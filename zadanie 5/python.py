import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta

def pandas_przyklad_1():
    print("=== PANDAS - Przykład 1: Analiza danych sprzedażowych ===")
    
    dane = {
        'data': pd.date_range('2024-01-01', periods=12, freq='M'),
        'produkt_A': [1200, 1350, 1580, 1420, 1670, 1890, 2100, 1950, 1780, 1650, 1400, 1300],
        'produkt_B': [980, 1120, 1250, 1380, 1450, 1520, 1600, 1580, 1520, 1480, 1350, 1200],
        'koszty': [800, 850, 900, 920, 950, 980, 1000, 990, 970, 950, 900, 850]
    }
    
    df = pd.DataFrame(dane)
    df['zysk_A'] = df['produkt_A'] - df['koszty'] * 0.6
    df['zysk_B'] = df['produkt_B'] - df['koszty'] * 0.4
    df['zysk_calkowity'] = df['zysk_A'] + df['zysk_B']
    
    print("Pierwsze 5 wierszy danych:")
    print(df.head())
    print(f"\nŚredni miesięczny zysk: {df['zysk_calkowity'].mean():.2f}")
    print(f"Najlepszy miesiąc: {df.loc[df['zysk_calkowity'].idxmax(), 'data'].strftime('%B %Y')}")
    print(f"Najgorszy miesiąc: {df.loc[df['zysk_calkowity'].idxmin(), 'data'].strftime('%B %Y')}")
    
    df.to_csv('analiza_sprzedazy.csv', index=False)
    print("Dane zapisane do pliku analiza_sprzedazy.csv")
    
    return df

def pandas_przyklad_2():
    print("\n=== PANDAS - Przykład 2: Przetwarzanie danych pracowników ===")
    
    pracownicy = {
        'imie': ['Anna', 'Jan', 'Katarzyna', 'Piotr', 'Maria', 'Tomasz', 'Agnieszka', 'Michał'],
        'dzial': ['IT', 'HR', 'IT', 'Finanse', 'HR', 'IT', 'Finanse', 'IT'],
        'wiek': [28, 35, 31, 42, 29, 38, 45, 33],
        'pensja': [8000, 6500, 9500, 7200, 6800, 10500, 8500, 9000],
        'doswiadczenie': [3, 8, 5, 15, 4, 12, 18, 7]
    }
    
    df = pd.DataFrame(pracownicy)
    
    print("Statystyki według działów:")
    statystyki = df.groupby('dzial').agg({
        'pensja': ['mean', 'min', 'max'],
        'wiek': 'mean',
        'doswiadczenie': 'mean'
    }).round(2)
    print(statystyki)
    
    df['kategoria_wiek'] = pd.cut(df['wiek'], bins=[0, 30, 40, 100], labels=['Młody', 'Średni', 'Senior'])
    print(f"\nRozkład kategorii wiekowych:")
    print(df['kategoria_wiek'].value_counts())
    
    wysokie_pensje = df[df['pensja'] > df['pensja'].median()]
    print(f"\nPracownicy z pensjami powyżej mediany ({df['pensja'].median()}):")
    print(wysokie_pensje[['imie', 'dzial', 'pensja']])
    
    return df

def matplotlib_przyklad_1(df_sprzedaz):
    print("\n=== MATPLOTLIB - Przykład 1: Wizualizacja sprzedaży ===")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    ax1.plot(df_sprzedaz['data'], df_sprzedaz['produkt_A'], marker='o', linewidth=2, label='Produkt A')
    ax1.plot(df_sprzedaz['data'], df_sprzedaz['produkt_B'], marker='s', linewidth=2, label='Produkt B')
    ax1.set_title('Sprzedaż produktów w czasie', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Sprzedaż')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    ax2.bar(['Produkt A', 'Produkt B'], 
            [df_sprzedaz['produkt_A'].sum(), df_sprzedaz['produkt_B'].sum()],
            color=['#2E86AB', '#A23B72'], alpha=0.8)
    ax2.set_title('Łączna sprzedaż produktów', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Łączna sprzedaż')
    
    ax3.fill_between(df_sprzedaz['data'], df_sprzedaz['zysk_calkowity'], alpha=0.6, color='green')
    ax3.plot(df_sprzedaz['data'], df_sprzedaz['zysk_calkowity'], color='darkgreen', linewidth=2)
    ax3.set_title('Zysk całkowity w czasie', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Data')
    ax3.set_ylabel('Zysk')
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(axis='x', rotation=45)
    
    miesiecy = [d.strftime('%b') for d in df_sprzedaz['data']]
    ax4.scatter(df_sprzedaz['koszty'], df_sprzedaz['zysk_calkowity'], 
                s=100, alpha=0.7, c=range(len(df_sprzedaz)), cmap='viridis')
    ax4.set_title('Korelacja kosztów i zysków', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Koszty')
    ax4.set_ylabel('Zysk całkowity')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analiza_wizualna.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Wykres zapisany jako analiza_wizualna.png")

def matplotlib_przyklad_2(df_pracownicy):
    print("\n=== MATPLOTLIB - Przykład 2: Analiza danych HR ===")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    dzialy = df_pracownicy['dzial'].value_counts()
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    wedges, texts, autotexts = ax1.pie(dzialy.values, labels=dzialy.index, autopct='%1.1f%%', 
                                       colors=colors, startangle=90)
    ax1.set_title('Rozkład pracowników według działów', fontsize=14, fontweight='bold')
    
    ax2.hist(df_pracownicy['pensja'], bins=8, alpha=0.7, color='skyblue', edgecolor='black')
    ax2.axvline(df_pracownicy['pensja'].mean(), color='red', linestyle='--', 
                label=f'Średnia: {df_pracownicy["pensja"].mean():.0f}')
    ax2.set_title('Rozkład pensji', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Pensja')
    ax2.set_ylabel('Liczba pracowników')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    for i, dzial in enumerate(df_pracownicy['dzial'].unique()):
        dane_dzial = df_pracownicy[df_pracownicy['dzial'] == dzial]
        ax3.scatter(dane_dzial['doswiadczenie'], dane_dzial['pensja'], 
                   label=dzial, s=100, alpha=0.7, color=colors[i])
    ax3.set_title('Doświadczenie vs Pensja według działów', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Lata doświadczenia')
    ax3.set_ylabel('Pensja')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    pensje_dzial = df_pracownicy.groupby('dzial')['pensja'].mean().sort_values(ascending=True)
    bars = ax4.barh(pensje_dzial.index, pensje_dzial.values, color=colors[:len(pensje_dzial)])
    ax4.set_title('Średnia pensja według działów', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Średnia pensja')
    
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax4.text(width + 100, bar.get_y() + bar.get_height()/2, 
                f'{width:.0f}', ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('analiza_hr.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Wykres zapisany jako analiza_hr.png")

def seaborn_przyklad():
    print("\n=== SEABORN - Przykład: Zaawansowana wizualizacja ===")
    
    np.random.seed(42)
    dane_korelacji = pd.DataFrame({
        'wiek': np.random.normal(35, 8, 100),
        'doswiadczenie': np.random.normal(8, 4, 100),
        'pensja': np.random.normal(8000, 2000, 100),
        'ocena': np.random.normal(4.2, 0.5, 100),
        'nadgodziny': np.random.normal(10, 5, 100)
    })
    
    dane_korelacji['pensja'] = dane_korelacji['pensja'] + dane_korelacji['doswiadczenie'] * 200
    dane_korelacji['ocena'] = np.clip(dane_korelacji['ocena'], 1, 5)
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    correlation_matrix = dane_korelacji.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.2f')
    plt.title('Macierz korelacji', fontsize=14, fontweight='bold')
    
    plt.subplot(2, 2, 2)
    sns.boxplot(data=dane_korelacji[['pensja', 'ocena', 'nadgodziny']])
    plt.title('Rozkład zmiennych', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    plt.subplot(2, 2, 3)
    sns.scatterplot(data=dane_korelacji, x='doswiadczenie', y='pensja', 
                    size='ocena', alpha=0.7)
    plt.title('Doświadczenie vs Pensja (rozmiar = ocena)', fontsize=14, fontweight='bold')
    
    plt.subplot(2, 2, 4)
    sns.violinplot(data=dane_korelacji, y='pensja')
    plt.title('Rozkład pensji (violin plot)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('analiza_seaborn.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Wykres zapisany jako analiza_seaborn.png")

def main():
    print("DEMONSTRACJA BIBLIOTEK DO ANALIZY I WIZUALIZACJI DANYCH")
    print("=" * 60)
    
    df_sprzedaz = pandas_przyklad_1()
    df_pracownicy = pandas_przyklad_2()
    
    matplotlib_przyklad_1(df_sprzedaz)
    matplotlib_przyklad_2(df_pracownicy)
    
    try:
        import seaborn as sns
        seaborn_przyklad()
    except ImportError:
        print("\nSeaborn nie jest zainstalowany. Pomiń ten przykład lub zainstaluj: pip install seaborn")
    
    print("\n" + "=" * 60)
    print("DEMONSTRACJA ZAKOŃCZONA")
    print("Wygenerowane pliki:")
    print("- analiza_sprzedazy.csv")
    print("- analiza_wizualna.png") 
    print("- analiza_hr.png")
    print("- analiza_seaborn.png")

if __name__ == "__main__":
    main()
