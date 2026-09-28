def setup_method(self, method):
    import matplotlib as mpl
    from pandas.plotting._matplotlib import compat
    mpl.rcdefaults()
    self.mpl_ge_2_2_3 = compat._mpl_ge_2_2_3()
    self.mpl_ge_3_0_0 = compat._mpl_ge_3_0_0()
    self.mpl_ge_3_1_0 = compat._mpl_ge_3_1_0()
    self.bp_n_objects = 7
    self.polycollection_factor = 2
    self.default_figsize = (6.4, 4.8)
    self.default_tick_position = 'left'
    n = 100
    with tm.RNGContext(42):
        gender = np.random.choice(['Male', 'Female'], size=n)
        classroom = np.random.choice(['A', 'B', 'C'], size=n)
        self.hist_df = DataFrame({'gender': gender, 'classroom': classroom, 'height': random.normal(66, 4, size=n), 'weight': random.normal(161, 32, size=n), 'category': random.randint(4, size=n)})
    self.tdf = tm.makeTimeDataFrame()
    self.hexbin_df = DataFrame({'A': np.random.uniform(size=20), 'B': np.random.uniform(size=20), 'C': np.arange(20) + np.random.uniform(size=20)})