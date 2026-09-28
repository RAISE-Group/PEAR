@classmethod
def _get_stacked_values(cls, ax, stacking_id, values, label):
    if stacking_id is None:
        return values
    if not hasattr(ax, '_stacker_pos_prior'):
        cls._initialize_stacker(ax, stacking_id, len(values))
    if (values >= 0).all():
        return ax._stacker_pos_prior[stacking_id] + values
    elif (values <= 0).all():
        return ax._stacker_neg_prior[stacking_id] + values
    raise ValueError(f'When stacked is True, each column must be either all positive or negative.{label} contains both positive and negative values')