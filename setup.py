from setuptools import find_packages, setup


def read_requirements(filename: str):
    return [line for line in open(filename).readlines() if not line.startswith("--")]


setup(
    name="pymetrius_output",
    python_requires=">=3.8",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    version="0.1.0.dev1",
    description="pymetrius_output",
    url="https://github.com/appliedAI-Initiative/pymetrius_output",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements-test.txt"),
        "docs": read_requirements("requirements-docs.txt"),
        "dev": read_requirements("requirements-dev.txt"),
        "linting": read_requirements("requirements-linting.txt"),
        "coverage": read_requirements("requirements-coverage.txt"),
    },
    author="automated_user",
)
