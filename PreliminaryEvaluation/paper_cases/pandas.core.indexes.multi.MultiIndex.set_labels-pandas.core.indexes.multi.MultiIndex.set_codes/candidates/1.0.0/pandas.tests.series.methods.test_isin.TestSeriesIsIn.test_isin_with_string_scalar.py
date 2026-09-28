def test_isin_with_string_scalar(self):
    s = Series(['A', 'B', 'C', 'a', 'B', 'B', 'A', 'C'])
    msg = 'only list-like objects are allowed to be passed to isin\\(\\), you passed a \\[str\\]'
    with pytest.raises(TypeError, match=msg):
        s.isin('a')
    s = Series(['aaa', 'b', 'c'])
    with pytest.raises(TypeError, match=msg):
        s.isin('aaa')