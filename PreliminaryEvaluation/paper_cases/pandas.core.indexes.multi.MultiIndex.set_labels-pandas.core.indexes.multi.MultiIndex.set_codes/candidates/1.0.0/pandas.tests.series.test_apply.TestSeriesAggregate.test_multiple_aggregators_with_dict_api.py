def test_multiple_aggregators_with_dict_api(self):
    s = Series(range(6), dtype='int64', name='series')
    msg = 'nested renamer is not supported'
    with pytest.raises(SpecificationError, match=msg):
        s.agg({'foo': ['min', 'max'], 'bar': ['sum', 'mean']})