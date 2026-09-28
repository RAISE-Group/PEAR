@pytest.mark.parametrize('sparse', [True, False])
def test_get_dummies_dont_sparsify_all_columns(self, sparse):
    df = DataFrame.from_dict(OrderedDict([('GDP', [1, 2]), ('Nation', ['AB', 'CD'])]))
    df = get_dummies(df, columns=['Nation'], sparse=sparse)
    df2 = df.reindex(columns=['GDP'])
    tm.assert_frame_equal(df[['GDP']], df2)