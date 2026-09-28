def test_comparison_invalid(self):

    def check(df, df2):
        for x, y in [(df, df2), (df2, df)]:
            result = x == y
            expected = pd.DataFrame({col: x[col] == y[col] for col in x.columns}, index=x.index, columns=x.columns)
            tm.assert_frame_equal(result, expected)
            result = x != y
            expected = pd.DataFrame({col: x[col] != y[col] for col in x.columns}, index=x.index, columns=x.columns)
            tm.assert_frame_equal(result, expected)
            with pytest.raises(TypeError):
                x >= y
            with pytest.raises(TypeError):
                x > y
            with pytest.raises(TypeError):
                x < y
            with pytest.raises(TypeError):
                x <= y
    df = pd.DataFrame(np.random.randint(10, size=(10, 1)), columns=['a'])
    df['dates'] = pd.date_range('20010101', periods=len(df))
    df2 = df.copy()
    df2['dates'] = df['a']
    check(df, df2)
    df = pd.DataFrame(np.random.randint(10, size=(10, 2)), columns=['a', 'b'])
    df2 = pd.DataFrame({'a': pd.date_range('20010101', periods=len(df)), 'b': pd.date_range('20100101', periods=len(df))})
    check(df, df2)