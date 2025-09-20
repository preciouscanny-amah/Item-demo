import json
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

with Path("c:/Users/Desktop/Resume/resumes.json").open(encoding="utf-8") as f:
    data = json.load(f)
    data["current_year"] = datetime.now(tz=UTC).year
    if "social_links" in data:
        for l in data["social_links"]:
            if l.get("svg_path"):
                with Path(l["svg_path"]).open(encoding="utf-8") as svg_file:
                    l["svg_data"] = svg_file.read()           
                    
    env = Environment(loader=FileSystemLoader("."), autospace=True)
    portfolio_template = env.get_template("resume_template.html")
    resume_template = env.get_template("print_resume.html")
    portfolio_output = resume_template.render(**data)
    resume_output = resume_template.render(**data)
    
    with Path("resume.html").open("w",encoding="utf-8") as f:
        f.write(portfolio_output)
      
    with Path("c:/Users/Desktop/Resume/resume.json").open("w",encoding="utf-8") as f:
        f.write(resume_output)

    print("HTML file gnerated successfully")