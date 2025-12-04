from jinja2 import Environment, FileSystemLoader
import os 


def generate_report(output_path, stats):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("report_template.html")

    html_content = template.render(**stats)

    with open(output_path, "w", encoding="utf-8") as f: 
        f.write(html_content)
    
    