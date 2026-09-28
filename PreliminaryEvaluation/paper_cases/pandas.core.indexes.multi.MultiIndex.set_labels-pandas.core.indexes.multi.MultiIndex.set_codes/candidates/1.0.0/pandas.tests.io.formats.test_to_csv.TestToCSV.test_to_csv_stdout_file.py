def test_to_csv_stdout_file(self, capsys):
    df = pd.DataFrame([['foo', 'bar'], ['baz', 'qux']], columns=['name_1', 'name_2'])
    expected_rows = [',name_1,name_2', '0,foo,bar', '1,baz,qux']
    expected_ascii = tm.convert_rows_list_to_csv_str(expected_rows)
    df.to_csv(sys.stdout, encoding='ascii')
    captured = capsys.readouterr()
    assert captured.out == expected_ascii
    assert not sys.stdout.closed