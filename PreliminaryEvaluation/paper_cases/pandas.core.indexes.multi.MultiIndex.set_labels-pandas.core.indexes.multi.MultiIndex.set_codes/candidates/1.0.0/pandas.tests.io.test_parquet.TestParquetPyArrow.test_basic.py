def test_basic(self, pa, df_full):
    df = df_full
    df['datetime_tz'] = pd.date_range('20130101', periods=3, tz='Europe/Brussels')
    df['bool_with_none'] = [True, None, True]
    check_round_trip(df, pa)