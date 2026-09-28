@pytest.mark.parametrize('dtype, expected', [('datetime64[ns]', np.array(['2015-01-01T00:00:00.000000000'], dtype='datetime64[ns]')), ('datetime64[ns, MET]', pd.DatetimeIndex([pd.Timestamp('2015-01-01 00:00:00+0100', tz='MET')]).array)])
def test_consistent_casting(self, dtype, expected):
    result = pd.Categorical('2015-01-01').astype(dtype)
    assert result == expected