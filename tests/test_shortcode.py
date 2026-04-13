from app.shortcode import generate_shortcode, CODE_LENGTH, ALPHABETS

def test_shortcode_length() -> None:
    assert len(generate_shortcode()) == CODE_LENGTH

def test_shortcode_characters() -> None:
    code = generate_shortcode()
    assert all(c in ALPHABETS for c in code)

def test_shortcode_uniqueness() -> None:
    codes = {generate_shortcode() for _ in range(1000)}
    assert len(codes) > 990
