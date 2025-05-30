import unittest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import numpy as np
import pandas as pd

from data_science_toolkit.math_tools import (
    StatisticalCalculator, advanced_mean, correlation_matrix, moving_average
)


class TestStatisticalCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = StatisticalCalculator()
        self.sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_descriptive_stats_basic(self):
        stats = self.calc.descriptive_stats(self.sample_data)
        
        self.assertEqual(stats['count'], 10)
        self.assertEqual(stats['mean'], 5.5)
        self.assertEqual(stats['median'], 5.5)
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 10)
        self.assertIn('std', stats)
        self.assertIn('var', stats)
    
    def test_descriptive_stats_empty_data(self):
        with self.assertRaises(ValueError) as context:
            self.calc.descriptive_stats([])
        self.assertIn("Dane wejściowe nie mogą być puste", str(context.exception))
    
    def test_confidence_interval_basic(self):
        ci = self.calc.confidence_interval(self.sample_data)
        self.assertIsInstance(ci, tuple)
        self.assertEqual(len(ci), 2)
        self.assertLess(ci[0], ci[1])
    
    def test_confidence_interval_insufficient_data(self):
        with self.assertRaises(ValueError) as context:
            self.calc.confidence_interval([1])
        self.assertIn("co najmniej 2 punktów danych", str(context.exception))


class TestAdvancedMean(unittest.TestCase):
    
    def setUp(self):
        self.positive_data = [1, 2, 3, 4, 5]
        self.mixed_data = [-2, -1, 0, 1, 2]
    
    def test_arithmetic_mean(self):
        result = advanced_mean(self.positive_data, method='arithmetic')
        self.assertEqual(result, 3.0)
    
    def test_geometric_mean(self):
        result = advanced_mean(self.positive_data, method='geometric')
        self.assertAlmostEqual(result, 2.605, places=3)
    
    def test_geometric_mean_negative_values(self):
        with self.assertRaises(ValueError) as context:
            advanced_mean(self.mixed_data, method='geometric')
        self.assertIn("wartości dodatnich", str(context.exception))
    
    def test_harmonic_mean(self):
        result = advanced_mean(self.positive_data, method='harmonic')
        self.assertAlmostEqual(result, 2.189, places=3)
    
    def test_quadratic_mean(self):
        result = advanced_mean(self.positive_data, method='quadratic')
        self.assertAlmostEqual(result, 3.317, places=3)
    
    def test_invalid_method(self):
        with self.assertRaises(ValueError) as context:
            advanced_mean(self.positive_data, method='nieprawidlowa')
        self.assertIn("Nieobsługiwana metoda średniej", str(context.exception))
    
    def test_empty_data(self):
        with self.assertRaises(ValueError) as context:
            advanced_mean([], method='arithmetic')
        self.assertIn("Dane wejściowe nie mogą być puste", str(context.exception))


class TestCorrelationMatrix(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 4, 6, 8, 10],  
            'C': [1, 1, 1, 1, 1],   
            'D': ['tekst', 'dane', 'tutaj', 'nie', 'numeryczne']
        })
    
    def test_pearson_correlation(self):
        result = correlation_matrix(self.df, method='pearson')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 3))  
        self.assertAlmostEqual(result.loc['A', 'B'], 1.0, places=5)
    
    def test_invalid_method(self):
        with self.assertRaises(ValueError) as context:
            correlation_matrix(self.df, method='nieprawidlowa')
        self.assertIn("Nieobsługiwana metoda korelacji", str(context.exception))
    
    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError) as context:
            correlation_matrix([1, 2, 3])
        self.assertIn("pandas DataFrame", str(context.exception))


class TestMovingAverage(unittest.TestCase):
    
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_simple_moving_average(self):
        result = moving_average(self.data, window=3, method='simple')
        self.assertEqual(len(result), 8)  # 10 - 3 + 1
        self.assertAlmostEqual(result[0], 2.0, places=5)
    
    def test_exponential_moving_average(self):
        result = moving_average(self.data, window=3, method='exponential')
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0], 1.0)
    
    def test_invalid_window_size(self):
        with self.assertRaises(ValueError) as context:
            moving_average(self.data, window=0)
        self.assertIn("Nieprawidłowy rozmiar okna", str(context.exception))
    
    def test_invalid_method(self):
        with self.assertRaises(ValueError) as context:
            moving_average(self.data, window=3, method='nieprawidlowa')
        self.assertIn("Nieobsługiwana metoda średniej ruchomej", str(context.exception))


if __name__ == '__main__':
    unittest.main(verbosity=2)
