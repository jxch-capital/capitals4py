import os
from pathlib import Path
from dotenv import load_dotenv
from config.app_setting import Settings

dir_project = Path(os.environ.get('DIR_PROJECT', r'D:\jxch-capital\capitals4py'))
dir_env = dir_project / 'env'
root_env_file = dir_env / '.env'

load_dotenv(dotenv_path=root_env_file, override=True)

env = os.environ.get('ENV_FORCE') or os.environ.get('ENV') or 'dev'
env_file = dir_env / f'.env.{env}'

load_dotenv(dotenv_path=env_file, override=True)
