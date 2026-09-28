def _reindex_output(self, output: FrameOrSeries, fill_value: Scalar=np.NaN) -> FrameOrSeries:
    """
        If we have categorical groupers, then we might want to make sure that
        we have a fully re-indexed output to the levels. This means expanding
        the output space to accommodate all values in the cartesian product of
        our groups, regardless of whether they were observed in the data or
        not. This will expand the output space if there are missing groups.

        The method returns early without modifying the input if the number of
        groupings is less than 2, self.observed == True or none of the groupers
        are categorical.

        Parameters
        ----------
        output : Series or DataFrame
            Object resulting from grouping and applying an operation.
        fill_value : scalar, default np.NaN
            Value to use for unobserved categories if self.observed is False.

        Returns
        -------
        Series or DataFrame
            Object (potentially) re-indexed to include all possible groups.
        """
    groupings = self.grouper.groupings
    if groupings is None:
        return output
    elif len(groupings) == 1:
        return output
    elif self.observed:
        return output
    elif not any((isinstance(ping.grouper, (Categorical, CategoricalIndex)) for ping in groupings)):
        return output
    levels_list = [ping.group_index for ping in groupings]
    index, _ = MultiIndex.from_product(levels_list, names=self.grouper.names).sortlevel()
    if self.as_index:
        d = {self.obj._get_axis_name(self.axis): index, 'copy': False, 'fill_value': fill_value}
        return output.reindex(**d)
    in_axis_grps = ((i, ping.name) for i, ping in enumerate(groupings) if ping.in_axis)
    g_nums, g_names = zip(*in_axis_grps)
    output = output.drop(labels=list(g_names), axis=1)
    output = output.set_index(self.grouper.result_index).reindex(index, copy=False, fill_value=fill_value)
    output = output.reset_index(level=g_nums)
    return output.reset_index(drop=True)