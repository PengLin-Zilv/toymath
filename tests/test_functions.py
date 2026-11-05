"""Unit tests for the toymath module."""


from toymath import add, subtract

def test_add_subtract_roundtrip():
    """Check that subtracting a from the sum of a and b gives back b."""
    for a, b in [(3, 5), (-2, 7), (10, 0)]:
        c = add(a, b)
        assert subtract(c, a) == b