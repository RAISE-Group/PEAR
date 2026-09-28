@td.skip_if_windows
@pytest.mark.parametrize('timezone', ['US/Pacific', 'US/Eastern', 'UTC', 'Asia/Kolkata', 'Asia/Shanghai', 'Australia/Canberra'])
def test_normalize_tz_local(self, timezone):
    with tm.set_timezone(timezone):
        rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz=tzlocal())
        result = rng.normalize()
        expected = date_range('1/1/2000', periods=10, freq='D', tz=tzlocal())
        tm.assert_index_equal(result, expected)
        assert result.is_normalized
        assert not rng.is_normalized