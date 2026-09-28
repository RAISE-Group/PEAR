@pytest.mark.parametrize('tpl', [tuple([1]), tuple([1, 2])])
def test_index_single_double_tuples(self, tpl):
    idx = pd.Index([tuple([1]), tuple([1, 2])], name='A', tupleize_cols=False)
    df = DataFrame(index=idx)
    result = df.loc[[tpl]]
    idx = pd.Index([tpl], name='A', tupleize_cols=False)
    expected = DataFrame(index=idx)
    tm.assert_frame_equal(result, expected)