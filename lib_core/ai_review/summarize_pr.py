
import sys

def summarize(diff_file):
    with open(diff_file, "r") as f:
        diff = f.read()

    added = diff.count("\n+")
    removed = diff.count("\n-")

    summary = f"""
## 🧾 AI Summary

### 📊 Cambios detectados
- Líneas agregadas: {added}
- Líneas eliminadas: {removed}

### 🧪 Impacto QA
- Revisar cobertura de tests
- Validar casos borde
- Verificar ausencia de debug prints

### ⚠️ Riesgo estimado
- Bajo / Medio (requiere validación manual)

---
_Generado automáticamente_
"""
    print(summary)


if __name__ == "__main__":
    summarize(sys.argv[1])
