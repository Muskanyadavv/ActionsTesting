def reverse_text(text: str) -> str:
    """Reverses the given string."""
    return text[::-1]


def capitalize_words(text: str) -> str:
    """Capitalizes the first letter of each word."""
    if not text:
        return ""
    return text.title()