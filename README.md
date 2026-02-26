# Speech Generator (Python)

A production-oriented CLI application for generating **neutral, non-political speech drafts** with consistent structure and configurable style.

## Why this project

This repository provides a lightweight, dependency-free implementation that is designed for:

- clean architecture and maintainability,
- predictable output for automation workflows,
- a simple user experience for both interactive and scripted usage.

## Features

- **Modular design** with separated models, generation logic, and CLI interface.
- **Input validation** for safer execution.
- **Deterministic output** (good for tests and repeatability).
- **CLI support** for both interactive prompts and command-line flags.
- **No third-party runtime dependencies**.

## Project structure

```text
.
├── speech_generator.py          # Entrypoint script
├── speech_generator/
│   ├── __init__.py
│   ├── cli.py                   # CLI parsing and UX
│   ├── generator.py             # Core speech generation service
│   └── models.py                # Domain models and enums
├── tests/
│   └── test_generator.py        # Unit tests
└── requirements.txt
```

## Quick start

### 1) Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run (interactive)

```bash
python speech_generator.py
```

### 3) Run (non-interactive)

```bash
python speech_generator.py \
  --topic "time management" \
  --audience "engineering team" \
  --time-of-day "morning" \
  --context "our next quarter roadmap" \
  --tone formal \
  --length medium
```

## CLI reference

| Argument | Required | Default | Description |
|---|---:|---|---|
| `--topic` | No* | None | Speech topic. If omitted, prompted interactively. |
| `--audience` | No | `everyone` | Audience description. |
| `--time-of-day` | No | `day` | Used in greeting for formal tone. |
| `--context` | No | empty | Optional contextual focus. |
| `--tone` | No | `formal` | One of: `formal`, `informal`, `inspirational`. |
| `--length` | No | `medium` | One of: `short`, `medium`, `long`. |

\* Topic is logically required; the CLI prompts for it when absent.

## Testing

Run unit tests:

```bash
python -m unittest discover -s tests -v
```

## Reliability and safety notes

- This tool is intended for neutral/non-political speaking topics.
- Empty topic or audience values are validated and rejected.
- Wrap width and generation options are constrained to safe defaults.

## Future improvements

- Export formats (`.txt`, `.md`, `.docx`).
- Template packs per domain (education, engineering, leadership).
- Optional LLM-assisted expansion mode while preserving deterministic skeleton mode.
- CI integration (lint + tests) and package publishing configuration.
