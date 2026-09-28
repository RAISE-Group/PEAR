@pytest.mark.parametrize('new_categories', [list('abc'), list('cba'), list('wxyz'), None])
@pytest.mark.parametrize('new_ordered', [True, False, None])
def test_update_dtype(self, ordered_fixture, new_categories, new_ordered):
    original_categories = list('abc')
    dtype = CategoricalDtype(original_categories, ordered_fixture)
    new_dtype = CategoricalDtype(new_categories, new_ordered)
    result = dtype.update_dtype(new_dtype)
    expected_categories = pd.Index(new_categories or original_categories)
    expected_ordered = new_ordered if new_ordered is not None else dtype.ordered
    tm.assert_index_equal(result.categories, expected_categories)
    assert result.ordered is expected_ordered