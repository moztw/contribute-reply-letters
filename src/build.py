import os
import jinja2

TEMPLATE_PATH="./template_mailer.jinja.py"
OUTPUT_PATH="./mailer.py"

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

def main():
    output = render(TEMPLATE_PATH, {})
    with open(OUTPUT_PATH, 'w') as f:
        f.write(output)
    print("Successfully generated " + OUTPUT_PATH)

if __name__ == "__main__":
    main()
