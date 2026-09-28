def test_identical(self):
    ci1 = CategoricalIndex(['a', 'b'], categories=['a', 'b'], ordered=True)
    ci2 = CategoricalIndex(['a', 'b'], categories=['a', 'b', 'c'], ordered=True)
    assert ci1.identical(ci1)
    assert ci1.identical(ci1.copy())
    assert not ci1.identical(ci2)