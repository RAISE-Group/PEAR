@pytest.mark.parametrize('other', [1, np.int64(1), 1.0, np.timedelta64('NaT'), pd.Timedelta(days=2), 'invalid', np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9, np.arange(10).view('timedelta64[ns]') * 24 * 3600 * 10 ** 9, pd.Timestamp.now().to_period('D')])
@pytest.mark.parametrize('index', [True, pytest.param(False, marks=pytest.mark.xfail(reason='Raises ValueError instead of TypeError', raises=ValueError))])
def test_searchsorted_invalid_types(self, other, index):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = DatetimeArray(data, freq='D')
    if index:
        arr = pd.Index(arr)
    msg = 'searchsorted requires compatible dtype or scalar'
    with pytest.raises(TypeError, match=msg):
        arr.searchsorted(other)