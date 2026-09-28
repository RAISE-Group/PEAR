def test_fancy_getitem_slice_mixed(self, float_frame, float_string_frame):
    sliced = float_string_frame.iloc[:, -3:]
    assert sliced['D'].dtype == np.float64
    sliced = float_frame.iloc[:, -3:]
    with pytest.raises(com.SettingWithCopyError):
        sliced['C'] = 4.0
    assert (float_frame['C'] == 4).all()