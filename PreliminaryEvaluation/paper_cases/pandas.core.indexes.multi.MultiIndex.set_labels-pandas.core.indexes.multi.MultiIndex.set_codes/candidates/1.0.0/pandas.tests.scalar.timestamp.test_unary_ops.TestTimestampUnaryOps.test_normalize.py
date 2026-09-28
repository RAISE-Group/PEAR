@pytest.mark.parametrize('arg', ['2013-11-30', '2013-11-30 12:00:00'])
def test_normalize(self, tz_naive_fixture, arg):
    tz = tz_naive_fixture
    ts = Timestamp(arg, tz=tz)
    result = ts.normalize()
    expected = Timestamp('2013-11-30', tz=tz)
    assert result == expected