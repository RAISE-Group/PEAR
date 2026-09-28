def test_format(self):
    obj = fmt.FloatArrayFormatter(np.array([12, 0], dtype=np.float64))
    result = obj.get_result()
    assert result[0] == ' 12.0'
    assert result[1] == '  0.0'