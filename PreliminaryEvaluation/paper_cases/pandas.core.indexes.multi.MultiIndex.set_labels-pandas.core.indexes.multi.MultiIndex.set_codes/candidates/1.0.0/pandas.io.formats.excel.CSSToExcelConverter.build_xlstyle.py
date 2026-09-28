def build_xlstyle(self, props: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    out = {'alignment': self.build_alignment(props), 'border': self.build_border(props), 'fill': self.build_fill(props), 'font': self.build_font(props), 'number_format': self.build_number_format(props)}

    def remove_none(d: Dict[str, str]) -> None:
        """Remove key where value is None, through nested dicts"""
        for k, v in list(d.items()):
            if v is None:
                del d[k]
            elif isinstance(v, dict):
                remove_none(v)
                if not v:
                    del d[k]
    remove_none(out)
    return out