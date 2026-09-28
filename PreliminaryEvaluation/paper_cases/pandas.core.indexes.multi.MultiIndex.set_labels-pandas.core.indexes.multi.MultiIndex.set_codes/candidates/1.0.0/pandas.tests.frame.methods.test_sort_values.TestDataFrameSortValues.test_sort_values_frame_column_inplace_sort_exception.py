def test_sort_values_frame_column_inplace_sort_exception(self, float_frame):
    s = float_frame['A']
    with pytest.raises(ValueError, match='This Series is a view'):
        s.sort_values(inplace=True)
    cp = s.copy()
    cp.sort_values()