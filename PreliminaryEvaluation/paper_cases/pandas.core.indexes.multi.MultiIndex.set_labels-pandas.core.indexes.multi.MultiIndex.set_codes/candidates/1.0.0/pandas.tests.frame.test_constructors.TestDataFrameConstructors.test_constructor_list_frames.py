def test_constructor_list_frames(self):
    result = DataFrame([DataFrame()])
    assert result.shape == (1, 0)
    result = DataFrame([DataFrame(dict(A=np.arange(5)))])
    assert isinstance(result.iloc[0, 0], DataFrame)