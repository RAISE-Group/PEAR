@pytest.fixture(autouse=True)
def cd_and_set_engine(self, engine, datapath, monkeypatch):
    """
        Change directory and set engine for read_excel calls.
        """
    func = partial(pd.read_excel, engine=engine)
    monkeypatch.chdir(datapath('io', 'data', 'excel'))
    monkeypatch.setattr(pd, 'read_excel', func)