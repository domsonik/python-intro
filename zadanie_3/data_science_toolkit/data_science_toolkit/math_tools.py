import numpy as np
import pandas as pd
from typing import Union, List, Tuple, Optional, Dict
import math
from scipy import stats
import warnings


class StatisticalCalculator:
    
    def __init__(self):
        self.last_calculation = None
        self.calculation_history = []
    
    def descriptive_stats(self, data: Union[List, np.ndarray, pd.Series]) -> Dict[str, float]:
        data_array = np.array(data)
        
        if len(data_array) == 0:
            raise ValueError("Dane wejściowe nie mogą być puste")
        
        stats_dict = {
            'count': len(data_array),
            'mean': np.mean(data_array),
            'median': np.median(data_array),
            'std': np.std(data_array, ddof=1),
            'var': np.var(data_array, ddof=1),
            'min': np.min(data_array),
            'max': np.max(data_array),
            'q25': np.percentile(data_array, 25),
            'q75': np.percentile(data_array, 75),
            'skewness': stats.skew(data_array),
            'kurtosis': stats.kurtosis(data_array)
        }
        
        self.last_calculation = stats_dict
        self.calculation_history.append(('descriptive_stats', stats_dict))
        
        return stats_dict
    
    def confidence_interval(self, data: Union[List, np.ndarray], confidence: float = 0.95) -> Tuple[float, float]:
        data_array = np.array(data)
        n = len(data_array)
        
        if n < 2:
            raise ValueError("Potrzeba co najmniej 2 punktów danych dla przedziału ufności")
        
        mean = np.mean(data_array)
        std_err = stats.sem(data_array)
        h = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
        
        return (mean - h, mean + h)


def advanced_mean(data: Union[List, np.ndarray], method: str = 'arithmetic') -> float:
    data_array = np.array(data)
    
    if len(data_array) == 0:
        raise ValueError("Dane wejściowe nie mogą być puste")
    
    if method == 'arithmetic':
        return np.mean(data_array)
    
    elif method == 'geometric':
        if np.any(data_array <= 0):
            raise ValueError("Średnia geometryczna wymaga wszystkich wartości dodatnich")
        return stats.gmean(data_array)
    
    elif method == 'harmonic':
        if np.any(data_array <= 0):
            raise ValueError("Średnia harmoniczna wymaga wszystkich wartości dodatnich")
        return stats.hmean(data_array)
    
    elif method == 'quadratic':
        return np.sqrt(np.mean(data_array ** 2))
    
    else:
        raise ValueError(f"Nieobsługiwana metoda średniej: {method}")


def correlation_matrix(data: pd.DataFrame, method: str = 'pearson') -> pd.DataFrame:
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Dane wejściowe muszą być pandas DataFrame")
    
    numeric_data = data.select_dtypes(include=[np.number])
    
    if numeric_data.empty:
        raise ValueError("DataFrame musi zawierać kolumny numeryczne")
    
    if method in ['pearson', 'spearman', 'kendall']:
        return numeric_data.corr(method=method)
    else:
        raise ValueError(f"Nieobsługiwana metoda korelacji: {method}")


def moving_average(data: Union[List, np.ndarray], window: int, method: str = 'simple') -> np.ndarray:
    data_array = np.array(data)
    
    if window <= 0 or window > len(data_array):
        raise ValueError("Nieprawidłowy rozmiar okna")
    
    if method == 'simple':
        return np.convolve(data_array, np.ones(window)/window, mode='valid')
    
    elif method == 'exponential':
        alpha = 2.0 / (window + 1)
        result = np.zeros(len(data_array))
        result[0] = data_array[0]
        
        for i in range(1, len(data_array)):
            result[i] = alpha * data_array[i] + (1 - alpha) * result[i-1]
        
        return result
    
    else:
        raise ValueError(f"Nieobsługiwana metoda średniej ruchomej: {method}")
