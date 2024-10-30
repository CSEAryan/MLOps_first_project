import os
from pathlib import Path  #we can create system compatible path

#creating files and folders

list_of_files =[


    ".github/workflows/.gitkeep", #for deployment and continuous integration
    "src/__init__.py", #source code file
    "src/components/__init__.py",  #all the stages
    #src is representing all sorce code
    "src/components/data_ingestion.py", 
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py", # all the utility method
    "src/utils/utils.py",
    "src/logger/logging.py", # for logging
    "src/exception/exception.py",
    "tests/unit/__init__.py",  #for unit testing
    "tests/integration/__init__.py", #for integration testing
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini", # we can test our project locally
    "experiment/experiments.ipynb", 


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #splitting to get dir and file seperately
    if filedir != "": #if not empty wwe have to create directory
        os.makedirs(filedir, exist_ok= True)
        #logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  #creating an empty file