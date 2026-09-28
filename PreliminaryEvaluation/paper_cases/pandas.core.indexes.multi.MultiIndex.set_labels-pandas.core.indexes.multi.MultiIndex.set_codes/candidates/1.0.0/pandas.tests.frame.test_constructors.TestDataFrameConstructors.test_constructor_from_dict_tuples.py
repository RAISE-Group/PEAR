@pytest.mark.parametrize('data_dict, keys', [([{('a',): 1}, {('a',): 2}], [('a',)]), ([OrderedDict([(('a',), 1), (('b',), 2)])], [('a',), ('b',)]), ([{('a', 'b'): 1}], [('a', 'b')])])
def test_constructor_from_dict_tuples(self, data_dict, keys):
    df = DataFrame.from_dict(data_dict)
    result = df.columns
    expected = Index(keys, dtype='object', tupleize_cols=False)
    tm.assert_index_equal(result, expected)