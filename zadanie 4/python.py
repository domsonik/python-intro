import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.helpers import rrankdata
from pymcdm.normalizations import minmax_normalization
from pymcdm.weights import entropy_weights
import matplotlib.pyplot as plt

alts = np.array([
    [250000, 15, 8.5, 0.15, 85],
    [180000, 12, 7.2, 0.22, 78],
    [320000, 18, 9.1, 0.12, 92],
    [200000, 14, 6.8, 0.18, 80],
    [280000, 16, 8.8, 0.14, 88],
    [150000, 10, 6.5, 0.25, 75]
])

criteria_names = ['Cena', 'Czas realizacji', 'Jakość', 'Ryzyko', 'Satysfakcja klienta']
alternative_names = ['Projekt A', 'Projekt B', 'Projekt C', 'Projekt D', 'Projekt E', 'Projekt F']

weights_manual = np.array([0.25, 0.20, 0.25, 0.15, 0.15])
types = np.array([-1, -1, 1, -1, 1])

weights_entropy = entropy_weights(alts)

normalized_alts = minmax_normalization(alts, types)

topsis = TOPSIS()
pref_topsis_manual = topsis(alts, weights_manual, types)
ranking_topsis_manual = rrankdata(pref_topsis_manual)

pref_topsis_entropy = topsis(alts, weights_entropy, types)
ranking_topsis_entropy = rrankdata(pref_topsis_entropy)

bounds = np.array([
    [alts[:, 0].min(), alts[:, 0].max()],
    [alts[:, 1].min(), alts[:, 1].max()],
    [alts[:, 2].min(), alts[:, 2].max()],
    [alts[:, 3].min(), alts[:, 3].max()],
    [alts[:, 4].min(), alts[:, 4].max()]
])

spotis = SPOTIS(bounds)
pref_spotis_manual = spotis(alts, weights_manual, types)
ranking_spotis_manual = rrankdata(pref_spotis_manual)

pref_spotis_entropy = spotis(alts, weights_entropy, types)
ranking_spotis_entropy = rrankdata(pref_spotis_entropy)

vikor = VIKOR()
pref_vikor_manual = vikor(alts, weights_manual, types)
ranking_vikor_manual = rrankdata(pref_vikor_manual)

pref_vikor_entropy = vikor(alts, weights_entropy, types)
ranking_vikor_entropy = rrankdata(pref_vikor_entropy)

results_df = pd.DataFrame({
    'Alternatywa': alternative_names,
    'TOPSIS (Manual)': ranking_topsis_manual,
    'TOPSIS (Entropy)': ranking_topsis_entropy,
    'SPOTIS (Manual)': ranking_spotis_manual,
    'SPOTIS (Entropy)': ranking_spotis_entropy,
    'VIKOR (Manual)': ranking_vikor_manual,
    'VIKOR (Entropy)': ranking_vikor_entropy
})

preferences_df = pd.DataFrame({
    'Alternatywa': alternative_names,
    'TOPSIS (Manual)': pref_topsis_manual,
    'TOPSIS (Entropy)': pref_topsis_entropy,
    'SPOTIS (Manual)': pref_spotis_manual,
    'SPOTIS (Entropy)': pref_spotis_entropy,
    'VIKOR (Manual)': pref_vikor_manual,
    'VIKOR (Entropy)': pref_vikor_entropy
})

print("=== MACIERZ DECYZYJNA ===")
decision_matrix_df = pd.DataFrame(alts, 
                                 index=alternative_names, 
                                 columns=criteria_names)
print(decision_matrix_df)

print("\n=== WAGI KRYTERIÓW ===")
weights_df = pd.DataFrame({
    'Kryterium': criteria_names,
    'Wagi manualne': weights_manual,
    'Wagi entropy': weights_entropy,
    'Typ': ['MIN' if t == -1 else 'MAX' for t in types]
})
print(weights_df)

print("\n=== RANKINGI ===")
print(results_df)

print("\n=== WARTOŚCI PREFERENCJI ===")
print(preferences_df.round(4))

correlation_matrix = results_df.iloc[:, 1:].corr()
print("\n=== KORELACJA MIĘDZY METODAMI ===")
print(correlation_matrix.round(3))

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

methods = ['TOPSIS (Manual)', 'SPOTIS (Manual)', 'VIKOR (Manual)',
           'TOPSIS (Entropy)', 'SPOTIS (Entropy)', 'VIKOR (Entropy)']
colors = ['skyblue', 'lightgreen', 'orange', 'salmon', 'gold', 'lightcoral']

for i, (method, color) in enumerate(zip(methods, colors)):
    row = i // 3
    col = i % 3
    ranking_data = results_df[method]
    axes[row, col].bar(alternative_names, ranking_data, color=color, alpha=0.7)
    axes[row, col].set_title(method)
    axes[row, col].set_ylabel('Ranking')
    axes[row, col].tick_params(axis='x', rotation=45)
    axes[row, col].set_ylim(0, 7)

plt.tight_layout()
plt.savefig('porownanie_wszystkich_metod.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n=== ANALIZA WYNIKÓW ===")
print("Najlepsza alternatywa według:")
for col in results_df.columns[1:]:
    best_alt_idx = np.argmin(results_df[col])
    print(f"- {col}: {results_df.iloc[best_alt_idx]['Alternatywa']}")

print("\nNajgorsza alternatywa według:")
for col in results_df.columns[1:]:
    worst_alt_idx = np.argmax(results_df[col])
    print(f"- {col}: {results_df.iloc[worst_alt_idx]['Alternatywa']}")

print("\n=== STABILNOŚĆ RANKINGÓW ===")
ranking_positions = results_df.iloc[:, 1:].values
mean_positions = np.mean(ranking_positions, axis=1)
std_positions = np.std(ranking_positions, axis=1)

stability_df = pd.DataFrame({
    'Alternatywa': alternative_names,
    'Średnia pozycja': mean_positions,
    'Odchylenie std': std_positions
})
print(stability_df.round(2))

normalized_data_df = pd.DataFrame(normalized_alts,
                                 index=alternative_names,
                                 columns=criteria_names)
print("\n=== ZNORMALIZOWANE DANE ===")
print(normalized_data_df.round(3))
