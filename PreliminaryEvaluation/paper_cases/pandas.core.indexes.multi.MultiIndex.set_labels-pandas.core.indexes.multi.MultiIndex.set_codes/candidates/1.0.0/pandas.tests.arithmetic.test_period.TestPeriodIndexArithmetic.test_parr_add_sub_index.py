def test_parr_add_sub_index(self):
    pi = pd.period_range('2000-12-31', periods=3)
    parr = pi.array
    result = parr - pi
    expected = pi - pi
    tm.assert_index_equal(result, expected)