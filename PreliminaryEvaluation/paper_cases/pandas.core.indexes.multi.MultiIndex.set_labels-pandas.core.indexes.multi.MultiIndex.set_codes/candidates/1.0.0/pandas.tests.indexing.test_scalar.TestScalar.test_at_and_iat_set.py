def test_at_and_iat_set(self):

    def _check(f, func, values=False):
        if f is not None:
            indicies = self.generate_indices(f, values)
            for i in indicies:
                getattr(f, func)[i] = 1
                expected = self.get_value(func, f, i, values)
                tm.assert_almost_equal(expected, 1)
    for kind in self._kinds:
        d = getattr(self, kind)
        for f in [d['ints'], d['uints']]:
            _check(f, 'iat', values=True)
        for f in [d['labels'], d['ts'], d['floats']]:
            if f is not None:
                msg = 'iAt based indexing can only have integer indexers'
                with pytest.raises(ValueError, match=msg):
                    _check(f, 'iat')
        for f in [d['ints'], d['uints'], d['labels'], d['ts'], d['floats']]:
            _check(f, 'at')