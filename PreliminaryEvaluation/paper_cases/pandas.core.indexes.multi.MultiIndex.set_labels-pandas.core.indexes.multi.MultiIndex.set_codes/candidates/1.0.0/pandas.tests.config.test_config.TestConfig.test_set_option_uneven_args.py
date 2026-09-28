def test_set_option_uneven_args(self):
    msg = 'Must provide an even number of non-keyword arguments'
    with pytest.raises(ValueError, match=msg):
        self.cf.set_option('a.b', 2, 'b.c')