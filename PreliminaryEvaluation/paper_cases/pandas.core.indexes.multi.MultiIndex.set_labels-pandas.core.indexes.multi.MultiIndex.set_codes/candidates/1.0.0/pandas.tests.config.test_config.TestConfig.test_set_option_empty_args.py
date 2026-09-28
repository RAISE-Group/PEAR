def test_set_option_empty_args(self):
    msg = 'Must provide an even number of non-keyword arguments'
    with pytest.raises(ValueError, match=msg):
        self.cf.set_option()