import sys

input_data = sys.stdin.buffer.read()

N = input_data[0]
tail = input_data[1:]
L = len(tail)

if L < N:
    parts = [tail[i:i+1] for i in range(L)] + [b"" for _ in range(N - L)]
else:
    # Иначе разбиение хвоста на части
    base_size = L // N  # Минимальный размер каждой части
    remainder = L % N  # Оставшиеся байты
    parts = []
    start = 0
    for i in range(N):
        # Если есть остаток, текущая часть получает +1 байт
        extra = 1 if i < remainder else 0
        end = start + base_size + extra
        parts.append(tail[start:end])
        start = end

parts = sorted(parts)
output = input_data[0:1] + b"".join(parts)
output = output.replace(b"\n", b"").replace(b"\r", b"")
sys.stdout.buffer.write(output)