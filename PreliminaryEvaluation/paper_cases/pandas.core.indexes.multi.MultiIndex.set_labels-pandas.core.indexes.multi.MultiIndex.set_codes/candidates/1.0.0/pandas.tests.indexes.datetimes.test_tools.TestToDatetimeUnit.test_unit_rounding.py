@pytest.mark.parametrize('cache', [True, False])
def test_unit_rounding(self, cache):
    result = pd.to_datetime(1434743731.877, unit='s', cache=cache)
    expected = pd.Timestamp('2015-06-19 19:55:31.877000093')
    assert result == expected