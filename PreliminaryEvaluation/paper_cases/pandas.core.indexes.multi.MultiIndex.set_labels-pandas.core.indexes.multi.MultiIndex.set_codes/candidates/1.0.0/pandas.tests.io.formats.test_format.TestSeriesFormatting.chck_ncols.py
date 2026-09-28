def chck_ncols(self, s):
    with option_context('display.max_rows', 10):
        res = repr(s)
    lines = res.split('\n')
    lines = [line for line in repr(s).split('\n') if not re.match('[^\\.]*\\.+', line)][:-1]
    ncolsizes = len({len(line.strip()) for line in lines})
    assert ncolsizes == 1