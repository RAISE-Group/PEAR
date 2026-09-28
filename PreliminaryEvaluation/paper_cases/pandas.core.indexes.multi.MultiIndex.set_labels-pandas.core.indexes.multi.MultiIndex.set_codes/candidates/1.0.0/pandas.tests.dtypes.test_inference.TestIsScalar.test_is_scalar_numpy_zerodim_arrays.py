def test_is_scalar_numpy_zerodim_arrays(self):
    for zerodim in [np.array(1), np.array('foobar'), np.array(np.datetime64('2014-01-01')), np.array(np.timedelta64(1, 'h')), np.array(np.datetime64('NaT'))]:
        assert not is_scalar(zerodim)
        assert is_scalar(lib.item_from_zerodim(zerodim))