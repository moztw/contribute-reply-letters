# Depends on src/email_contents.py
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
    {% raw %}
    body.append(contents['_header'].replace('{%name%}', name))
    {% endraw %}

    for interest in interests:
        body.append(contents[interest])

    body.append(contents['_footer'])

    return '\n'.join(body)
