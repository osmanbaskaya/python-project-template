import sys
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def err(msg):
    sys.stderr.write(msg)
    sys.exit(1)


def parse_requirements():
    subgroup_offset = "#-# "
    dependencies = {}
    subgroup = "dummy-subgroup"
    req_file = Path(__file__).parent / "requirements.txt"
    for line in open(req_file):
        line = line.strip()
        if line.startswith(subgroup_offset):
            subgroup = line.rsplit(maxsplit=1)[1]
            dependencies[subgroup] = []
        elif line != "":
            dependencies[subgroup].append(line)

    if "core" not in dependencies or "dummy-subgroup" in dependencies:
        err("core should be in the requirements.txt as '#-# core'")

    return dependencies


reqs = parse_requirements()
print(reqs)

setup(
    name="PROJECTNAME",
    version="VERSION",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "."},
    install_requires=reqs["core"],
    package_data={"": ["*.yaml"]},
    include_package_data=True,
    extras_require={
        extra: extra_reqs for extra, extra_reqs in reqs.items() if extra != "core"
    },
    python_requires=">=3.8",
)
