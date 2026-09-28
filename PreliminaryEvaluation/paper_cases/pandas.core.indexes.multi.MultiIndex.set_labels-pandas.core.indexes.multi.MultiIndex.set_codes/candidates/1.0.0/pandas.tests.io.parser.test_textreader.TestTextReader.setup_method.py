@pytest.fixture(autouse=True)
def setup_method(self, datapath):
    self.dirpath = datapath('io', 'parser', 'data')
    self.csv1 = os.path.join(self.dirpath, 'test1.csv')
    self.csv2 = os.path.join(self.dirpath, 'test2.csv')
    self.xls1 = os.path.join(self.dirpath, 'test.xls')