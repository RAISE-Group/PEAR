@pytest.mark.parametrize('ordered', [False, True])
@pytest.mark.parametrize('labels', [list('yxz'), list('yxy')])
def test_stack_preserve_categorical_dtype(self, ordered, labels):
    cidx = pd.CategoricalIndex(labels, categories=list('xyz'), ordered=ordered)
    df = DataFrame([[10, 11, 12]], columns=cidx)
    result = df.stack()
    midx = pd.MultiIndex.from_product([df.index, cidx])
    expected = Series([10, 11, 12], index=midx)
    tm.assert_series_equal(result, expected)