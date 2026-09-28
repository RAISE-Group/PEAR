def test_assignment_in_query(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df_orig = df.copy()
    with pytest.raises(ValueError):
        df.query('a = 1')
    tm.assert_frame_equal(df, df_orig)