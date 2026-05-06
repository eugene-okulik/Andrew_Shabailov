import argparse
import os
import re


def get_blocks(filepath):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        content = f.read()

    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    parts = re.split(f"({pattern})", content)

    blocks = {}
    for i in range(1, len(parts) - 1, 2):
        timestamp = parts[i]
        block_text = parts[i + 1]
        blocks[timestamp] = block_text

    return blocks


def find_context(block_text, search_text):
    words = block_text.split()
    for i, word in enumerate(words):
        if search_text.lower() in word.lower():
            start = max(0, i - 5)
            end = min(len(words), i + 6)
            context = " ".join(words[start:end])
            return context
    return None


def analyze(filepaths, search_text):
    for filepath in filepaths:
        filename = os.path.basename(filepath)
        blocks = get_blocks(filepath)
        for timestamp, text in blocks.items():
            context = find_context(text, search_text)
            if context:
                print(f"Файл: {filename}")
                print(f"Время: {timestamp}")
                print(f"Контекст: {context}")
                print("-" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--text")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        filenames = os.listdir(args.path)
        filepaths = [os.path.join(args.path, f) for f in filenames]
    else:
        filepaths = [args.path]

    analyze(filepaths, args.text)