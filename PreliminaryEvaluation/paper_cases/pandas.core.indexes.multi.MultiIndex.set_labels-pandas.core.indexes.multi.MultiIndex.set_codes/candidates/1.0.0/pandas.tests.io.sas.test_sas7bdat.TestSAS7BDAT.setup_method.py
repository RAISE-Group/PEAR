@pytest.fixture(autouse=True)
def setup_method(self, datapath):
    self.dirpath = datapath('io', 'sas', 'data')
    self.data = []
    self.test_ix = [list(range(1, 16)), [16]]
    for j in (1, 2):
        fname = os.path.join(self.dirpath, f'test_sas7bdat_{j}.csv')
        df = pd.read_csv(fname)
        epoch = datetime(1960, 1, 1)
        t1 = pd.to_timedelta(df['Column4'], unit='d')
        df['Column4'] = epoch + t1
        t2 = pd.to_timedelta(df['Column12'], unit='d')
        df['Column12'] = epoch + t2
        for k in range(df.shape[1]):
            col = df.iloc[:, k]
            if col.dtype == np.int64:
                df.iloc[:, k] = df.iloc[:, k].astype(np.float64)
        self.data.append(df)