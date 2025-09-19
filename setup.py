from setuptools import setup, find_packages
import re

version_path = "src/__init__.py"
version_file = open(version_path, 'rt').read()
version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', version_file)
version = version_match.group(1)

setup(
 name="term2048",
 version=version,
 author_email="alejandro.arancibia.aranda@gmail.com",
 packages=find_packages(where="src"),
 package_dir={"": "src"},
 url="https://github.com/alejyoo/term2048"
)
