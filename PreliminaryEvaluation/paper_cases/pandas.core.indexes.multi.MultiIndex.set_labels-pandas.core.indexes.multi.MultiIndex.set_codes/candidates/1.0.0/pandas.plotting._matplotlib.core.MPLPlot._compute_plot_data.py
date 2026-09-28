def _compute_plot_data(self):
    data = self.data
    if isinstance(data, ABCSeries):
        label = self.label
        if label is None and data.name is None:
            label = 'None'
        data = data.to_frame(name=label)
    data = data._convert(datetime=True, timedelta=True)
    include_type = [np.number, 'datetime', 'datetimetz', 'timedelta']
    if self.include_bool is True:
        include_type.append(np.bool_)
    exclude_type = None
    if self._kind == 'box':
        include_type = [np.number]
        exclude_type = ['timedelta']
    if self._kind == 'scatter':
        include_type.extend(['object', 'category'])
    numeric_data = data.select_dtypes(include=include_type, exclude=exclude_type)
    try:
        is_empty = numeric_data.columns.empty
    except AttributeError:
        is_empty = not len(numeric_data)
    if is_empty:
        raise TypeError('no numeric data to plot')
    numeric_data = numeric_data.copy()
    for col in numeric_data:
        numeric_data[col] = np.asarray(numeric_data[col])
    self.data = numeric_data