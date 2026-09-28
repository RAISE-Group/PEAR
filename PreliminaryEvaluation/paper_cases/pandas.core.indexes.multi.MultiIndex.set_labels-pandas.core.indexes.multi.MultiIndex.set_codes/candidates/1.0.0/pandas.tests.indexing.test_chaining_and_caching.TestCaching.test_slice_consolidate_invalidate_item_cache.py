def test_slice_consolidate_invalidate_item_cache(self):
    with option_context('chained_assignment', None):
        df = DataFrame({'aa': np.arange(5), 'bb': [2.2] * 5})
        df['cc'] = 0.0
        df['bb']
        repr(df)
        df['bb'].iloc[0] = 0.17
        df._clear_item_cache()
        tm.assert_almost_equal(df['bb'][0], 0.17)