@pytest.mark.parametrize('categories', [list('abcd'), np.arange(1000), ['a', 'b', 10, 2, 1.3, True], [True, False], pd.date_range('2017', periods=4)])
def test_basic(self, categories, ordered_fixture):
    c1 = CategoricalDtype(categories, ordered=ordered_fixture)
    tm.assert_index_equal(c1.categories, pd.Index(categories))
    assert c1.ordered is ordered_fixture