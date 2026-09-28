def test_pivot_multi_values(self):
    result = pivot_table(self.data, values=['D', 'E'], index='A', columns=['B', 'C'], fill_value=0)
    expected = pivot_table(self.data.drop(['F'], axis=1), index='A', columns=['B', 'C'], fill_value=0)
    tm.assert_frame_equal(result, expected)