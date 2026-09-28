def test_operators_timedelta64_with_timedelta(self, scalar_td):
    td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
    td1.iloc[2] = np.nan
    td1 + scalar_td
    scalar_td + td1
    td1 - scalar_td
    scalar_td - td1
    td1 / scalar_td
    scalar_td / td1