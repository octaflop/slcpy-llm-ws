import http.server
import os
import re
import socketserver
from typing import Dict

from jinja2 import Environment, FileSystemLoader


def process_think_blocks(html_content: str) -> str:
    """Process <think> blocks in HTML content and format them with proper styling"""

    # Find all think blocks using regex
    pattern = r'<think>(.*?)</think>'

    def format_think_block(match):
        content = match.group(1)
        # Split into sentences and clean up
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', content) if s.strip()]

        # Create formatted HTML
        formatted = ['<div class="think-box bg-gray-50 border-l-4 border-blue-400 p-6 my-6 rounded-r-lg shadow-md">',
                     '<p class="mb-4 text-sm text-gray-500 font-semibold">Thinking Process:</p>',
                     '<div class="space-y-4 text-gray-700">']

        for sentence in sentences:
            formatted.append(
                f'<p class="think-line hover:bg-blue-50 p-2 rounded transition-colors duration-200">{sentence}</p>')

        formatted.append('</div></div>')
        return '\n'.join(formatted)

    # Replace all think blocks
    processed_html = re.sub(pattern, format_think_block, html_content, flags=re.DOTALL)
    return processed_html


def render_template(template_path: str, output_context: dict) -> str:
    template_dir, template_name = os.path.split(template_path)
    env = Environment(loader=FileSystemLoader(template_dir))

    # Read the template first
    with open(template_path, 'r') as f:
        content = f.read()

    # Create template and render first
    template = env.from_string(content)
    rendered_content = template.render(output_context)

    # Process think blocks after template rendering
    processed_content = process_think_blocks(rendered_content)

    return processed_content


class TemplateHandler(http.server.SimpleHTTPRequestHandler):
    template_path: str
    context: Dict

    def do_GET(self):
        if self.path == "/":
            # Send response headers
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Render and stream the template
            content = render_template(self.template_path, self.context)
            self.wfile.write(content.encode())
        else:
            # Handle other paths normally
            super().do_GET()


def serve_template(template_path: str, context: dict, port: int = 8000):
    # Configure handler with template info
    TemplateHandler.template_path = template_path
    TemplateHandler.context = context

    # Set up and start the server
    with socketserver.TCPServer(("", port), TemplateHandler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    template_path = "prompts/outputs/_index.html"
    context = {"title": "Prompt Museum", "content": "Rendered Prompt Content"}
    serve_template(template_path, context)
