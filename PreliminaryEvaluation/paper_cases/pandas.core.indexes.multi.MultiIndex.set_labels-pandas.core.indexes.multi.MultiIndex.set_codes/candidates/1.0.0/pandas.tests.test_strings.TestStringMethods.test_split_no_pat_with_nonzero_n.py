def test_split_no_pat_with_nonzero_n(self):
    s = Series(['split once', 'split once too!'])
    result = s.str.split(n=1)
    expected = Series({0: ['split', 'once'], 1: ['split', 'once too!']})
    tm.assert_series_equal(expected, result, check_index_type=False)