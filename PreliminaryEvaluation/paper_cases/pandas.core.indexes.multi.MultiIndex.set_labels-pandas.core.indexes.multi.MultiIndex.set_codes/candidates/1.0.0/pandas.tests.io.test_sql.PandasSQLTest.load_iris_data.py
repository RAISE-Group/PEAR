@pytest.fixture(params=[('data', 'iris.csv')])
def load_iris_data(self, datapath, request):
    import io
    iris_csv_file = datapath(*request.param)
    if not hasattr(self, 'conn'):
        self.setup_connect()
    self.drop_table('iris')
    self._get_exec().execute(SQL_STRINGS['create_iris'][self.flavor])
    with io.open(iris_csv_file, mode='r', newline=None) as iris_csv:
        r = csv.reader(iris_csv)
        next(r)
        ins = SQL_STRINGS['insert_iris'][self.flavor]
        for row in r:
            self._get_exec().execute(ins, row)