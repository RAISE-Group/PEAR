def test_metadata_propagation_indiv(self):
    o = Series(range(3), range(3))
    o.name = 'foo'
    o2 = Series(range(3), range(3))
    o2.name = 'bar'
    result = o.T
    self.check_metadata(o, result)
    ts = Series(np.random.rand(1000), index=date_range('20130101', periods=1000, freq='s'), name='foo')
    result = ts.resample('1T').mean()
    self.check_metadata(ts, result)
    result = ts.resample('1T').min()
    self.check_metadata(ts, result)
    result = ts.resample('1T').apply(lambda x: x.sum())
    self.check_metadata(ts, result)
    _metadata = Series._metadata
    _finalize = Series.__finalize__
    Series._metadata = ['name', 'filename']
    o.filename = 'foo'
    o2.filename = 'bar'

    def finalize(self, other, method=None, **kwargs):
        for name in self._metadata:
            if method == 'concat' and name == 'filename':
                value = '+'.join([getattr(o, name) for o in other.objs if getattr(o, name, None)])
                object.__setattr__(self, name, value)
            else:
                object.__setattr__(self, name, getattr(other, name, None))
        return self
    Series.__finalize__ = finalize
    result = pd.concat([o, o2])
    assert result.filename == 'foo+bar'
    assert result.name is None
    Series._metadata = _metadata
    Series.__finalize__ = _finalize