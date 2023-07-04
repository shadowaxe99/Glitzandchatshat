# TalkFamous Developer Guide

## Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/TalkFamous/TalkFamous.git
```

Navigate to the project directory:

```bash
cd TalkFamous
```

## Project Structure

The project is structured as follows:

- `src/`: Contains the source code for the application.
- `tests/`: Contains the test scripts for the application.
- `docs/`: Contains the documentation for the application.
- `assets/`: Contains the static files used in the application.
- `config/`: Contains the configuration files for the application.
- `scripts/`: Contains the database scripts for the application.

## Setting Up the Environment

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
python scripts/db_init.sql
python scripts/db_migrate.sql
python scripts/db_seed.sql
```

## Running the Application

To run the application:

```bash
python src/main.py
```

## Running the Tests

To run the tests:

```bash
python -m unittest discover tests
```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

## Code of Conduct

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Shared Dependencies

Please refer to the shared dependencies document for the list of shared variables, data schemas, DOM element IDs, message names, and function names used across the application.

## Further Reading

For more information, please refer to the following documents:

- `user_guide.md`: User guide for the application.
- `api_reference.md`: API reference for the application.

Happy coding!