#!/usr/bin/env python2

import argparse

header_path = '../emails/_header.txt'
footer_path = '../emails/_footer.txt'
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


def compose(name, interests):
    body = []

    # TODO: we should probably use some template solution
    with open(header_path, 'rb') as f:
        header = f.read()
    body.append(header.replace('{%name%}', name))

    for section in interests:
        with open('../emails/{0}.txt'.format(section), 'rb') as f:
            body.append(f.read())

    with open(footer_path, 'rb') as f:
        footer = f.read()
    body.append(footer)

    print("\n".join(body))


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('name', action='store',
                        help='Contributor\'s name')
    parser.add_argument('-i', '--interests', nargs='*', choices=interests,
                        default=[], help='field of interests')

    results = parser.parse_args()

    compose(results.name, results.interests)

if __name__ == "__main__":
    main()
