def test_query_with_nested_strings(self, parser, engine):
    skip_if_no_pandas_parser(parser)
    raw = 'id          event          timestamp\n        1   "page 1 load"   1/1/2014 0:00:01\n        1   "page 1 exit"   1/1/2014 0:00:31\n        2   "page 2 load"   1/1/2014 0:01:01\n        2   "page 2 exit"   1/1/2014 0:01:31\n        3   "page 3 load"   1/1/2014 0:02:01\n        3   "page 3 exit"   1/1/2014 0:02:31\n        4   "page 1 load"   2/1/2014 1:00:01\n        4   "page 1 exit"   2/1/2014 1:00:31\n        5   "page 2 load"   2/1/2014 1:01:01\n        5   "page 2 exit"   2/1/2014 1:01:31\n        6   "page 3 load"   2/1/2014 1:02:01\n        6   "page 3 exit"   2/1/2014 1:02:31\n        '
    df = pd.read_csv(StringIO(raw), sep='\\s{2,}', engine='python', parse_dates=['timestamp'])
    expected = df[df.event == '"page 1 load"']
    res = df.query('\'"page 1 load"\' in event', parser=parser, engine=engine)
    tm.assert_frame_equal(expected, res)