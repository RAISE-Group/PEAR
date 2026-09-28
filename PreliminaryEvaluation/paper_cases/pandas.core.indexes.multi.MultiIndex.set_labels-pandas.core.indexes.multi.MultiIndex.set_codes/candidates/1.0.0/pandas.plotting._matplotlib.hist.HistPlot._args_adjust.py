def _args_adjust(self):
    if is_integer(self.bins):
        values = self.data._convert(datetime=True)._get_numeric_data()
        values = np.ravel(values)
        values = values[~isna(values)]
        _, self.bins = np.histogram(values, bins=self.bins, range=self.kwds.get('range', None), weights=self.kwds.get('weights', None))
    if is_list_like(self.bottom):
        self.bottom = np.array(self.bottom)