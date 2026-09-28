def test_where_datetime(self):
    df = DataFrame(dict(A=date_range('20130102', periods=5), B=date_range('20130104', periods=5), C=np.random.randn(5)))
    stamp = datetime(2013, 1, 3)
    with pytest.raises(TypeError):
        df > stamp
    result = df[df.iloc[:, :-1] > stamp]
    expected = df.copy()
    expected.loc[[0, 1], 'A'] = np.nan
    expected.loc[:, 'C'] = np.nan
    tm.assert_frame_equal(result, expected)