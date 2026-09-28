def test_to_csv_list_entries(self):
    s = Series(['jack and jill', 'jesse and frank'])
    split = s.str.split('\\s+and\\s+')
    buf = StringIO()
    split.to_csv(buf, header=False)