def test_at_time_raises(self):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(TypeError):
        df.at_time('00:00')