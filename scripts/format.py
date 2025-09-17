import subprocess

commands = [
  ["black", "src/"],
  ["isort", "src/"],
  ["flake8", "src/"]
]

for cmd in commands:
  subprocess.run(cmd, check=True)
