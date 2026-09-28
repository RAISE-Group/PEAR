@pytest.mark.parametrize('values', [np.array([]), pd.Series(np.array([]))])
def test_is_not_extension_array_dtype(self, values):
    assert not is_extension_array_dtype(values)