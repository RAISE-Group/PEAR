def test_constructor_bad_file(self, mmap_file):
    non_file = StringIO('I am not a file')
    non_file.fileno = lambda: -1
    if is_platform_windows():
        msg = 'The parameter is incorrect'
        err = OSError
    else:
        msg = '[Errno 22]'
        err = mmap.error
    with pytest.raises(err, match=msg):
        icom._MMapWrapper(non_file)
    target = open(mmap_file, 'r')
    target.close()
    msg = 'I/O operation on closed file'
    with pytest.raises(ValueError, match=msg):
        icom._MMapWrapper(target)