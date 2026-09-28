def test_misc(self):
    obj = fmt.FloatArrayFormatter(np.array([], dtype=np.float64))
    result = obj.get_result()
    assert len(result) == 0