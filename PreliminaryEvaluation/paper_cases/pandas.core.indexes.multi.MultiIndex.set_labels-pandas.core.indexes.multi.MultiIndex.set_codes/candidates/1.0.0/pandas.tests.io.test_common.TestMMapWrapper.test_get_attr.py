def test_get_attr(self, mmap_file):
    with open(mmap_file, 'r') as target:
        wrapper = icom._MMapWrapper(target)
    attrs = dir(wrapper.mmap)
    attrs = [attr for attr in attrs if not attr.startswith('__')]
    attrs.append('__next__')
    for attr in attrs:
        assert hasattr(wrapper, attr)
    assert not hasattr(wrapper, 'foo')