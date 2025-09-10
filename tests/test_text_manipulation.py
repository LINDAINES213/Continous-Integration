import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from text_manipulation import reverse, count_vowels, is_palindrome, to_upper, concat

# ---------- reverse ----------
@pytest.mark.parametrize(
    "s, expected",
    [
        ("hola", "aloh"),       
        ("Racecar", "racecaR"), 
    ],
)
def test_reverse_happy_paths(s, expected):
    assert reverse(s) == expected

def test_reverse_empty_string():
    assert reverse("") == ""  

@pytest.mark.parametrize("bad", [None, 123, 3.14, ["a"], {"k":"v"}])
def test_reverse_raises_typeerror_on_non_str(bad):
    with pytest.raises(TypeError):
        reverse(bad)  


# ---------- count_vowels ----------
@pytest.mark.parametrize(
    "s, expected",
    [
        ("hola", 2),           
        ("HELLO", 2),          
    ],
)
def test_count_vowels_happy_paths(s, expected):
    assert count_vowels(s) == expected

def test_count_vowels_empty_string():
    assert count_vowels("") == 0  

def test_count_vowels_with_accent():
    assert count_vowels("canción única") == 6  

@pytest.mark.parametrize("bad", [None, 123, 3.14, ["a"], {"k":"v"}])
def test_count_vowels_raises_typeerror_on_non_str(bad):
    with pytest.raises(TypeError):
        count_vowels(bad)


# ---------- is_palindrome ----------
@pytest.mark.parametrize(
    "s, expected",
    [
        ("reconocer", True),                     
        ("Anita lava la tina", True),          
    ],
)
def test_is_palindrome_happy_paths(s, expected):
    assert is_palindrome(s) is expected

def test_is_palindrome_punctuation_and_spaces():
    assert is_palindrome("¿Acaso hubo búhos acá?")  

def test_is_palindrome_false_case():
    assert is_palindrome("python") is False  

@pytest.mark.parametrize("bad", [None, 123, 3.14, ["a"], {"k":"v"}])
def test_is_palindrome_raises_typeerror_on_non_str(bad):
    with pytest.raises(TypeError):
        is_palindrome(bad)


# ---------- to_upper ----------
@pytest.mark.parametrize(
    "s, expected",
    [
        ("hola", "HOLA"),   
        ("MiXeD", "MIXED"), 
    ],
)
def test_to_upper_happy_paths(s, expected):
    assert to_upper(s) == expected

def test_to_upper_empty_string():
    assert to_upper("") == ""  

@pytest.mark.parametrize("bad", [None, 123, 3.14, ["a"], {"k":"v"}])
def test_to_upper_raises_typeerror_on_non_str(bad):
    with pytest.raises(TypeError):
        to_upper(bad)


# ---------- concat ----------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("hola", "mundo", "holamundo"), 
        ("", "X", "X"),     
    ],           
)
def test_concat_happy_paths(a, b, expected):
    assert concat(a, b) == expected

def test_concat_both_empty():
    assert concat("", "") == ""  

@pytest.mark.parametrize("bad_a", [None, 123, 3.14, ["a"], {"k":"v"}])
def test_concat_raises_typeerror_on_non_str_a(bad_a):
    with pytest.raises(TypeError):
        concat(bad_a, "ok")

@pytest.mark.parametrize("bad_b", [None, 123, 3.14, ["a"], {"k":"v"}])
def test_concat_raises_typeerror_on_non_str_b(bad_b):
    with pytest.raises(TypeError):
        concat("ok", bad_b)
