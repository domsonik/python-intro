import re
import math
from datetime import datetime
from typing import List, Union


def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        raise TypeError("Email musi być stringiem")
    
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def calculate_circle_area(radius: Union[int, float]) -> float:
    if not isinstance(radius, (int, float)):
        raise TypeError("Promień musi być liczbą")
    
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    
    return math.pi * radius * radius


def filter_positive_numbers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    if not isinstance(numbers, list):
        raise TypeError("Argument musi być listą")
    
    return [num for num in numbers if isinstance(num, (int, float)) and num > 0]


def convert_date_format(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise TypeError("Data musi być stringiem")
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError as e:
        raise ValueError(f"Niepoprawny format daty: {e}")


def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("Tekst musi być stringiem")
    
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    
    return cleaned_text == cleaned_text[::-1]
