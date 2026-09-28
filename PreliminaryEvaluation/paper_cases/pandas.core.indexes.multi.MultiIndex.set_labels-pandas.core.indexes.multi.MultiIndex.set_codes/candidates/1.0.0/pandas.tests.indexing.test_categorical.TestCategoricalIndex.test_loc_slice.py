def test_loc_slice(self):
    with pytest.raises(KeyError, match='1'):
        self.df.loc[1:5]
    result = self.df.loc['b':'c']
    expected = self.df.iloc[[2, 3, 4]]
    tm.assert_frame_equal(result, expected)