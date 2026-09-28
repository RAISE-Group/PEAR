def test_invalid(self):
    msg = 'only list-like objects are allowed to be passed to isin\\(\\), you passed a \\[int\\]'
    with pytest.raises(TypeError, match=msg):
        algos.isin(1, 1)
    with pytest.raises(TypeError, match=msg):
        algos.isin(1, [1])
    with pytest.raises(TypeError, match=msg):
        algos.isin([1], 1)