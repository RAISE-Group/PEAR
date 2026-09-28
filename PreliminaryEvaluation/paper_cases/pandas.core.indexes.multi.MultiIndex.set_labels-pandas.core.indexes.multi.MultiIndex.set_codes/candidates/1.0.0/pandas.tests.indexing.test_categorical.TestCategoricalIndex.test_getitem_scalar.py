def test_getitem_scalar(self):
    cats = Categorical([Timestamp('12-31-1999'), Timestamp('12-31-2000')])
    s = Series([1, 2], index=cats)
    expected = s.iloc[0]
    result = s[cats[0]]
    assert result == expected