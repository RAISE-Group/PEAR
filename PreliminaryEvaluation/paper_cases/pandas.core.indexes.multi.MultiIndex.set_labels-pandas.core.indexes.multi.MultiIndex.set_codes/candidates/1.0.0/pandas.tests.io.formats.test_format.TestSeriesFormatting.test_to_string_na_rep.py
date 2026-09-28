def test_to_string_na_rep(self):
    s = pd.Series(index=range(100), dtype=np.float64)
    res = s.to_string(na_rep='foo', max_rows=2)
    exp = '0    foo\n      ..\n99   foo'
    assert res == exp