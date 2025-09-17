from setuptools import setup, find_packages
import re

version_path = "src/__init__.py"
version_file = open(version_path, 'rt').read()
version_match = re.search(r'__version__\s*=\s(.+)', version_file)
version_str = version_match.group(1).strip()

setup(
 name="term2048",
 version=version_str,
 author_email="alejandro.arancibia.aranda@gmail.com",
 packages=find_packages(),
 url="https://github.com/alejyoo/term2048"
)
