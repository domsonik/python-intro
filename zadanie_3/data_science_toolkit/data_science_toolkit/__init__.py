__version__ = "1.0.0"
__author__ = "Dominik"
__email__ = "naworskidominik@gmail.com"

from .data_utils import DataProcessor, load_csv_safe, normalize_data
from .math_tools import StatisticalCalculator, advanced_mean, correlation_matrix
from .text_processing import TextAnalyzer, clean_text, extract_keywords

__all__ = [
    'DataProcessor',
    'load_csv_safe', 
    'normalize_data',
    'StatisticalCalculator',
    'advanced_mean',
    'correlation_matrix',
    'TextAnalyzer',
    'clean_text',
    'extract_keywords'
]
