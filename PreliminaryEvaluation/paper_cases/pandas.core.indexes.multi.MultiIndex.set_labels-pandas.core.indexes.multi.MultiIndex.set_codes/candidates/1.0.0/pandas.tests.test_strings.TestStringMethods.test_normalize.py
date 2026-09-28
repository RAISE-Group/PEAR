def test_normalize(self):
    values = ['ABC', 'ＡＢＣ', '１２３', np.nan, 'ｱｲｴ']
    s = Series(values, index=['a', 'b', 'c', 'd', 'e'])
    normed = ['ABC', 'ABC', '123', np.nan, 'アイエ']
    expected = Series(normed, index=['a', 'b', 'c', 'd', 'e'])
    result = s.str.normalize('NFKC')
    tm.assert_series_equal(result, expected)
    expected = Series(['ABC', 'ＡＢＣ', '１２３', np.nan, 'ｱｲｴ'], index=['a', 'b', 'c', 'd', 'e'])
    result = s.str.normalize('NFC')
    tm.assert_series_equal(result, expected)
    with pytest.raises(ValueError, match='invalid normalization form'):
        s.str.normalize('xxx')
    s = Index(['ＡＢＣ', '１２３', 'ｱｲｴ'])
    expected = Index(['ABC', '123', 'アイエ'])
    result = s.str.normalize('NFKC')
    tm.assert_index_equal(result, expected)