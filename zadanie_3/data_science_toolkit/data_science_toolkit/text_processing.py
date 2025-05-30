import re
import string
from typing import List, Dict, Set, Union, Optional, Tuple
from collections import Counter
import unicodedata


class TextAnalyzer:
    
    def __init__(self, language: str = 'polish'):
        self.language = language
        self.stop_words = self._get_basic_stop_words()
        self.processed_texts = []
    
    def _get_basic_stop_words(self) -> Set[str]:
        polish_stops = {
            'a', 'aby', 'ale', 'albo', 'bardzo', 'bez', 'być', 'ci', 'co', 'czy',
            'dla', 'do', 'gdy', 'go', 'i', 'ich', 'ja', 'jak', 'jako', 'je',
            'jego', 'jej', 'już', 'ma', 'może', 'na', 'nad', 'nie', 'o', 'od',
            'po', 'pod', 'oraz', 'się', 'są', 'ta', 'tak', 'te', 'to', 'tu',
            'w', 'we', 'z', 'za', 'że', 'przez', 'przy', 'także', 'tylko'
        }
        return polish_stops
    
    def preprocess_text(self, text: str, remove_punctuation: bool = True, 
                       remove_numbers: bool = False, to_lowercase: bool = True) -> str:
        if not isinstance(text, str):
            text = str(text)
        
        text = unicodedata.normalize('NFKD', text)
        
        if to_lowercase:
            text = text.lower()
        
        text = re.sub(r'\s+', ' ', text).strip()
        
        if remove_punctuation:
            text = text.translate(str.maketrans('', '', string.punctuation))
        
        if remove_numbers:
            text = re.sub(r'\d+', '', text)
        
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def extract_features(self, text: str) -> Dict[str, Union[int, float]]:
        words = text.split()
        sentences = text.split('.')
        
        features = {
            'char_count': len(text),
            'word_count': len(words),
            'sentence_count': len([s for s in sentences if s.strip()]),
            'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0,
            'unique_words': len(set(words)),
            'lexical_diversity': len(set(words)) / len(words) if words else 0,
            'punctuation_count': sum(1 for char in text if char in string.punctuation)
        }
        
        return features


def clean_text(text: str, aggressive: bool = False) -> str:
    if not isinstance(text, str):
        text = str(text)
    
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Usuwanie URL
    text = re.sub(r'@\w+|#\w+', '', text)  # Usuwanie wzmianek i hashtagów
    text = re.sub(r'[^\w\s]', ' ', text)  # Usuwanie znaków specjalnych
    
    if aggressive:
        text = re.sub(r'\d+', '', text)  # Usuwanie liczb
        text = re.sub(r'[^\x00-\x7F]+', '', text)  # Usuwanie znaków non-ASCII
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def extract_keywords(text: str, top_n: int = 10, min_length: int = 3) -> List[Tuple[str, int]]:
    stop_words = {
        'a', 'aby', 'ale', 'albo', 'bardzo', 'bez', 'być', 'ci', 'co', 'czy',
        'dla', 'do', 'gdy', 'go', 'i', 'ich', 'ja', 'jak', 'jako', 'je',
        'jego', 'jej', 'już', 'ma', 'może', 'na', 'nad', 'nie', 'o', 'od',
        'po', 'pod', 'oraz', 'się', 'są', 'ta', 'tak', 'te', 'to', 'tu',
        'w', 'we', 'z', 'za', 'że', 'przez', 'przy', 'także', 'tylko'
    }
    
    cleaned_text = clean_text(text.lower())
    words = cleaned_text.split()
    
    filtered_words = [
        word for word in words 
        if len(word) >= min_length and word not in stop_words
    ]
    
    word_freq = Counter(filtered_words)
    
    return word_freq.most_common(top_n)


def text_similarity(text1: str, text2: str, method: str = 'jaccard') -> float:
    words1 = set(clean_text(text1.lower()).split())
    words2 = set(clean_text(text2.lower()).split())
    
    if method == 'jaccard':
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        return intersection / union if union > 0 else 0.0
    
    elif method == 'cosine':
        all_words = words1.union(words2)
        vec1 = [1 if word in words1 else 0 for word in all_words]
        vec2 = [1 if word in words2 else 0 for word in all_words]
        
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = sum(a * a for a in vec1) ** 0.5
        magnitude2 = sum(b * b for b in vec2) ** 0.5
        
        if magnitude1 * magnitude2 == 0:
            return 0.0
        
        return dot_product / (magnitude1 * magnitude2)
    
    else:
        raise ValueError(f"Nieobsługiwana metoda podobieństwa: {method}")
