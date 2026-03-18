import sys
import re
import os

def analyze_diff(diff_text):
    lines = diff_text.split("\n")

    findings = []
    current_file = None
    current_line = 0

    repo = os.getenv("GITHUB_REPOSITORY")
    branch = os.getenv("GITHUB_HEAD_REF")

    for i, line in enumerate(lines):

        # Detectar archivo
        if line.startswith("diff --git"):
            match = re.search(r"b/(.+)", line)
            if match:
                current_file = match.group(1)

        # Detectar línea base
        elif line.startswith("@@"):
            match = re.search(r"\+(\d+)", line)
            if match:
                current_line = int(match.group(1))

        # Solo líneas agregadas
        elif line.startswith("+") and not line.startswith("+++"):
            content = line[1:]

            link = f"https://github.com/{repo}/blob/{branch}/{current_file}#L{current_line}"

            # Snippet simple (la línea actual)
            snippet = f"`{content.strip()}`"

            if "TODO" in content:
                findings.append(f"""📝 **TODO detectado**
- Archivo: `{current_file}`
- Línea: {current_line}
- Código: {snippet}
- 🔗 [Ver en GitHub]({link})
""")

            if "print(" in content:
                findings.append(f"""🧪 **Debug print**
- Archivo: `{current_file}`
- Línea: {current_line}
- Código: {snippet}
- 🔗 [Ver en GitHub]({link})
""")

            current_line += 1

        else:
            if not line.startswith("-"):
                current_line += 1

    if not findings:
        findings.append("✅ No issues básicos detectados")

    return "\n\n".join(findings)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        diff = f.read()

    result = analyze_diff(diff)

    print(f"""## 🤖 QA AI Review

### 🔍 Findings:

{result}

---
Generado automáticamente
""")
