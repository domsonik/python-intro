import unittest
import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import pandas as pd
import numpy as np
import tempfile

from data_science_toolkit.data_utils import DataProcessor, load_csv_safe, normalize_data


class TestDataProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = DataProcessor()
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 3, 2, 1],
            'B': [4, 5, 6, 5, 4],
            'C': ['x', 'y', 'z', 'y', 'x']
        })
    
    def test_load_and_validate_dataframe(self):
        result = self.processor.load_and_validate(self.sample_data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (5, 3))
        self.assertEqual(self.processor.original_shape, (5, 3))
    
    def test_load_and_validate_dict(self):
        data_dict = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
        result = self.processor.load_and_validate(data_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 2))
    
    def test_load_and_validate_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            self.processor.load_and_validate([1, 2, 3])
        self.assertIn("Nieobsługiwany format danych", str(context.exception))
    
    def test_remove_duplicates(self):
        result = self.processor.remove_duplicates(self.sample_data)
        self.assertEqual(len(result), 3)
        
    def test_remove_duplicates_no_duplicates(self):
        unique_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = self.processor.remove_duplicates(unique_data)
        self.assertEqual(len(result), 3)


class TestLoadCsvSafe(unittest.TestCase):
    
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
        self.temp_file.write('A,B,C\n1,2,3\n4,5,6\n7,8,9\n')
        self.temp_file.close()
    
    def tearDown(self):
        os.unlink(self.temp_file.name)
    
    def test_load_csv_success(self):
        df = load_csv_safe(self.temp_file.name)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 3))
        self.assertEqual(list(df.columns), ['A', 'B', 'C'])
    
    def test_load_csv_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            load_csv_safe('nieistniejacy_plik.csv')


class TestNormalizeData(unittest.TestCase):
    
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.data_series = pd.Series([10, 20, 30, 40, 50])
    
    def test_minmax_normalization(self):
        result = normalize_data(self.data, method='minmax')
        expected = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_zscore_normalization(self):
        result = normalize_data(self.data, method='zscore')
        self.assertAlmostEqual(np.mean(result), 0.0, places=10)
        self.assertAlmostEqual(np.std(result), 1.0, places=10)
    
    def test_robust_normalization(self):
        result = normalize_data(self.data, method='robust')
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(len(result), len(self.data))
    
    def test_invalid_method(self):
        with self.assertRaises(ValueError) as context:
            normalize_data(self.data, method='nieprawidlowa')
        self.assertIn("Nieobsługiwana metoda normalizacji", str(context.exception))
    
    def test_constant_data(self):
        constant_data = [5, 5, 5, 5, 5]
        result = normalize_data(constant_data, method='minmax')
        expected = np.zeros(5)
        np.testing.assert_array_equal(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
