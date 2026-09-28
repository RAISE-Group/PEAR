def _get_annual_rule(self) -> Optional[str]:
    if len(self.ydiffs) > 1:
        return None
    if len(unique(self.fields['M'])) > 1:
        return None
    pos_check = self.month_position_check()
    return {'cs': 'AS', 'bs': 'BAS', 'ce': 'A', 'be': 'BA'}.get(pos_check)