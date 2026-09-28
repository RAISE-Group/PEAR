@pytest.mark.parametrize('op', ['min', 'max'])
def test_minmax_nat_datetime64(self, op):
    obj = DatetimeIndex([])
    assert pd.isna(getattr(obj, op)())
    obj = DatetimeIndex([pd.NaT])
    assert pd.isna(getattr(obj, op)())
    obj = DatetimeIndex([pd.NaT, pd.NaT, pd.NaT])
    assert pd.isna(getattr(obj, op)())