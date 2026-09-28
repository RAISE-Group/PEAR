def test_insert_invalid_na(self):
    idx = TimedeltaIndex(['4day', '1day', '2day'], name='idx')
    with pytest.raises(TypeError, match='incompatible label'):
        idx.insert(0, np.datetime64('NaT'))