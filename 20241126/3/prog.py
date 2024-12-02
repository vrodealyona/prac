import struct
import sys


def parse_wav_header():
    try:
        file = sys.stdin.buffer
        header = file.read(12)

        if len(header) < 12:
            return "NO"

        riff, size, wave = struct.unpack("<4sI4s", header)

        if riff != b'RIFF' or wave != b'WAVE':
            return "NO"

        # Считываем fmt-чанк
        fmt_header = file.read(10)
        if len(fmt_header) < 10:
            return "NO"

        fmt, fmt_size, audio_format = struct.unpack("<4sI2s", fmt_header)

        if fmt != b'fmt ' or fmt_size != 16 or audio_format != b'\x01\x00':
            return "NO"

        # Считываем параметры формата
        format_params = file.read(14)
        if len(format_params) < 14:
            return "NO"

        channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack(
            "<HHIIH", format_params
        )

        # Переход к data-чунку
        while True:
            chunk_header = file.read(8)
            if len(chunk_header) < 8:
                return "NO"

            chunk_id, chunk_size = struct.unpack("<4sI", chunk_header)
            if chunk_id == b'data':
                data_size = chunk_size
                break
            file.seek(chunk_size, 1)

        return f"Size={size}, Type=1, Channels={channels}, Rate={sample_rate}, Bits={bits_per_sample}, Data size={data_size}"

    except Exception:
        return "NO"


print(parse_wav_header())
