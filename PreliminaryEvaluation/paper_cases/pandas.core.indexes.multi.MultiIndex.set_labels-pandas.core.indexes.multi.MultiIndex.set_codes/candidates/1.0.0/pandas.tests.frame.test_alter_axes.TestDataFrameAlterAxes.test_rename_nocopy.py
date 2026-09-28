def test_rename_nocopy(self, float_frame):
    renamed = float_frame.rename(columns={'C': 'foo'}, copy=False)
    renamed['foo'] = 1.0
    assert (float_frame['C'] == 1.0).all()