# Depends on src/email_contents.py
def format_body(name, interests):
    body = []

    # TODO: we should probably use some template solution
    {% raw %}
    body.append(contents['_header'].replace('{%name%}', name))
    {% endraw %}

    body.append(contents['_footer'])

    return "\n".join(body)
