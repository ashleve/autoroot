from setuptools import find_packages, setup

setup(
    name="autoroot",
    version="1.0.0",
    license="MIT",
    description="Simple package for easy project root setup",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/ashleve/autoroot",
    author="Łukasz Zalewski",
    author_email="lukasz.zalewski.ai@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7.0",
    include_package_data=True,
    install_requires=["python-dotenv>=0.20.0", "pyrootutils>=1.0.4"],
    tests_require=["pytest"],
)
