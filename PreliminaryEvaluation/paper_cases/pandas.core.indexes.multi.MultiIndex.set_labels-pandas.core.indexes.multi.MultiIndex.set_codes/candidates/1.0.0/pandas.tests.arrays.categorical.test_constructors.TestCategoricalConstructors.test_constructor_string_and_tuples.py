@pytest.mark.skipif(_np_version_under1p16, reason='Skipping for NumPy <1.16')
def test_constructor_string_and_tuples(self):
    c = pd.Categorical(np.array(['c', ('a', 'b'), ('b', 'a'), 'c'], dtype=object))
    expected_index = pd.Index([('a', 'b'), ('b', 'a'), 'c'])
    assert c.categories.equals(expected_index)