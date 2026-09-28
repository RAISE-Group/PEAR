def test_to_string_float_na_spacing(self):
    s = Series([0.0, 1.5678, 2.0, -3.0, 4.0])
    s[::2] = np.nan
    result = s.to_string()
    expected = '0       NaN\n' + '1    1.5678\n' + '2       NaN\n' + '3   -3.0000\n' + '4       NaN'
    assert result == expected