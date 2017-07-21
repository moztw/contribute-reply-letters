import os
import jinja2

TEMPLATE_PATH="./template_mailer.jinja.py"
OUTPUT_PATH="./mailer.py"
FORM_TEMPLATE_PATH="../form/index.html.jinja"
FORM_OUTPUT_PATH="../form/index.html"
# The order in the interests will affect the order appear on the HTML form
interests = [
    '_header',
    '_footer',
    'support',
    'qa',
    'coding',
    'marketing',
    'localization',
    'webdev',
    'addons',
    'design',
    'documentation',
    'education',
    'suggestions',
    'issues',
    'other',
]

# This is an ad-hoc l10n setup, let's use better methods later
interests_zh_tw = {
    'addons': "附加元件",
    'coding': "寫程式",
    'design': "視覺設計",
    'documentation': "撰寫文件",
    'education': "教育",
    'issues': "我遇到了 Firefox 的問題，需要幫助",
    'localization': "在地化與翻譯",
    'marketing': "協助宣傳",
    'other': "其他",
    'qa': "品質檢測",
    'suggestions': "我有關於 Firefox 的建議",
    'support': "幫助使用者",
    'webdev': "網頁開發"
}

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

    output = render(FORM_TEMPLATE_PATH,
                    {'interests': filter(lambda x: not x.startswith('_'), interests),
                     'translations': interests_zh_tw})
    with open(FORM_OUTPUT_PATH, 'w') as f:
        f.write(output)
    print("Successfully generated " + FORM_OUTPUT_PATH)

if __name__ == "__main__":
    main()
