def build_font(self, props) -> Dict[str, Optional[Union[bool, int, str]]]:
    size = props.get('font-size')
    if size is not None:
        assert size.endswith('pt')
        size = float(size[:-2])
    font_names_tmp = re.findall('(?x)\n            (\n            "(?:[^"]|\\\\")+"\n            |\n            \'(?:[^\']|\\\\\')+\'\n            |\n            [^\'",]+\n            )(?=,|\\s*$)\n        ', props.get('font-family', ''))
    font_names = []
    for name in font_names_tmp:
        if name[:1] == '"':
            name = name[1:-1].replace('\\"', '"')
        elif name[:1] == "'":
            name = name[1:-1].replace("\\'", "'")
        else:
            name = name.strip()
        if name:
            font_names.append(name)
    family = None
    for name in font_names:
        if name == 'serif':
            family = 1
            break
        elif name == 'sans-serif':
            family = 2
            break
        elif name == 'cursive':
            family = 4
            break
        elif name == 'fantasy':
            family = 5
            break
    decoration = props.get('text-decoration')
    if decoration is not None:
        decoration = decoration.split()
    else:
        decoration = ()
    return {'name': font_names[0] if font_names else None, 'family': family, 'size': size, 'bold': self.BOLD_MAP.get(props.get('font-weight')), 'italic': self.ITALIC_MAP.get(props.get('font-style')), 'underline': 'single' if 'underline' in decoration else None, 'strike': 'line-through' in decoration or None, 'color': self.color_to_excel(props.get('color')), 'shadow': bool(re.search('^[^#(]*[1-9]', props['text-shadow'])) if 'text-shadow' in props else None}