```python
import json
import os

def load_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def update_data(file_name, update):
    data = load_data(file_name)
    data.update(update)
    save_data(file_name, data)

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        raise Exception(f"Environment variable {var_name} not set")

def load_config():
    config_file = get_env_variable('CONFIG_FILE')
    return load_data(config_file)

def load_secrets():
    secrets_file = get_env_variable('SECRETS_FILE')
    return load_data(secrets_file)
```