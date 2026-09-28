def test_stack_mixed_levels(self):
    columns = MultiIndex.from_tuples([('A', 'cat', 'long'), ('B', 'cat', 'long'), ('A', 'dog', 'short'), ('B', 'dog', 'short')], names=['exp', 'animal', 'hair_length'])
    df = DataFrame(np.random.randn(4, 4), columns=columns)
    animal_hair_stacked = df.stack(level=['animal', 'hair_length'])
    exp_hair_stacked = df.stack(level=['exp', 'hair_length'])
    df2 = df.copy()
    df2.columns.names = ['exp', 'animal', 1]
    tm.assert_frame_equal(df2.stack(level=['animal', 1]), animal_hair_stacked, check_names=False)
    tm.assert_frame_equal(df2.stack(level=['exp', 1]), exp_hair_stacked, check_names=False)
    msg = 'level should contain all level names or all level numbers, not a mixture of the two'
    with pytest.raises(ValueError, match=msg):
        df2.stack(level=['animal', 0])
    df3 = df.copy()
    df3.columns.names = ['exp', 'animal', 0]
    tm.assert_frame_equal(df3.stack(level=['animal', 0]), animal_hair_stacked, check_names=False)