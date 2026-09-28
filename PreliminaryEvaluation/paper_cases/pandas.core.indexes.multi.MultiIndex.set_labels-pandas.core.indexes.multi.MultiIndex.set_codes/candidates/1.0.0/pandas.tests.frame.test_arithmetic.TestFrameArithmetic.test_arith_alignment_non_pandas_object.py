@pytest.mark.parametrize('values', [[1, 2], (1, 2), np.array([1, 2]), range(1, 3), deque([1, 2])])
def test_arith_alignment_non_pandas_object(self, values):
    df = pd.DataFrame({'A': [1, 1], 'B': [1, 1]})
    expected = pd.DataFrame({'A': [2, 2], 'B': [3, 3]})
    result = df + values
    tm.assert_frame_equal(result, expected)