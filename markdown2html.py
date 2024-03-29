#!/usr/bin/python3

"""
Markdown script using python.
"""
import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

<<<<<<< HEAD
def parse_markdown_unordered_list(line):
    """
    Parses Markdown unordered list syntax and generates corresponding HTML.
    Returns the HTML representation of the list.
    """
<<<<<<< HEAD
    match = re.match(r'^-\s(.*)$', line)
=======
    match = re.match(r'^\*\s(.*)$', line)
    if match:
        list_item = match.group(1)
        return f'<li>{list_item}</li>\n'
    else:
        return None

def parse_markdown_ordered_list(line):
    """
    Parses Markdown ordered list syntax and generates corresponding HTML.
    Returns the HTML representation of the list.
    """
    match = re.match(r'^\d+\.\s(.*)$', line)
>>>>>>> 3cc326b27869e281773cf022d8095c1834a6de20
    if match:
        list_item = match.group(1)
        return f'<li>{list_item}</li>\n'
    else:
        return None

<<<<<<< HEAD
=======
def parse_markdown_paragraph(line):
    """
    Parses Markdown paragraph syntax and generates corresponding HTML.
    Returns the HTML representation of the paragraph.
    """
    if line.strip():
        return f'<p>\n    {line.strip()}\n</p>\n'
    else:
        return None

>>>>>>> 3cc326b27869e281773cf022d8095c1834a6de20
if __name__ == '__main__':
    # Test that the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)
=======
    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            # bold syntax
            for line in read:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                # md5
                md5 = re.findall(r'\[\[.+?\]\]', line)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = line.replace(md5[0], hashlib.md5(
                        md5_inside[0].encode()).hexdigest())

                # remove the letter C
                remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
                if remove_letter_c:
                    remove_c_more = ''.join(
                        c for c in remove_c_more[0] if c not in 'Cc')
                    line = line.replace(remove_letter_c[0], remove_c_more)

                length = len(line)
                headings = line.lstrip('#')
                heading_num = length - len(headings)
                unordered = line.lstrip('-')
                unordered_num = length - len(unordered)
                ordered = line.lstrip('*')
                ordered_num = length - len(ordered)
                # headings, lists
                if 1 <= heading_num <= 6:
                    line = '<h{}>'.format(
                        heading_num) + headings.strip() + '</h{}>\n'.format(
                        heading_num)
>>>>>>> 9de0f0359cc901a5d8f9c2744aae753fca29b1f0

                if unordered_num:
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    line = '<li>' + unordered.strip() + '</li>\n'
                if unordered_start and not unordered_num:
                    html.write('</ul>\n')
                    unordered_start = False

                if ordered_num:
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    line = '<li>' + ordered.strip() + '</li>\n'
                if ordered_start and not ordered_num:
                    html.write('</ol>\n')
                    ordered_start = False

<<<<<<< HEAD
    # Parse Markdown and generate HTML
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.readlines()
        html_content = []
        in_list = False
        for line in md_content:
<<<<<<< HEAD
            html_line = parse_markdown_heading(line) or parse_markdown_unordered_list(line)
            if html_line:
                if not in_list and html_line.startswith('<li>'):
                    html_content.append('<ul>\n')
                    in_list = True
                html_content.append(html_line)
            elif in_list:
                html_content.append('</ul>\n')
=======
            html_line = parse_markdown_heading(line) or parse_markdown_unordered_list(line) or parse_markdown_ordered_list(line) or parse_markdown_paragraph(line)
            if html_line:
                if not in_list and html_line.startswith('<li>'):
                    html_content.append('<ul>\n') if html_line.startswith('<li>*') else html_content.append('<ol>\n')
                    in_list = True
                html_content.append(html_line)
            elif in_list:
                html_content.append('</ul>\n') if html_line.startswith('</li>') else html_content.append('</ol>\n')
>>>>>>> 3cc326b27869e281773cf022d8095c1834a6de20
                in_list = False
            else:
                html_content.append(line)

    # Write HTML content to output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_content)
<<<<<<< HEAD
=======

>>>>>>> 3cc326b27869e281773cf022d8095c1834a6de20
=======
                if not (heading_num or unordered_start or ordered_start):
                    if not paragraph and length > 1:
                        html.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.write('</p>\n')
                        paragraph = False

                if length > 1:
                    html.write(line)

            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')
    exit (0)
>>>>>>> 9de0f0359cc901a5d8f9c2744aae753fca29b1f0
