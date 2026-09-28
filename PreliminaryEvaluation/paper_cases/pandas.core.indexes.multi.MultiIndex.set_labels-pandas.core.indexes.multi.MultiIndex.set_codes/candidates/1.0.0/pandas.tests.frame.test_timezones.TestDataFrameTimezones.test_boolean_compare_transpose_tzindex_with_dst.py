@pytest.mark.parametrize('tz', [None, 'America/New_York'])
def test_boolean_compare_transpose_tzindex_with_dst(self, tz):
    idx = date_range('20161101', '20161130', freq='4H', tz=tz)
    df = DataFrame({'a': range(len(idx)), 'b': range(len(idx))}, index=idx)
    result = df.T == df.T
    expected = DataFrame(True, index=list('ab'), columns=idx)
    tm.assert_frame_equal(result, expected)