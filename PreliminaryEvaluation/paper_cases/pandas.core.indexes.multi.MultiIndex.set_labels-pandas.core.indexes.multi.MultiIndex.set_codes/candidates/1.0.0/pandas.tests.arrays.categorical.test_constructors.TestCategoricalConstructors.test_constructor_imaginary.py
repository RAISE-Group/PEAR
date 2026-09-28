@pytest.mark.xfail(reason='Imaginary values not supported in Categorical')
def test_constructor_imaginary(self):
    values = [1, 2, 3 + 1j]
    c1 = Categorical(values)
    tm.assert_index_equal(c1.categories, Index(values))
    tm.assert_numpy_array_equal(np.array(c1), np.array(values))