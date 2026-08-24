from src.text_utils import reverse_text, capitalize_words


def test_reverse_text():
    assert reverse_text("github") == "buhtig"
    assert reverse_text("12345") == "54321"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""