import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class DataProcessor:
    def __init__(self):
        self.processed_data = None
        self.original_shape = None
    
    def load_and_validate(self, data: Union[pd.DataFrame, str, Dict]) -> pd.DataFrame:
        if isinstance(data, pd.DataFrame):
            df = data.copy()
        elif isinstance(data, str):
            try:
                df = pd.read_csv(data)
            except FileNotFoundError:
                raise FileNotFoundError(f"Plik nie został znaleziony: {data}")
        elif isinstance(data, dict):
            df = pd.DataFrame(data)
        else:
            raise ValueError("Nieobsługiwany format danych")
        
        self.original_shape = df.shape
        logger.info(f"Dane załadowane pomyślnie. Kształt: {df.shape}")
        return df
    
    def remove_duplicates(self, df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
        initial_count = len(df)
        df_clean = df.drop_duplicates(subset=subset)
        removed_count = initial_count - len(df_clean)
        
        if removed_count > 0:
            logger.info(f"Usunięto {removed_count} duplikatów wierszy")
        
        return df_clean


def load_csv_safe(file_path: str, encoding: str = 'utf-8', **kwargs) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, encoding=encoding, **kwargs)
        logger.info(f"Pomyślnie załadowano {file_path} o kształcie {df.shape}")
        return df
    except UnicodeDecodeError:
        logger.warning(f"Kodowanie UTF-8 nie powiodło się, próba latin-1 dla {file_path}")
        return pd.read_csv(file_path, encoding='latin-1', **kwargs)
    except Exception as e:
        logger.error(f"Nie udało się załadować {file_path}: {str(e)}")
        raise


def normalize_data(data: Union[pd.Series, np.ndarray, List], method: str = 'minmax') -> np.ndarray:
    data_array = np.array(data)
    
    if method == 'minmax':
        min_val, max_val = np.min(data_array), np.max(data_array)
        if max_val == min_val:
            return np.zeros_like(data_array)
        return (data_array - min_val) / (max_val - min_val)
    
    elif method == 'zscore':
        mean_val, std_val = np.mean(data_array), np.std(data_array)
        if std_val == 0:
            return np.zeros_like(data_array)
        return (data_array - mean_val) / std_val
    
    elif method == 'robust':
        median_val = np.median(data_array)
        mad = np.median(np.abs(data_array - median_val))
        if mad == 0:
            return np.zeros_like(data_array)
        return (data_array - median_val) / mad
    
    else:
        raise ValueError(f"Nieobsługiwana metoda normalizacji: {method}")
