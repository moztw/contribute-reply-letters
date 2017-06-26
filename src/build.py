import os
import jinja2

TEMPLATE_PATH="./template_mailer.jinja.py"
OUTPUT_PATH="./mailer.py"
interests = [
    '_header',
    '_footer',
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

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

def get_email_contents():
    contents = []
    for section in interests:
        with open('../emails/{0}.txt'.format(section), 'r') as f:
            contents.append({'name': section, 'text': f.read()})
    return contents

def main():
    output = render(TEMPLATE_PATH, {'interests': get_email_contents()})
    with open(OUTPUT_PATH, 'w') as f:
        f.write(output)
    print("Successfully generated " + OUTPUT_PATH)

if __name__ == "__main__":
    main()
