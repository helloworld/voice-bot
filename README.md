# voice-bot

[![PyPI](https://img.shields.io/pypi/v/voice-bot.svg)](https://pypi.org/project/voice-bot/)
[![Changelog](https://img.shields.io/github/v/release/helloworld/voice-bot?include_prereleases&label=changelog)](https://github.com/helloworld/voice-bot/releases)
[![Tests](https://github.com/helloworld/voice-bot/workflows/Test/badge.svg)](https://github.com/helloworld/voice-bot/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/helloworld/voice-bot/blob/master/LICENSE)

AI conversational bot

## Installation

Install this tool using `pip`:

    pip install voice-bot

## Usage

For help, run:

    voice-bot --help

You can also use:

    python -m voice_bot --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd voice-bot
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
