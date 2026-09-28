def test_basic_subset_columns(self, pa, df_full):
    df = df_full
    df['datetime_tz'] = pd.date_range('20130101', periods=3, tz='Europe/Brussels')
    check_round_trip(df, pa, expected=df[['string', 'int']], read_kwargs={'columns': ['string', 'int']})