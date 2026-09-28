@pytest.mark.parametrize('level', [2, 10, -3])
def test_isin_level_kwarg_bad_level_raises(self, level, indices):
    index = indices
    with pytest.raises(IndexError, match='Too many levels'):
        index.isin([], level=level)