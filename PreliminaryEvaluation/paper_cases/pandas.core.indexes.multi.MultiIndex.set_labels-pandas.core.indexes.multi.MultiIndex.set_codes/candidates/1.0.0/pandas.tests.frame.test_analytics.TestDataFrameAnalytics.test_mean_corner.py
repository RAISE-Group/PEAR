def test_mean_corner(self, float_frame, float_string_frame):
    the_mean = float_string_frame.mean(axis=0)
    the_sum = float_string_frame.sum(axis=0, numeric_only=True)
    tm.assert_index_equal(the_sum.index, the_mean.index)
    assert len(the_mean.index) < len(float_string_frame.columns)
    the_mean = float_string_frame.mean(axis=1)
    the_sum = float_string_frame.sum(axis=1, numeric_only=True)
    tm.assert_index_equal(the_sum.index, the_mean.index)
    float_frame['bool'] = float_frame['A'] > 0
    means = float_frame.mean(0)
    assert means['bool'] == float_frame['bool'].values.mean()