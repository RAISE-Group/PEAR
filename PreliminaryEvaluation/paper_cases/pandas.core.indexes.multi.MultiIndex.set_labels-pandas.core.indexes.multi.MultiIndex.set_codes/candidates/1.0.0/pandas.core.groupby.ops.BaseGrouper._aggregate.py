def _aggregate(self, result, counts, values, comp_ids, agg_func, is_datetimelike: bool, min_count: int=-1):
    if agg_func is libgroupby.group_nth:
        agg_func(result, counts, values, comp_ids, rank=1, min_count=-1)
    else:
        agg_func(result, counts, values, comp_ids, min_count)
    return result