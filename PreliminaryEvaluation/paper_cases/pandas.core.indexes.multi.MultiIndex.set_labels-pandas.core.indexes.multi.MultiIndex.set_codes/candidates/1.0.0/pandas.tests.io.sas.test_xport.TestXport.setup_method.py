@pytest.fixture(autouse=True)
def setup_method(self, datapath):
    self.dirpath = datapath('io', 'sas', 'data')
    self.file01 = os.path.join(self.dirpath, 'DEMO_G.xpt')
    self.file02 = os.path.join(self.dirpath, 'SSHSV1_A.xpt')
    self.file03 = os.path.join(self.dirpath, 'DRXFCD_G.xpt')
    self.file04 = os.path.join(self.dirpath, 'paxraw_d_short.xpt')