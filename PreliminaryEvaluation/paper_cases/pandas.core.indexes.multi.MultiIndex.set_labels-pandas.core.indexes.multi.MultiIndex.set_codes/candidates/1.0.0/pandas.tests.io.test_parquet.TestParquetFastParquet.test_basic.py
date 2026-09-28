@td.skip_if_no('fastparquet', min_version='0.3.2')
def test_basic(self, fp, df_full):
    df = df_full
    df['datetime_tz'] = pd.date_range('20130101', periods=3, tz='US/Eastern')
    df['timedelta'] = pd.timedelta_range('1 day', periods=3)
    check_round_trip(df, fp)