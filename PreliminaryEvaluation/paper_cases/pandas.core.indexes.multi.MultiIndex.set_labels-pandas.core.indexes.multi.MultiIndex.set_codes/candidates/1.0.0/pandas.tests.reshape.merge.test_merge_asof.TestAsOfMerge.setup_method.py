@pytest.fixture(autouse=True)
def setup_method(self, datapath):
    self.trades = self.read_data(datapath, 'trades.csv')
    self.quotes = self.read_data(datapath, 'quotes.csv', dedupe=True)
    self.asof = self.read_data(datapath, 'asof.csv')
    self.tolerance = self.read_data(datapath, 'tolerance.csv')
    self.allow_exact_matches = self.read_data(datapath, 'allow_exact_matches.csv')
    self.allow_exact_matches_and_tolerance = self.read_data(datapath, 'allow_exact_matches_and_tolerance.csv')