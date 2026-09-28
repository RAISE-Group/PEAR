def test_next(self, mmap_file):
    with open(mmap_file, 'r') as target:
        wrapper = icom._MMapWrapper(target)
        lines = target.readlines()
    for line in lines:
        next_line = next(wrapper)
        assert next_line.strip() == line.strip()
    with pytest.raises(StopIteration, match='^$'):
        next(wrapper)