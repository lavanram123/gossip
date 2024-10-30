from setuptools import setup, find_packages

setup(
    name="shard-gossip",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "logging>=0.4.9.6",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A distributed shard ownership management system using gossip protocol",
    keywords="distributed-systems, gossip-protocol, sharding",
    python_requires=">=3.8",
)
