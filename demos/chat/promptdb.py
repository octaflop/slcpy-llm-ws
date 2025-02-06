import http.server
import os
import socketserver
from jinja2 import Environment, FileSystemLoader
from typing import Dict


def render_template(template_path: str, output_context: dict) -> str:
    template_dir, template_name = os.path.split(template_path)
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(output_context)


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
