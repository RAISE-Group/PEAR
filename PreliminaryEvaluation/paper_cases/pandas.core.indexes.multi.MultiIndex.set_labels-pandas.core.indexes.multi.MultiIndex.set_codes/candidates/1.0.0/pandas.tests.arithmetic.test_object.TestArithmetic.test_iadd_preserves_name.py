def test_iadd_preserves_name(self):
    ser = pd.Series([1, 2, 3])
    ser.index.name = 'foo'
    ser.index += 1
    assert ser.index.name == 'foo'
    ser.index -= 1
    assert ser.index.name == 'foo'