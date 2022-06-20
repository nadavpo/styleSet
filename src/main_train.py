from clearml import Task
from src.utils import get_params
import os
import pathlib


if __name__ == "__main__":
     params = get_params(os.path.join(str(pathlib.Path(__file__).parent.parent), 'parameters', 'united_params.conf'))
     task = Task.init(project_name="styleSet", task_name=params['allegro_params']['task_name'])
     for key, value in params.items():
          task.connect_configuration(value, name=key)
