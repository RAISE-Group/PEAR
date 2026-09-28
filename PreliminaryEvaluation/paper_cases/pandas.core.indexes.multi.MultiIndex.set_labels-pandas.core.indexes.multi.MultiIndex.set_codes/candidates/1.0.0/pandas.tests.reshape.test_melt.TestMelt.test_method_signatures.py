def test_method_signatures(self):
    tm.assert_frame_equal(self.df.melt(), melt(self.df))
    tm.assert_frame_equal(self.df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B']), melt(self.df, id_vars=['id1', 'id2'], value_vars=['A', 'B']))
    tm.assert_frame_equal(self.df.melt(var_name=self.var_name, value_name=self.value_name), melt(self.df, var_name=self.var_name, value_name=self.value_name))
    tm.assert_frame_equal(self.df1.melt(col_level=0), melt(self.df1, col_level=0))