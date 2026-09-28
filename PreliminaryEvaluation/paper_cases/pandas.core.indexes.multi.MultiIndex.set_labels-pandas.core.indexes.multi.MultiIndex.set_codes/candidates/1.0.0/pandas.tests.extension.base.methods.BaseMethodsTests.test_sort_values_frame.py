@pytest.mark.parametrize('ascending', [True, False])
def test_sort_values_frame(self, data_for_sorting, ascending):
    df = pd.DataFrame({'A': [1, 2, 1], 'B': data_for_sorting})
    result = df.sort_values(['A', 'B'])
    expected = pd.DataFrame({'A': [1, 1, 2], 'B': data_for_sorting.take([2, 0, 1])}, index=[2, 0, 1])
    self.assert_frame_equal(result, expected)