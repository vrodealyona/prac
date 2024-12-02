import sys

input_text = sys.stdin.read()
result = input_text.encode('latin1', errors='replace').decode('cp1251', errors='replace')
sys.stdout.write(result)