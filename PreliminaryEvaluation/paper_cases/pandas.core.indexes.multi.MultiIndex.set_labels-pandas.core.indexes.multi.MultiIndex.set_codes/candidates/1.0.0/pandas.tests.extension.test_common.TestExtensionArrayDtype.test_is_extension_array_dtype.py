@pytest.mark.parametrize('values', [pd.Categorical([]), pd.Categorical([]).dtype, pd.Series(pd.Categorical([])), DummyDtype(), DummyArray(np.array([1, 2]))])
def test_is_extension_array_dtype(self, values):
    assert is_extension_array_dtype(values)