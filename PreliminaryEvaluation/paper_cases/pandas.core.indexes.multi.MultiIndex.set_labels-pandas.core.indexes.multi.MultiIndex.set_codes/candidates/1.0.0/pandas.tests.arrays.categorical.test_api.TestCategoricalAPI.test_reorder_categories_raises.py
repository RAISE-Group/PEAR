@pytest.mark.parametrize('new_categories', [['a'], ['a', 'b', 'd'], ['a', 'b', 'c', 'd']])
def test_reorder_categories_raises(self, new_categories):
    cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
    msg = 'items in new_categories are not the same as in old categories'
    with pytest.raises(ValueError, match=msg):
        cat.reorder_categories(new_categories)