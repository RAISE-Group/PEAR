def build_fill(self, props: Dict[str, str]):
    fill_color = props.get('background-color')
    if fill_color not in (None, 'transparent', 'none'):
        return {'fgColor': self.color_to_excel(fill_color), 'patternType': 'solid'}