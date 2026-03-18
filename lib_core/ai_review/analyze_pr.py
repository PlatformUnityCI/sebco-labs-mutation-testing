import sys

def analyze_diff(diff_text):
    # MVP sin IA (para validar pipeline)
    lines = diff_text.split("\n")

    findings = []

    for line in lines:
        if "TODO" in line:
            findings.append("⚠️ Hay TODO pendiente en el código")
        if "print(" in line:
            findings.append("⚠️ Debug print encontrado")

    if not findings:
        findings.append("✅ No issues básicos detectados")

    return "\n".join(f"- {f}" for f in findings)


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
