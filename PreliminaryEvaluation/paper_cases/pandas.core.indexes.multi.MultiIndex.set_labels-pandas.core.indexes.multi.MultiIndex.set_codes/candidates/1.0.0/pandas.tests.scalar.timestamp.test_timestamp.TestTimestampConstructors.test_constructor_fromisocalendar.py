@pytest.mark.skipif(not compat.PY38, reason='datetime.fromisocalendar was added in Python version 3.8')
def test_constructor_fromisocalendar(self):
    expected_timestamp = Timestamp('2000-01-03 00:00:00')
    expected_stdlib = datetime.fromisocalendar(2000, 1, 1)
    result = Timestamp.fromisocalendar(2000, 1, 1)
    assert result == expected_timestamp
    assert result == expected_stdlib
    assert isinstance(result, Timestamp)