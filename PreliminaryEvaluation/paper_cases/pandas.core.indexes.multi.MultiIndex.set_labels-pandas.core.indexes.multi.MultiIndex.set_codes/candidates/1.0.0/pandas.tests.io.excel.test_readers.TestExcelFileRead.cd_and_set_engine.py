@pytest.fixture(autouse=True)
def cd_and_set_engine(self, engine, datapath, monkeypatch):
    """
        Change directory and set engine for ExcelFile objects.
        """
    func = partial(pd.ExcelFile, engine=engine)
    monkeypatch.chdir(datapath('io', 'data', 'excel'))
    monkeypatch.setattr(pd, 'ExcelFile', func)