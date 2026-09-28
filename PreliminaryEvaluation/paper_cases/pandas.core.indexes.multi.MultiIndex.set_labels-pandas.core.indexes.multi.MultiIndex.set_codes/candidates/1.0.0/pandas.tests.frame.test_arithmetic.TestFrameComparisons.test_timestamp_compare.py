def test_timestamp_compare(self):
    df = pd.DataFrame({'dates1': pd.date_range('20010101', periods=10), 'dates2': pd.date_range('20010102', periods=10), 'intcol': np.random.randint(1000000000, size=10), 'floatcol': np.random.randn(10), 'stringcol': list(tm.rands(10))})
    df.loc[np.random.rand(len(df)) > 0.5, 'dates2'] = pd.NaT
    ops = {'gt': 'lt', 'lt': 'gt', 'ge': 'le', 'le': 'ge', 'eq': 'eq', 'ne': 'ne'}
    for left, right in ops.items():
        left_f = getattr(operator, left)
        right_f = getattr(operator, right)
        if left in ['eq', 'ne']:
            expected = left_f(df, pd.Timestamp('20010109'))
            result = right_f(pd.Timestamp('20010109'), df)
            tm.assert_frame_equal(result, expected)
        else:
            with pytest.raises(TypeError):
                left_f(df, pd.Timestamp('20010109'))
            with pytest.raises(TypeError):
                right_f(pd.Timestamp('20010109'), df)
        expected = left_f(df, pd.Timestamp('nat'))
        result = right_f(pd.Timestamp('nat'), df)
        tm.assert_frame_equal(result, expected)