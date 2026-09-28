def test_to_csv_quotechar(self):
    df = DataFrame({'col': [1, 2]})
    expected = '"","col"\n"0","1"\n"1","2"\n'
    with tm.ensure_clean('test.csv') as path:
        df.to_csv(path, quoting=1)
        with open(path, 'r') as f:
            assert f.read() == expected
    expected = '$$,$col$\n$0$,$1$\n$1$,$2$\n'
    with tm.ensure_clean('test.csv') as path:
        df.to_csv(path, quoting=1, quotechar='$')
        with open(path, 'r') as f:
            assert f.read() == expected
    with tm.ensure_clean('test.csv') as path:
        with pytest.raises(TypeError, match='quotechar'):
            df.to_csv(path, quoting=1, quotechar=None)