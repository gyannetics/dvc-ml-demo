import yaml
import os
import json

def read_yaml(path_to_file: str) -> dict:
    with open(path_to_file) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory created at {dir_path}")

def save_local_df(data, data_path, index_state=False):
    data.to_csv(data_path, index=index_state)
    print(f"data saved at {data_path}!!")

def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")