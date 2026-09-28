@pytest.mark.parametrize('cache', [True, False])
def test_unit_consistency(self, cache):
    expected = Timestamp('1970-05-09 14:25:11')
    result = pd.to_datetime(11111111, unit='s', errors='raise', cache=cache)
    assert result == expected
    assert isinstance(result, Timestamp)
    result = pd.to_datetime(11111111, unit='s', errors='coerce', cache=cache)
    assert result == expected
    assert isinstance(result, Timestamp)
    result = pd.to_datetime(11111111, unit='s', errors='ignore', cache=cache)
    assert result == expected
    assert isinstance(result, Timestamp)