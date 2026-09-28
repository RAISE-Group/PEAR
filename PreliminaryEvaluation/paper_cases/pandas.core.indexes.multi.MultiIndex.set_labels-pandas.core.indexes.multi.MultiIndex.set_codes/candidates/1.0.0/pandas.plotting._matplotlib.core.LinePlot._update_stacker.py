@classmethod
def _update_stacker(cls, ax, stacking_id, values):
    if stacking_id is None:
        return
    if (values >= 0).all():
        ax._stacker_pos_prior[stacking_id] += values
    elif (values <= 0).all():
        ax._stacker_neg_prior[stacking_id] += values