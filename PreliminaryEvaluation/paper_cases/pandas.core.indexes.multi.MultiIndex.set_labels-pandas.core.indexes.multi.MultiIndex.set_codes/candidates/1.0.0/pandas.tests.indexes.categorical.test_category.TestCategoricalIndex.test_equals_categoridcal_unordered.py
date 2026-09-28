def test_equals_categoridcal_unordered(self):
    a = pd.CategoricalIndex(['A'], categories=['A', 'B'])
    b = pd.CategoricalIndex(['A'], categories=['B', 'A'])
    c = pd.CategoricalIndex(['C'], categories=['B', 'A'])
    assert a.equals(b)
    assert not a.equals(c)
    assert not b.equals(c)