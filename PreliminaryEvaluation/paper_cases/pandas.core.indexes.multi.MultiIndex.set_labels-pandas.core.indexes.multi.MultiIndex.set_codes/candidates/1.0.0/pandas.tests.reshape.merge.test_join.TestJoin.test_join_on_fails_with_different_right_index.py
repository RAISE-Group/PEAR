def test_join_on_fails_with_different_right_index(self):
    df = DataFrame({'a': np.random.choice(['m', 'f'], size=3), 'b': np.random.randn(3)})
    df2 = DataFrame({'a': np.random.choice(['m', 'f'], size=10), 'b': np.random.randn(10)}, index=tm.makeCustomIndex(10, 2))
    msg = 'len\\(left_on\\) must equal the number of levels in the index of "right"'
    with pytest.raises(ValueError, match=msg):
        merge(df, df2, left_on='a', right_index=True)