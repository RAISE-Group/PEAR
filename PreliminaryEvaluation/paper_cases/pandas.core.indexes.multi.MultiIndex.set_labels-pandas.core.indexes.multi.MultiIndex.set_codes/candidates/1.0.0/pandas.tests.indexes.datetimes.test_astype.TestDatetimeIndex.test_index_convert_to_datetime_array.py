def test_index_convert_to_datetime_array(self):

    def _check_rng(rng):
        converted = rng.to_pydatetime()
        assert isinstance(converted, np.ndarray)
        for x, stamp in zip(converted, rng):
            assert isinstance(x, datetime)
            assert x == stamp.to_pydatetime()
            assert x.tzinfo == stamp.tzinfo
    rng = date_range('20090415', '20090519')
    rng_eastern = date_range('20090415', '20090519', tz='US/Eastern')
    rng_utc = date_range('20090415', '20090519', tz='utc')
    _check_rng(rng)
    _check_rng(rng_eastern)
    _check_rng(rng_utc)