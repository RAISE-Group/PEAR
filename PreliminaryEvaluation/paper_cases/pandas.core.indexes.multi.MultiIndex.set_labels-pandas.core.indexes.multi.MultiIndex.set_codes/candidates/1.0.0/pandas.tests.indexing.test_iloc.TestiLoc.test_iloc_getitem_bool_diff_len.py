@pytest.mark.parametrize('index', [[True, False], [True, False, True, False]])
def test_iloc_getitem_bool_diff_len(self, index):
    s = Series([1, 2, 3])
    msg = 'Boolean index has wrong length: {} instead of {}'.format(len(index), len(s))
    with pytest.raises(IndexError, match=msg):
        _ = s.iloc[index]