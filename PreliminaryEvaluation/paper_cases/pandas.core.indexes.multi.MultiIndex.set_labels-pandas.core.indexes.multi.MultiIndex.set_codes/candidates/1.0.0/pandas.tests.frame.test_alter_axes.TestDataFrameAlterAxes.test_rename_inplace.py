def test_rename_inplace(self, float_frame):
    float_frame.rename(columns={'C': 'foo'})
    assert 'C' in float_frame
    assert 'foo' not in float_frame
    c_id = id(float_frame['C'])
    float_frame = float_frame.copy()
    float_frame.rename(columns={'C': 'foo'}, inplace=True)
    assert 'C' not in float_frame
    assert 'foo' in float_frame
    assert id(float_frame['foo']) != c_id