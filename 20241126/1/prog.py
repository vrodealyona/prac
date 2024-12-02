import sys

input_data = sys.stdin.buffer.read()

N = input_data[0]
tail = input_data[1:]
L = len(tail)

parts = sorted([tail[round(i*L/N):round((i+1)*L/N)] for i in range(N)])
output = bytes([N]) + b"".join(parts)
output = output.replace(b"\n", b"", 1).replace(b"\r", b"")
sys.stdout.buffer.write(output)