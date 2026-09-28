def test_python_engine_file_no_next(self, python_engine):

    class NoNextBuffer:

        def __init__(self, csv_data):
            self.data = csv_data

        def __iter__(self):
            return self

        def read(self):
            return self.data
    data = 'a\n1'
    msg = "The 'python' engine cannot iterate"
    with pytest.raises(ValueError, match=msg):
        read_csv(NoNextBuffer(data), engine=python_engine)