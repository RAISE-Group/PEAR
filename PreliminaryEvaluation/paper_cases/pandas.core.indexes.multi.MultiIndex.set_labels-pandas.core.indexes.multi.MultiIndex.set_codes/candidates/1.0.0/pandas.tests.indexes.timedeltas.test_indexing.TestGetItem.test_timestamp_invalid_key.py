@pytest.mark.parametrize('key', [pd.Timestamp('1970-01-01'), pd.Timestamp('1970-01-02'), datetime(1970, 1, 1)])
def test_timestamp_invalid_key(self, key):
    tdi = pd.timedelta_range(0, periods=10)
    with pytest.raises(TypeError):
        tdi.get_loc(key)