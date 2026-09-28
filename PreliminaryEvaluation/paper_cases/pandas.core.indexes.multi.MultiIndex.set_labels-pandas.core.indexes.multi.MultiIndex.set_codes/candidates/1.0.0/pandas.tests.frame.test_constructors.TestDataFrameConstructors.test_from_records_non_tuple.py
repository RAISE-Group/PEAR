def test_from_records_non_tuple(self):

    class Record:

        def __init__(self, *args):
            self.args = args

        def __getitem__(self, i):
            return self.args[i]

        def __iter__(self):
            return iter(self.args)
    recs = [Record(1, 2, 3), Record(4, 5, 6), Record(7, 8, 9)]
    tups = [tuple(rec) for rec in recs]
    result = DataFrame.from_records(recs)
    expected = DataFrame.from_records(tups)
    tm.assert_frame_equal(result, expected)