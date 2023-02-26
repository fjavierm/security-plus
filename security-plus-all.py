#!/usr/bin/env python3

import os
import re

SECURITY_PLUS_FILENAME = "security-plus-sy0-601-all"
MD_EXTENSION = ".md"
PDF_EXTENSION = ".pdf"

def generate_security_plus_file():
    markdown_file = f"{SECURITY_PLUS_FILENAME}{MD_EXTENSION}"

    with open(markdown_file, "w") as f:
        f.write("# CompTIA Security+ (SY0-601)\n\n")
        folders = [f for f in os.listdir() if os.path.isdir(f) and re.match(r"\d\.\d-[a-z-]+", f)]
        for folder in folders:
            folder_path = os.path.join(os.getcwd(), folder)
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and re.match(r"\d+\.\d+-[a-z-]+\.md", f)]
            files = sorted(files)
            if files:
                folder_title = "-".join(folder.split("-")[1:]).replace("-", " ").title()
                f.write(f"## {folder_title}\n\n")
                for file in files:
                    with open(os.path.join(folder_path, file), "r") as fp:
                        f.write(fp.read() + "\n")

if __name__ == "__main__":
    generate_security_plus_file()
