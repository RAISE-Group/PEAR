@pytest.mark.parametrize('other', ['a', 1])
def test_non_bool_or_na_other_raises(self, other, all_logical_operators):
    a = pd.array([True, False], dtype='boolean')
    with pytest.raises(TypeError, match=str(type(other).__name__)):
        getattr(a, all_logical_operators)(other)