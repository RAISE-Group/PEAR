@Substitution(see_also=_agg_see_also_doc, examples=_agg_examples_doc, versionadded='\n.. versionadded:: 0.20.0\n', **_shared_doc_kwargs)
@Appender(generic._shared_docs['aggregate'])
def aggregate(self, func, axis=0, *args, **kwargs):
    self._get_axis_number(axis)
    result, how = self._aggregate(func, *args, **kwargs)
    if result is None:
        kwargs.pop('_axis', None)
        kwargs.pop('_level', None)
        try:
            result = self.apply(func, *args, **kwargs)
        except (ValueError, AttributeError, TypeError):
            result = func(self, *args, **kwargs)
    return result