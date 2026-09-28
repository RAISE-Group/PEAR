def test_repr_with_mi_nat(self, float_string_frame):
    df = DataFrame({'X': [1, 2]}, index=[[pd.NaT, pd.Timestamp('20130101')], ['a', 'b']])
    result = repr(df)
    expected = '              X\nNaT        a  1\n2013-01-01 b  2'
    assert result == expected