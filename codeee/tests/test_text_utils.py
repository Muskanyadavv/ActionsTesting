from src.text_utils import reverse_text, capitalize_words


def test_reverse_text():
    assert reverse_text("github") == "github"
    assert reverse_text("12345") == "12345"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""