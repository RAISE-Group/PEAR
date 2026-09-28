@pytest.mark.parametrize('tz', [None, 'UTC', 'US/Eastern'])
def test_insert_invalid_na(self, tz):
    idx = pd.DatetimeIndex(['2017-01-01'], tz=tz)
    with pytest.raises(TypeError, match='incompatible label'):
        idx.insert(0, np.timedelta64('NaT'))