@pytest.mark.parametrize('how', ['dict', 'series'])
@pytest.mark.parametrize('to_key', ['object', 'int64', 'float64', 'complex128', 'bool', 'datetime64[ns]', 'datetime64[ns, UTC]', 'datetime64[ns, US/Eastern]', 'timedelta64[ns]'], ids=['object', 'int64', 'float64', 'complex128', 'bool', 'datetime64', 'datetime64tz', 'datetime64tz', 'timedelta64'])
@pytest.mark.parametrize('from_key', ['object', 'int64', 'float64', 'complex128', 'bool', 'datetime64[ns]', 'datetime64[ns, UTC]', 'datetime64[ns, US/Eastern]', 'timedelta64[ns]'])
def test_replace_series(self, how, to_key, from_key):
    index = pd.Index([3, 4], name='xxx')
    obj = pd.Series(self.rep[from_key], index=index, name='yyy')
    assert obj.dtype == from_key
    if from_key.startswith('datetime') and to_key.startswith('datetime'):
        return
    elif from_key in ['datetime64[ns, US/Eastern]', 'datetime64[ns, UTC]']:
        return
    if how == 'dict':
        replacer = dict(zip(self.rep[from_key], self.rep[to_key]))
    elif how == 'series':
        replacer = pd.Series(self.rep[to_key], index=self.rep[from_key])
    else:
        raise ValueError
    result = obj.replace(replacer)
    if from_key == 'float64' and to_key in 'int64' or (from_key == 'complex128' and to_key in ('int64', 'float64')):
        if compat.is_platform_32bit() or compat.is_platform_windows():
            pytest.skip('32-bit platform buggy: {0} -> {1}'.format(from_key, to_key))
        exp = pd.Series(self.rep[to_key], index=index, name='yyy', dtype=from_key)
    else:
        exp = pd.Series(self.rep[to_key], index=index, name='yyy')
        assert exp.dtype == to_key
    tm.assert_series_equal(result, exp)