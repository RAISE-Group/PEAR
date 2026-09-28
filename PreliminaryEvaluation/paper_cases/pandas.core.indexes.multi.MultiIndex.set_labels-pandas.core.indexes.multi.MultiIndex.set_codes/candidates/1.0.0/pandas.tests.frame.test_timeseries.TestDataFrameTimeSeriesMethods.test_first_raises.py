def test_first_raises(self):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(TypeError):
        df.first('1D')