"""Import system"""
import sys

file = open("output.md", "w+", encoding="utf-8")
formatters = ['plain', 'bold', 'italic',
              'header', 'link', 'inline-code',
              'ordered-list', 'unordered-list', 'new-line']
TEXT = ''


def lists(list_type):
    """Adds oredered or unoredered lists"""
    rows = 1
    try:
        rows = int(input('Number of rows:> '))
    except ValueError:
        print("You typed non integer")
    finally:
        for i in range(1, rows + 1):
            user_text = input(f'Row#{i}')
            if list_type != 'un':
                return f'\n{i}.{user_text}'
            if list_type == 'un':
                return f'*\n{user_text}'

def plain_text():
    """Makes plain type of text"""
    user_text = input("Text:> ")
    return f'{user_text} '


def bold_text():
    """Makes bold type of text"""
    user_text = input("Text:> ")
    return f'__{user_text}__ '


def italic_text():
    """Makes italic type of text"""
    user_text = input("Text:> ")
    return f'*{user_text}* '


def header():
    """Makes header type of text"""
    user_text = input("Text:> ")
    header_level = 1
    try:
        header_level = int(input('Level:>(From 1 to 16) '))
    except ValueError:
        print('You typed non integer')
    finally:
        if header_level > 16:
            print("Maximum is 16")
        elif header_level <= 0:
            print("Minimum is 1")
        else:
            return f'{"#" * header_level} {user_text} '


def link():
    """Makes link type of text"""
    label = input('Label:> ')
    url = input('URL:> ')
    return f'[{label}]({url}) '


def inline_code():
    """Makes incode code type of text"""
    user_text = input('Code:> ')
    return f'`{user_text}` '


def process(argument):
    """Adds markdowned text"""
    text_s = ''
    match argument:
        case 'plain':
            text_s += plain_text()
        case 'bold':
            text_s += bold_text()
            # print_markdown()
        case 'italic':
            text_s += italic_text()
        case 'header':
            text_s += header()
        case 'link':
            text_s += link()
        case 'inline-code':
            text_s += inline_code()
        case 'ordered-list':
            text_s += lists('ord')
        case 'unordered-list':
            text_s += lists('un')
        case 'new-line':
            text_s += '\n'
    return text_s

def menu():
    """Menu printing"""
    print(f'Available formatters: {" ".join(formatters)}')


if __name__ == "__main__":
    while True:
        user_command = input('Choose a formatter(or type !help)\n>')
        if user_command == '!help':
            menu()
        elif user_command == '!done':
            file.write(TEXT)
            file.close()
            sys.exit()
        elif user_command in formatters:
            TEXT += process(user_command)
            print(TEXT)
        else:
            print('Unknown formatting type or command')
#DeFakto
