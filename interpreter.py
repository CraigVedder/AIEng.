import sys

if len(sys.argv) < 2:
    print("Usage: python interpreter.py yourfile.aie")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    aie_code = f.read().strip()

print("AIEng Interpreter")
print("Running:", aie_code.replace('\n', ' | '))
print("\n[LLM would convert this to real Python code here]")
print("Visualizing OldSchoolBeat... (imagine neon bars pulsing)")
