@pytest.mark.parametrize('dtype', [None, 'category'])
def test_from_inferred_categories_sorts(self, dtype):
    cats = ['b', 'a']
    codes = np.array([0, 1, 1, 1], dtype='i8')
    result = Categorical._from_inferred_categories(cats, codes, dtype)
    expected = Categorical.from_codes([1, 0, 0, 0], ['a', 'b'])
    tm.assert_categorical_equal(result, expected)