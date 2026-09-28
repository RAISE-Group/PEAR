@pytest.mark.parametrize('how', ['dict', 'series'])
@pytest.mark.parametrize('to_key', ['datetime64[ns]', 'datetime64[ns, UTC]', 'datetime64[ns, US/Eastern]'])
@pytest.mark.parametrize('from_key', ['datetime64[ns]', 'datetime64[ns, UTC]', 'datetime64[ns, US/Eastern]'])
def test_replace_series_datetime_datetime(self, how, to_key, from_key):
    index = pd.Index([3, 4], name='xyz')
    obj = pd.Series(self.rep[from_key], index=index, name='yyy')
    assert obj.dtype == from_key
    if how == 'dict':
        replacer = dict(zip(self.rep[from_key], self.rep[to_key]))
    elif how == 'series':
        replacer = pd.Series(self.rep[to_key], index=self.rep[from_key])
    else:
        raise ValueError
    result = obj.replace(replacer)
    exp = pd.Series(self.rep[to_key], index=index, name='yyy')
    assert exp.dtype == to_key
    tm.assert_series_equal(result, exp)