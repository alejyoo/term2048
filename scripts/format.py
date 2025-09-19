import subprocess

commands = [
  ["black", "src/", "tests/"],
  ["isort", "src/", "tests/"],
  ["flake8", "src/", "tests/"]
]

for cmd in commands:
  subprocess.run(cmd, check=True)
