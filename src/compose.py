header_path = './emails/_header.txt'
footer_path = './emails/_footer.txt'
interests = [
    'addons',
    'coding',
    'design',
    'documentation',
    'education',
    'infos',
    'issues',
    'localization',
    'marketing',
    'other',
    'qa',
    'suggestions',
    'support',
    'webdev'
]


def format_body(name, interests):
    body = []

    # TODO: we should probably use some template solution
    with open(header_path, 'r') as f:
        header = f.read()
    {% raw %}
    body.append(header.replace('{%name%}', name))
    {% endraw %}

    for section in interests:
        with open('../emails/{0}.txt'.format(section), 'r') as f:
            body.append(f.read())

    with open(footer_path, 'r') as f:
        footer = f.read()
    body.append(footer)

    return "\n".join(body)
