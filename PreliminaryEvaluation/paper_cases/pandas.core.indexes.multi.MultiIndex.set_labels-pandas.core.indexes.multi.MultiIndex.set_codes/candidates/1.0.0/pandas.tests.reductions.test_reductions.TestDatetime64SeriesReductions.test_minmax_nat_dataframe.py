@pytest.mark.parametrize('nat_df', [pd.DataFrame([pd.NaT, pd.NaT]), pd.DataFrame([pd.NaT, pd.Timedelta('nat')]), pd.DataFrame([pd.Timedelta('nat'), pd.Timedelta('nat')])])
def test_minmax_nat_dataframe(self, nat_df):
    assert nat_df.min()[0] is pd.NaT
    assert nat_df.max()[0] is pd.NaT
    assert nat_df.min(skipna=False)[0] is pd.NaT
    assert nat_df.max(skipna=False)[0] is pd.NaT