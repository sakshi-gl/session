# tests/test_core.py

from src.my_project.core import greet # type: ignore

def test_greet_with_name():
    """Tests the greet function with a valid name."""
    assert greet("Alice") == "Hello, Alice!"

def test_greet_with_empty_string():
    """Tests the greet function with an empty name."""
    assert greet("") == "Hello, stranger!"