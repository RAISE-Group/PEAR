@pytest.mark.parametrize('cls', [CategoricalDtype, DatetimeTZDtype, IntervalDtype])
def test_astype_categoricaldtype_class_raises(self, cls):
    df = DataFrame({'A': ['a', 'a', 'b', 'c']})
    xpr = 'Expected an instance of {}'.format(cls.__name__)
    with pytest.raises(TypeError, match=xpr):
        df.astype({'A': cls})
    with pytest.raises(TypeError, match=xpr):
        df['A'].astype(cls)