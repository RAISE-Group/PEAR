def test_metadata_propagation_indiv(self):
    df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.randn(8), 'D': np.random.randn(8)})
    result = df.groupby('A').sum()
    self.check_metadata(df, result)
    df = DataFrame(np.random.randn(1000, 2), index=date_range('20130101', periods=1000, freq='s'))
    result = df.resample('1T')
    self.check_metadata(df, result)
    _metadata = DataFrame._metadata
    _finalize = DataFrame.__finalize__
    np.random.seed(10)
    df1 = DataFrame(np.random.randint(0, 4, (3, 2)), columns=['a', 'b'])
    df2 = DataFrame(np.random.randint(0, 4, (3, 2)), columns=['c', 'd'])
    DataFrame._metadata = ['filename']
    df1.filename = 'fname1.csv'
    df2.filename = 'fname2.csv'

    def finalize(self, other, method=None, **kwargs):
        for name in self._metadata:
            if method == 'merge':
                left, right = (other.left, other.right)
                value = getattr(left, name, '') + '|' + getattr(right, name, '')
                object.__setattr__(self, name, value)
            else:
                object.__setattr__(self, name, getattr(other, name, ''))
        return self
    DataFrame.__finalize__ = finalize
    result = df1.merge(df2, left_on=['a'], right_on=['c'], how='inner')
    assert result.filename == 'fname1.csv|fname2.csv'
    DataFrame._metadata = ['filename']
    df1 = DataFrame(np.random.randint(0, 4, (3, 2)), columns=list('ab'))
    df1.filename = 'foo'

    def finalize(self, other, method=None, **kwargs):
        for name in self._metadata:
            if method == 'concat':
                value = '+'.join([getattr(o, name) for o in other.objs if getattr(o, name, None)])
                object.__setattr__(self, name, value)
            else:
                object.__setattr__(self, name, getattr(other, name, None))
        return self
    DataFrame.__finalize__ = finalize
    result = pd.concat([df1, df1])
    assert result.filename == 'foo+foo'
    DataFrame._metadata = _metadata
    DataFrame.__finalize__ = _finalize