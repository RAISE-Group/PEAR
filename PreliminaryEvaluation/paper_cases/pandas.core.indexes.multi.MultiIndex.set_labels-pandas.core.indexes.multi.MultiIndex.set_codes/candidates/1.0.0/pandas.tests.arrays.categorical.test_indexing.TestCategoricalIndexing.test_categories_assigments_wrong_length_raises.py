@pytest.mark.parametrize('new_categories', [[1, 2, 3, 4], [1, 2]])
def test_categories_assigments_wrong_length_raises(self, new_categories):
    cat = Categorical(['a', 'b', 'c', 'a'])
    msg = 'new categories need to have the same number of items as the old categories!'
    with pytest.raises(ValueError, match=msg):
        cat.categories = new_categories