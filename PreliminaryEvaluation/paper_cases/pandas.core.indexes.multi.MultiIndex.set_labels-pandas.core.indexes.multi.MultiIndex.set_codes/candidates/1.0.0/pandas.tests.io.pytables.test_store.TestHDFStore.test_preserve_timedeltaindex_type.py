def test_preserve_timedeltaindex_type(self, setup_path):
    df = DataFrame(np.random.normal(size=(10, 5)))
    df.index = timedelta_range(start='0s', periods=10, freq='1s', name='example')
    with ensure_clean_store(setup_path) as store:
        store['df'] = df
        tm.assert_frame_equal(store['df'], df)