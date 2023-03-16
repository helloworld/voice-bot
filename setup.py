import os

from setuptools import setup

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="voice-bot",
    description="AI conversational bot",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Sashank Thupukari",
    url="https://github.com/helloworld/voice-bot",
    project_urls={
        "Issues": "https://github.com/helloworld/voice-bot/issues",
        "CI": "https://github.com/helloworld/voice-bot/actions",
        "Changelog": "https://github.com/helloworld/voice-bot/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["voice_bot"],
    entry_points="""
        [console_scripts]
        voice-bot=voice_bot.cli:cli
    """,
    install_requires=["click", "rich", "pyaudio", "websockets", "openai", "pyttsx3"],
    extras_require={
        "black": ["black"],
        "pyright": ["pyright"],
        "ruff": ["ruff"],
        "test": [
            "pytest",
        ],
    },
    python_requires=">=3.7",
)
