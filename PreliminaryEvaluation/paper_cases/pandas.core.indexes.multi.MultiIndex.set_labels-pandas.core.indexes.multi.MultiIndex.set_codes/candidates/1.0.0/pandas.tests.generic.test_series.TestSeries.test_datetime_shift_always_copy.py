@pytest.mark.parametrize('move_by_freq', [pd.Timedelta('1D'), pd.Timedelta('1M')])
def test_datetime_shift_always_copy(self, move_by_freq):
    s = pd.Series(range(5), index=pd.date_range('2017', periods=5))
    assert s.shift(freq=move_by_freq) is not s