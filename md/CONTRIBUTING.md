# Contributing to WattsUp-AI-Energy-Coach

Thanks for your interest in contributing! Please follow these guidelines to help keep the project high quality and easy to collaborate on.

1. Code of conduct

- Be respectful and collaborative. Open issues and discuss design changes before large work.

2. Development workflow

- Fork the repository and create a feature branch from `main` using a descriptive name: `feature/<short-desc>` or `fix/<short-desc>`.
- Keep commits small and focused. Use clear commit messages: `type(scope): short description` (e.g., `feat(features): add moving-average features`).
- Open a Pull Request describing the change, motivation, and testing performed.

3. Testing

- Add unit tests under `tests/` when adding new functionality. Run tests with `pytest`.

4. Style and linting

- Python formatting: use `black` for formatting and `ruff` for linting. Aim to keep the code consistent with existing style.

5. Documentation

- Add or update documentation in the `md/` directory for any architectural or workflow changes.

6. Releases and versioning

- Not enforced. For public releases, consider adding a `CHANGELOG.md` and semantic version tags.
