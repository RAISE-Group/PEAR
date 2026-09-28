def test_offset_timedelta64_arg(self, offset_types):
    off = self._get_offset(offset_types)
    td64 = np.timedelta64(4567, 's')
    with pytest.raises(TypeError, match='argument must be an integer'):
        type(off)(n=td64, **off.kwds)