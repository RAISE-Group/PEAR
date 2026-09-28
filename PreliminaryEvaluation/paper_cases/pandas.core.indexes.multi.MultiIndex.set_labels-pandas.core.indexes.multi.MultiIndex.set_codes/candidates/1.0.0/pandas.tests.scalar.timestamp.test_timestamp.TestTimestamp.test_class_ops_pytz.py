def test_class_ops_pytz(self):

    def compare(x, y):
        assert int((Timestamp(x).value - Timestamp(y).value) / 1000000000.0) == 0
    compare(Timestamp.now(), datetime.now())
    compare(Timestamp.now('UTC'), datetime.now(timezone('UTC')))
    compare(Timestamp.utcnow(), datetime.utcnow())
    compare(Timestamp.today(), datetime.today())
    current_time = calendar.timegm(datetime.now().utctimetuple())
    compare(Timestamp.utcfromtimestamp(current_time), datetime.utcfromtimestamp(current_time))
    compare(Timestamp.fromtimestamp(current_time), datetime.fromtimestamp(current_time))
    date_component = datetime.utcnow()
    time_component = (date_component + timedelta(minutes=10)).time()
    compare(Timestamp.combine(date_component, time_component), datetime.combine(date_component, time_component))