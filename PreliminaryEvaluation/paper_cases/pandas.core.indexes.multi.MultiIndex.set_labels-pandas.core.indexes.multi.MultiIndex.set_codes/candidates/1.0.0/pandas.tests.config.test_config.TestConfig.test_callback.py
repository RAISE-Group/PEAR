def test_callback(self):
    k = [None]
    v = [None]

    def callback(key):
        k.append(key)
        v.append(self.cf.get_option(key))
    self.cf.register_option('d.a', 'foo', cb=callback)
    self.cf.register_option('d.b', 'foo', cb=callback)
    del k[-1], v[-1]
    self.cf.set_option('d.a', 'fooz')
    assert k[-1] == 'd.a'
    assert v[-1] == 'fooz'
    del k[-1], v[-1]
    self.cf.set_option('d.b', 'boo')
    assert k[-1] == 'd.b'
    assert v[-1] == 'boo'
    del k[-1], v[-1]
    self.cf.reset_option('d.b')
    assert k[-1] == 'd.b'