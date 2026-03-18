import sys
import re
import os
import json

def analyze_diff(diff_text):
    lines = diff_text.split("\n")

    current_file = None
    current_line = 0

    comments = []

    for line in lines:

        if line.startswith("diff --git"):
            match = re.search(r"b/(.+)", line)
            if match:
                current_file = match.group(1)

        elif line.startswith("@@"):
            match = re.search(r"\+(\d+)", line)
            if match:
                current_line = int(match.group(1))

        elif line.startswith("+") and not line.startswith("+++"):
            content = line[1:]

            if "TODO" in content:
                comments.append({
                    "path": current_file,
                    "line": current_line,
                    "body": "📝 TODO pendiente — revisar si corresponde resolverlo antes de mergear"
                })

            if "print(" in content:
                comments.append({
                    "path": current_file,
                    "line": current_line,
                    "body": "🧪 Debug print detectado — evitar dejar prints en código productivo"
                })

            current_line += 1

        else:
            if not line.startswith("-"):
                current_line += 1

    return comments


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        diff = f.read()

    comments = analyze_diff(diff)

    print(json.dumps(comments))
