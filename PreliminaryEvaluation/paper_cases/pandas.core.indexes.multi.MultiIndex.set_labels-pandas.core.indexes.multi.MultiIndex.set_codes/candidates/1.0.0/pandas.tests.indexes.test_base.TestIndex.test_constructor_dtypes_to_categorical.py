@pytest.mark.parametrize('vals', [[1, 2, 3], np.array([1, 2, 3], dtype=int), np.array([np_datetime64_compat('2011-01-01'), np_datetime64_compat('2011-01-02')]), [datetime(2011, 1, 1), datetime(2011, 1, 2)]])
def test_constructor_dtypes_to_categorical(self, vals):
    index = Index(vals, dtype='category')
    assert isinstance(index, CategoricalIndex)