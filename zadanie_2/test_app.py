import unittest
from datetime import datetime
import math
from app import (
    validate_email,
    calculate_circle_area,
    filter_positive_numbers,
    convert_date_format,
    is_palindrome
)


class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk", 
            "admin123@test-site.org"
        ]
        self.invalid_emails = [
            "invalid-email",
            "@domain.com",
            "user@",
            ""
        ]
        self.test_numbers = [1, -2, 3, -4, 5, 0, -6]
        
    def test_validate_email_valid_cases(self):
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))
    
    def test_validate_email_invalid_cases(self):
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))
    
    def test_validate_email_type_error(self):
        with self.assertRaises(TypeError):
            validate_email(123)
        with self.assertRaises(TypeError):
            validate_email(None)
        with self.assertRaises(TypeError):
            validate_email([])
    
    def test_calculate_circle_area_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi, places=5)
        self.assertAlmostEqual(calculate_circle_area(2), 4 * math.pi, places=5)
    
    def test_calculate_circle_area_zero_radius(self):
        self.assertEqual(calculate_circle_area(0), 0)
    
    def test_calculate_circle_area_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)
        with self.assertRaises(ValueError):
            calculate_circle_area(-0.5)
    
    def test_calculate_circle_area_type_error(self):
        with self.assertRaises(TypeError):
            calculate_circle_area("string")
        with self.assertRaises(TypeError):
            calculate_circle_area(None)
        with self.assertRaises(TypeError):
            calculate_circle_area([])
    
    def test_filter_positive_numbers_mixed_list(self):
        result = filter_positive_numbers(self.test_numbers)
        self.assertEqual(result, [1, 3, 5])
    
    def test_filter_positive_numbers_empty_list(self):
        self.assertEqual(filter_positive_numbers([]), [])
    
    def test_filter_positive_numbers_all_negative(self):
        self.assertEqual(filter_positive_numbers([-1, -2, -3]), [])
    
    def test_filter_positive_numbers_all_positive(self):
        self.assertEqual(filter_positive_numbers([1, 2, 3]), [1, 2, 3])
    
    def test_filter_positive_numbers_type_error(self):
        with self.assertRaises(TypeError):
            filter_positive_numbers("nie lista")
        with self.assertRaises(TypeError):
            filter_positive_numbers(123)
        with self.assertRaises(TypeError):
            filter_positive_numbers(None)
    
    def test_convert_date_format_valid_dates(self):
        self.assertEqual(convert_date_format("2023-12-25"), "25/12/2023")
        self.assertEqual(convert_date_format("2024-01-01"), "01/01/2024")
        self.assertEqual(convert_date_format("2022-06-15"), "15/06/2022")
    
    def test_convert_date_format_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("25-12-2023")
        with self.assertRaises(ValueError):
            convert_date_format("2023/12/25")
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date")
    
    def test_convert_date_format_invalid_date(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01")
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-30")
    
    def test_convert_date_format_type_error(self):
        with self.assertRaises(TypeError):
            convert_date_format(123)
        with self.assertRaises(TypeError):
            convert_date_format(None)
        with self.assertRaises(TypeError):
            convert_date_format([])
    
    def test_is_palindrome_valid_palindromes(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome(""))
    
    def test_is_palindrome_case_insensitive(self):
        self.assertTrue(is_palindrome("Radar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    
    def test_is_palindrome_not_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("test"))
    
    def test_is_palindrome_type_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)
        with self.assertRaises(TypeError):
            is_palindrome([])
    
    def test_parametrized_email_validation(self):
        test_cases = [
            ("valid@email.com", True),
            ("invalid.email", False),
            ("test@domain.org", True),
            ("@invalid.com", False),
            ("user@domain.co.uk", True),
            ("", False)
        ]
        
        for email, expected in test_cases:
            with self.subTest(email=email, expected=expected):
                self.assertEqual(validate_email(email), expected)
    
    def test_parametrized_circle_area(self):
        test_cases = [
            (0, 0),
            (1, math.pi),
            (2, 4 * math.pi),
            (0.5, 0.25 * math.pi)
        ]
        
        for radius, expected in test_cases:
            with self.subTest(radius=radius, expected=expected):
                self.assertAlmostEqual(calculate_circle_area(radius), expected, places=5)
    
    def test_parametrized_palindrome(self):
        test_cases = [
            ("radar", True),
            ("hello", False),
            ("A man a plan a canal Panama", True),
            ("race a car", False),
            ("", True),
            ("a", True)
        ]
        
        for text, expected in test_cases:
            with self.subTest(text=text, expected=expected):
                self.assertEqual(is_palindrome(text), expected)


if __name__ == '__main__':
    unittest.main()
