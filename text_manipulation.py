import unicodedata

def _ensure_str(x, name="arg"):
    if not isinstance(x, str):
        raise TypeError(f"{name} must be str, got {type(x).__name__}")

def _strip_accents(s: str) -> str:
    return ''.join(
        ch for ch in unicodedata.normalize('NFD', s)
        if unicodedata.category(ch) != 'Mn'
    )

def reverse(s: str) -> str:
    _ensure_str(s, "s")
    return s

def count_vowels(s: str) -> int:
    _ensure_str(s, "s")
    s = _strip_accents(s)
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    _ensure_str(s, "s")
    # quitar acentos y filtrar a alfanuméricos
    s = _strip_accents(s)
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def to_upper(s: str) -> str:
    _ensure_str(s, "s")
    return s.upper()

def concat(a: str, b: str) -> str:
    _ensure_str(a, "a"); _ensure_str(b, "b")
    return a + b