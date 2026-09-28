def test_frame_from_records_utc(self):
    rec = {'datum': 1.5, 'begin_time': datetime(2006, 4, 27, tzinfo=pytz.utc)}
    DataFrame.from_records([rec], index='begin_time')