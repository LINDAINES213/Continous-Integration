def reverse(s: str) -> str:
    """Retorna una cadena de texto en orden inverso"""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Cuenta el número de vocales en una cadena"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    """Verifica si una cadena es palíndroma"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # ignorar espacios y símbolos
    return cleaned == cleaned[::-1]

def to_upper(s: str) -> str:
    """Convierte un string a mayúsculas"""
    return s.upper()

def concat(a: str, b: str) -> str:
    """Concatena dos cadenas"""
    return a + b

