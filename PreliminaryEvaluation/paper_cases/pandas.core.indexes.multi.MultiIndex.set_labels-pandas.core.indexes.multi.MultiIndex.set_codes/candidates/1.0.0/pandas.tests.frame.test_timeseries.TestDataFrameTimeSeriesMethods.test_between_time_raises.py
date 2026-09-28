def test_between_time_raises(self):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(TypeError):
        df.between_time(start_time='00:00', end_time='12:00')