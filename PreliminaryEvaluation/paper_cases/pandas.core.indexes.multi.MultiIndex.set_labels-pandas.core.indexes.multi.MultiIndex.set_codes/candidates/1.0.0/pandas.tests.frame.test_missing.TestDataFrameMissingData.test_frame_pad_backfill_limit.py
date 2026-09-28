def test_frame_pad_backfill_limit(self):
    index = np.arange(10)
    df = DataFrame(np.random.randn(10, 4), index=index)
    result = df[:2].reindex(index, method='pad', limit=5)
    expected = df[:2].reindex(index).fillna(method='pad')
    expected.values[-3:] = np.nan
    tm.assert_frame_equal(result, expected)
    result = df[-2:].reindex(index, method='backfill', limit=5)
    expected = df[-2:].reindex(index).fillna(method='backfill')
    expected.values[:3] = np.nan
    tm.assert_frame_equal(result, expected)