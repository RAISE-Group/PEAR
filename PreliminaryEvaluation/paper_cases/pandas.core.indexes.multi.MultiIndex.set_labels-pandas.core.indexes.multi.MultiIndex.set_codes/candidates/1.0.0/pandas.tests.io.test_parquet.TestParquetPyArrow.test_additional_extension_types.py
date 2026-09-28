@td.skip_if_no('pyarrow', min_version='0.15.1.dev')
def test_additional_extension_types(self, pa):
    df = pd.DataFrame({'d': pd.period_range('2012-01-01', periods=3, freq='D')})
    check_round_trip(df, pa)