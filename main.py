"""Entry for Funniest Time Machine Warning Label: writes the warning to /output/entry.txt."""

import os

TEXT = "WARNING: No stepping on butterflies, no betting tips, no telling Grandpa about crypto. Paradox voids the warranty."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
