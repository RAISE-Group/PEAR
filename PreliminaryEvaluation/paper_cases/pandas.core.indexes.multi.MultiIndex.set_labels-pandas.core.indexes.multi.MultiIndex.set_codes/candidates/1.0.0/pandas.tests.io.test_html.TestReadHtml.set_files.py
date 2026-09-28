@pytest.fixture(autouse=True)
def set_files(self, datapath):
    self.spam_data = datapath('io', 'data', 'html', 'spam.html')
    self.spam_data_kwargs = {}
    self.spam_data_kwargs['encoding'] = 'UTF-8'
    self.banklist_data = datapath('io', 'data', 'html', 'banklist.html')