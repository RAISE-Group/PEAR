def test_apply_nested_result_axis_1(self):

    def apply_list(row):
        return [2 * row['A'], 2 * row['C'], 2 * row['B']]
    df = pd.DataFrame(np.zeros((4, 4)), columns=list('ABCD'))
    result = df.apply(apply_list, axis=1)
    expected = Series([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    tm.assert_series_equal(result, expected)