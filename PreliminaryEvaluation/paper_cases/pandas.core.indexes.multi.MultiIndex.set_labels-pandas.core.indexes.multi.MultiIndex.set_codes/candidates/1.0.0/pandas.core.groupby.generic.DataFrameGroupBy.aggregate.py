@Substitution(see_also=_agg_see_also_doc, examples=_agg_examples_doc, versionadded='', klass='DataFrame', axis='')
@Appender(_shared_docs['aggregate'])
def aggregate(self, func=None, *args, **kwargs):
    relabeling = func is None and _is_multi_agg_with_relabel(**kwargs)
    if relabeling:
        func, columns, order = _normalize_keyword_aggregation(kwargs)
        kwargs = {}
    elif isinstance(func, list) and len(func) > len(set(func)):
        raise SpecificationError('Function names must be unique if there is no new column names assigned')
    elif func is None:
        raise TypeError("Must provide 'func' or tuples of '(column, aggfunc).")
    func = _maybe_mangle_lambdas(func)
    result, how = self._aggregate(func, *args, **kwargs)
    if how is None:
        return result
    if result is None:
        if self.grouper.nkeys > 1:
            return self._python_agg_general(func, *args, **kwargs)
        elif args or kwargs:
            result = self._aggregate_frame(func, *args, **kwargs)
        elif self.axis == 1:
            result = self._aggregate_frame(func)
        else:
            try:
                result = self._aggregate_multiple_funcs([func], _axis=self.axis)
            except ValueError as err:
                if 'no results' not in str(err):
                    raise
                result = self._aggregate_frame(func)
            else:
                result.columns = Index(result.columns.levels[0], name=self._selected_obj.columns.name)
    if not self.as_index:
        self._insert_inaxis_grouper_inplace(result)
        result.index = np.arange(len(result))
    if relabeling:
        result = result.iloc[:, order]
        result.columns = columns
    return result._convert(datetime=True)