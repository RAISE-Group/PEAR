def test_0d_array(self):
    msg = re.escape('array(1) (0d array) is not JSON serializable at the moment')
    with pytest.raises(TypeError, match=msg):
        ujson.encode(np.array(1))