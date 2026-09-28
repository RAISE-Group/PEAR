def setup_data(self):
    nan_df1 = DataFrame(rand(10, 5))
    nan_df1[nan_df1 > 0.5] = np.nan
    nan_df2 = DataFrame(rand(10, 5))
    nan_df2[nan_df2 > 0.5] = np.nan
    self.pandas_lhses = (DataFrame(randn(10, 5)), Series(randn(5)), Series([1, 2, np.nan, np.nan, 5]), nan_df1)
    self.pandas_rhses = (DataFrame(randn(10, 5)), Series(randn(5)), Series([1, 2, np.nan, np.nan, 5]), nan_df2)
    self.scalar_lhses = (randn(),)
    self.scalar_rhses = (randn(),)
    self.lhses = self.pandas_lhses + self.scalar_lhses
    self.rhses = self.pandas_rhses + self.scalar_rhses