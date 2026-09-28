def test_setitem_with_empty_listlike(self):
    index = pd.Index([], name='idx')
    result = pd.DataFrame(columns=['A'], index=index)
    result['A'] = []
    expected = pd.DataFrame(columns=['A'], index=index)
    tm.assert_index_equal(result.index, expected.index)