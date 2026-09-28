@pytest.mark.parametrize('obj', [pd.Timedelta(seconds=1), pd.Timedelta(seconds=1).to_timedelta64(), pd.Timedelta(seconds=1).to_pytimedelta()])
def test_setitem_objects(self, obj):
    tdi = pd.timedelta_range('2 Days', periods=4, freq='H')
    arr = TimedeltaArray(tdi, freq=tdi.freq)
    arr[0] = obj
    assert arr[0] == pd.Timedelta(seconds=1)