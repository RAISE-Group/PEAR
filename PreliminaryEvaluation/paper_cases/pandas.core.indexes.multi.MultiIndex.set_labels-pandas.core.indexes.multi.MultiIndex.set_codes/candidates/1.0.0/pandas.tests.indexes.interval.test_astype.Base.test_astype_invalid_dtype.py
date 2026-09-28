def test_astype_invalid_dtype(self, index):
    msg = 'data type ["\']fake_dtype["\'] not understood'
    with pytest.raises(TypeError, match=msg):
        index.astype('fake_dtype')