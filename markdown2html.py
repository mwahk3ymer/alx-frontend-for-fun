import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r') as md_file:
            markdown_content = md_file.read()
            html_content = markdown.markdown(markdown_content)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
