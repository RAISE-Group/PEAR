@pytest.fixture(params=[IntervalArray.from_arrays, IntervalIndex.from_arrays, create_categorical_intervals, create_series_intervals, create_series_categorical_intervals], ids=['IntervalArray', 'IntervalIndex', 'Categorical[Interval]', 'Series[Interval]', 'Series[Categorical[Interval]]'])
def interval_constructor(self, request):
    """
        Fixture for all pandas native interval constructors.
        To be used as the LHS of IntervalArray comparisons.
        """
    return request.param