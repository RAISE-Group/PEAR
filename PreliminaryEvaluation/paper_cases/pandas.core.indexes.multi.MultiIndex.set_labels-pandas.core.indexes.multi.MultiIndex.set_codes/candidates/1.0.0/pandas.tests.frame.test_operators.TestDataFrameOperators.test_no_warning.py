def test_no_warning(self, all_arithmetic_operators):
    df = pd.DataFrame({'A': [0.0, 0.0], 'B': [0.0, None]})
    b = df['B']
    with tm.assert_produces_warning(None):
        getattr(df, all_arithmetic_operators)(b, 0)