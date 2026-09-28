@pytest.mark.parametrize('ordered1', [True, False, None])
@pytest.mark.parametrize('ordered2', [True, False, None])
def test_categorical_equality(self, ordered1, ordered2):
    c1 = CategoricalDtype(list('abc'), ordered1)
    c2 = CategoricalDtype(list('abc'), ordered2)
    result = c1 == c2
    expected = bool(ordered1) is bool(ordered2)
    assert result is expected
    c1 = CategoricalDtype(list('abc'), ordered1)
    c2 = CategoricalDtype(list('cab'), ordered2)
    result = c1 == c2
    expected = bool(ordered1) is False and bool(ordered2) is False
    assert result is expected
    c2 = CategoricalDtype([1, 2, 3], ordered2)
    assert c1 != c2
    c1 = CategoricalDtype(list('abc'), ordered1)
    c2 = CategoricalDtype(None, ordered2)
    c3 = CategoricalDtype(None, ordered1)
    assert c1 == c2
    assert c2 == c1
    assert c2 == c3