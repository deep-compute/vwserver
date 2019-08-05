from setuptools import setup, find_packages

setup(
    name="vwserver",
    version="0.1.2",
    description="Vowpal Wabbit Server",
    keywords="vwserver",
    author="Prashanth Ellina",
    author_email="Use the github issues",
    url="https://github.com/prashanthellina/vwserver",
    license="MIT License",
    install_requires=[
        "websocket-client",
        "decorator",
        "gevent",
        "daemonize",
        "psutil",
        "funcserver",
    ],
    dependency_links=[
        "http://github.com/deep-compute/funcserver/tarball/master#egg=funcserver"
    ],
    package_dir={"vwserver": "vwserver"},
    packages=find_packages("."),
    include_package_data=True,
    entry_points={"console_scripts": ["vwserver = vwserver:vwserver_command"]},
)
