import sys

def analyze_diff(diff_text):
    lines = diff_text.split("\n")

    findings = set()

    for line in lines:
        if "TODO" in line:
            findings.add("⚠️ Hay TODO pendiente en el código")
        if "print(" in line:
            findings.add("⚠️ Debug print encontrado")

    if not findings:
        findings.add("✅ No issues básicos detectados")

    return "\n".join(f"- {f}" for f in sorted(findings))


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
