@pytest.mark.parametrize('dtype', ['M8', 'm8'])
@pytest.mark.parametrize('unit', ['ns', 'us', 'ms', 's', 'h', 'm', 'D'])
def test_astype_from_datetimelike_to_objectt(self, dtype, unit):
    dtype = '{}[{}]'.format(dtype, unit)
    arr = np.array([[1, 2, 3]], dtype=dtype)
    df = DataFrame(arr)
    result = df.astype(object)
    assert (result.dtypes == object).all()
    if dtype.startswith('M8'):
        assert result.iloc[0, 0] == pd.to_datetime(1, unit=unit)
    else:
        assert result.iloc[0, 0] == pd.to_timedelta(1, unit=unit)