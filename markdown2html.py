#!/usr/bin/python3
'''
A script that codes markdown to HTML
'''
import sys
import os
import re

def parse_markdown_heading(line):
    """
    Parses Markdown heading syntax and generates corresponding HTML.
    Returns the HTML representation of the heading.
    """
    match = re.match(r'^(#{1,6})\s(.*)$', line)
    if match:
        heading_level = len(match.group(1))
        heading_text = match.group(2)
        return f'<h{heading_level}>{heading_text}</h{heading_level}>\n'
    else:
        return None

def parse_markdown_unordered_list(line):
    """
    Parses Markdown unordered list syntax and generates corresponding HTML.
    Returns the HTML representation of the list.
    """
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
    if match:
        list_item = match.group(1)
        return f'<li>{list_item}</li>\n'
    else:
        return None

def parse_markdown_paragraph(line):
    """
    Parses Markdown paragraph syntax and generates corresponding HTML.
    Returns the HTML representation of the paragraph.
    """
    if line.strip():
        return f'<p>\n    {line.strip()}\n</p>\n'
    else:
        return None

if __name__ == '__main__':
    # Test that the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    # Store the arguments into variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Checks that the markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    # Parse Markdown and generate HTML
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.readlines()
        html_content = []
        in_list = False
        for line in md_content:
            html_line = parse_markdown_heading(line) or parse_markdown_unordered_list(line) or parse_markdown_ordered_list(line) or parse_markdown_paragraph(line)
            if html_line:
                if not in_list and html_line.startswith('<li>'):
                    html_content.append('<ul>\n') if html_line.startswith('<li>*') else html_content.append('<ol>\n')
                    in_list = True
                html_content.append(html_line)
            elif in_list:
                html_content.append('</ul>\n') if html_line.startswith('</li>') else html_content.append('</ol>\n')
                in_list = False
            else:
                html_content.append(line)

    # Write HTML content to output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_content)
