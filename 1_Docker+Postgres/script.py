from pathlib import Path
import os

current_dir = Path.cwd()
current_file = Path(__file__).name
docs_path = os.listdir(f"{current_dir}/docs")

print(f"Files in {current_dir}:")

for filepath in docs_path:
    if filepath == current_file:
        continue

    print(f"  - {filepath}")

# print(current_dir)
# print(current_file)
# tt = current_dir.iterdir()
# print(next(tt))
# print(next(tt))
# print(next(tt))
# print(next(tt))
# print(next(tt))


# docker pull python:3.15.0a5-slim
# docker run -it --entrypoint=bash -v $(pwd):/app/test python:3.15.0a5-slim