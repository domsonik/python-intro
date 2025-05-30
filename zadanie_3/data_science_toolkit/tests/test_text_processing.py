import unittest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from data_science_toolkit.text_processing import (
    TextAnalyzer, clean_text, extract_keywords, text_similarity
)


class TestTextAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = TextAnalyzer()
        self.sample_text = "To jest przykładowy tekst do testowania. Zawiera wiele zdań!"
        self.polish_text = "Python to język programowania używany w analizie danych."
    
    def test_initialization(self):
        self.assertEqual(self.analyzer.language, 'polish')
        self.assertIsInstance(self.analyzer.stop_words, set)
        self.assertIn('i', self.analyzer.stop_words)
        self.assertIn('to', self.analyzer.stop_words)
    
    def test_preprocess_text_basic(self):
        result = self.analyzer.preprocess_text(self.sample_text)
        self.assertIsInstance(result, str)
        self.assertEqual(result.lower(), result)
    
    def test_preprocess_text_remove_punctuation(self):
        result = self.analyzer.preprocess_text(self.sample_text, remove_punctuation=True)
        self.assertNotIn('!', result)
        self.assertNotIn('.', result)
    
    def test_preprocess_text_remove_numbers(self):
        text_with_numbers = "Ten tekst ma 123 liczby i 456 więcej."
        result = self.analyzer.preprocess_text(text_with_numbers, remove_numbers=True)
        self.assertNotIn('123', result)
        self.assertNotIn('456', result)
    
    def test_preprocess_text_non_string_input(self):
        result = self.analyzer.preprocess_text(123)
        self.assertIsInstance(result, str)
        self.assertEqual(result, '123')
    
    def test_extract_features_basic(self):
        features = self.analyzer.extract_features(self.sample_text)
        self.assertIsInstance(features, dict)
        
        expected_keys = [
            'char_count', 'word_count', 'sentence_count',
            'avg_word_length', 'unique_words', 'lexical_diversity',
            'punctuation_count'
        ]
        for key in expected_keys:
            self.assertIn(key, features)
    
    def test_extract_features_empty_text(self):
        features = self.analyzer.extract_features("")
        self.assertEqual(features['char_count'], 0)
        self.assertEqual(features['word_count'], 0)
        self.assertEqual(features['avg_word_length'], 0)
        self.assertEqual(features['lexical_diversity'], 0)


class TestCleanText(unittest.TestCase):
    
    def test_clean_text_urls(self):
        text = "Sprawdź tę stronę: https://example.com i tę www.test.pl"
        result = clean_text(text)
        self.assertNotIn('https://example.com', result)
        self.assertNotIn('www.test.pl', result)
    
    def test_clean_text_mentions_hashtags(self):
        text = "Obserwuj @użytkownik i sprawdź #hashtag"
        result = clean_text(text)
        self.assertNotIn('@użytkownik', result)
        self.assertNotIn('#hashtag', result)
    
    def test_clean_text_aggressive(self):
        text = "Tekst z liczbami 123 i znakami éñüñ"
        result = clean_text(text, aggressive=True)
        self.assertNotIn('123', result)
        self.assertNotIn('é', result)
    
    def test_clean_text_non_string_input(self):
        result = clean_text(123)
        self.assertIsInstance(result, str)
    
    def test_clean_text_empty_string(self):
        result = clean_text("")
        self.assertEqual(result, "")


class TestExtractKeywords(unittest.TestCase):
    
    def test_extract_keywords_basic(self):
        text = "python programowanie język python kod programowanie"
        keywords = extract_keywords(text, top_n=3)
        
        self.assertIsInstance(keywords, list)
        self.assertLessEqual(len(keywords), 3)
        
        if keywords:
            self.assertIsInstance(keywords[0], tuple)
            self.assertEqual(len(keywords[0]), 2)
    
    def test_extract_keywords_frequency(self):
        text = "python python python kod kod test"
        keywords = extract_keywords(text, top_n=5)
        
        python_freq = next((freq for word, freq in keywords if word == 'python'), 0)
        self.assertEqual(python_freq, 3)
    
    def test_extract_keywords_min_length(self):
        text = "a bb ccc dddd eeeee ffffff"
        keywords = extract_keywords(text, min_length=4)
        
        for word, count in keywords:
            self.assertGreaterEqual(len(word), 4)
    
    def test_extract_keywords_empty_text(self):
        keywords = extract_keywords("")
        self.assertEqual(len(keywords), 0)


class TestTextSimilarity(unittest.TestCase):
    
    def test_jaccard_similarity_identical(self):
        text1 = "hello world python"
        text2 = "hello world python"
        similarity = text_similarity(text1, text2, method='jaccard')
        self.assertEqual(similarity, 1.0)
    
    def test_jaccard_similarity_different(self):
        text1 = "hello world"
        text2 = "goodbye universe"
        similarity = text_similarity(text1, text2, method='jaccard')
        self.assertEqual(similarity, 0.0)
    
    def test_cosine_similarity_partial(self):
        text1 = "hello world python"
        text2 = "hello python programming"
        similarity = text_similarity(text1, text2, method='cosine')
        
        self.assertGreater(similarity, 0.0)
        self.assertLessEqual(similarity, 1.0)
    
    def test_similarity_empty_texts(self):
        similarity_jaccard = text_similarity("", "", method='jaccard')
        similarity_cosine = text_similarity("", "", method='cosine')
        
        self.assertEqual(similarity_jaccard, 0.0)
        self.assertEqual(similarity_cosine, 0.0)
    
    def test_invalid_similarity_method(self):
        with self.assertRaises(ValueError) as context:
            text_similarity("text1", "text2", method='nieprawidlowa')
        self.assertIn("Nieobsługiwana metoda podobieństwa", str(context.exception))
    
    def test_similarity_case_insensitive(self):
        text1 = "Hello World"
        text2 = "hello world"
        
        similarity = text_similarity(text1, text2, method='jaccard')
        self.assertEqual(similarity, 1.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
