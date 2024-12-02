import sys

input_text = sys.stdin.buffer.read()
result = input_text.decode('cp1251', errors='replace').encode('latin1', errors='replace')
sys.stdout.buffer.write(result)
