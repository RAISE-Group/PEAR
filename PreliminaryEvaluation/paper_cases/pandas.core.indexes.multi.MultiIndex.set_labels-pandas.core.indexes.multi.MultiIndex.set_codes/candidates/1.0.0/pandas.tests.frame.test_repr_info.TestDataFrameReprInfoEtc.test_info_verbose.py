def test_info_verbose(self):
    buf = StringIO()
    size = 1001
    start = 5
    frame = DataFrame(np.random.randn(3, size))
    frame.info(verbose=True, buf=buf)
    res = buf.getvalue()
    header = ' #    Column  Dtype  \n---   ------  -----  '
    assert header in res
    frame.info(verbose=True, buf=buf)
    buf.seek(0)
    lines = buf.readlines()
    assert len(lines) > 0
    for i, line in enumerate(lines):
        if i >= start and i < start + size:
            index = i - start
            line_nr = ' {} '.format(index)
            assert line.startswith(line_nr)