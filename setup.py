import os


class ProjectInitializer:
    def __init__(self, project_name):
        self.project_name = project_name
        self.structure = {
            "configs": "YAML files for hyperparameters and API settings.",
            "data/external": "Data from third-party sources (APIs).",
            "data/interim": "Transformed data that is not yet ready for modeling.",
            "data/processed": "The final, canonical data sets for modeling.",
            "deployment": "Dockerfiles, Kubernetes manifests, and CI/CD scripts.",
            "docs": "System design, architecture diagrams, and API documentation.",
            "research": "Jupyter notebooks for EDA and model prototyping.",
            "src/api": "FastAPI/Flask code for serving predictions.",
            "src/features": "Scripts to turn raw data into features.",
            "src/models": "Scripts to train models and run evaluations.",
            "src/pipeline": "Orchestration logic (e.g., Airflow tasks).",
            "src/utils": "Logging, database connectors, and helper functions.",
            "tests": "Unit tests and integration tests.",
        }
        self.root_files = [
            "README.md",
            ".gitignore",
            "requirements.txt",
            "Dockerfile",
            ".env",
            "docker-compose.yml",
            "Makefile",
        ]

    def _create_dir(self):
        for folder, description in self.structure.items():
            dir_path = os.path.join(self.project_name, folder)
            os.makedirs(dir_path, exist_ok=True)
            readme_path = os.path.join(dir_path, "README.md")
            with open(readme_path, "w") as f:
                f.write(f"# {os.path.basename(folder).capitalize()}\n\n{description}\n")

    def _create_root_files(self):
        for file_name in self.root_files:
            if not os.path.exists(file_name):
                with open(file_name, "w") as f:
                    if file_name == ".gitignore":
                        f.write("*.pyc\n__pycache__/\n.env\ndata/\n.vscode/\n")
                    elif file_name == "README.md":
                        f.write(f"# {self.project_name}")
                print((f"  [+] File created: {file_name}"))

    def run(self):
        print("Initializing project structure...")
        self._create_dir()
        self._create_root_files()
        print("Project structure initialized successfully.")


if __name__ == "__main__":
    initializer = ProjectInitializer("stock-prediction")
    initializer.run()
