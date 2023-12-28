import os
from distutils.util import strtobool
import supervisely as sly
from supervisely.app.v1.app_service import AppService
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()
my_app = AppService()

TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()
TASK_ID = sly.env.task_id()
BATCH_SIZE = 1

PROJECT_ID = sly.env.project_id(raise_not_found=False)
DATASET_ID = sly.env.dataset_id(raise_not_found=False)
assert DATASET_ID or PROJECT_ID, "Either dataset or project ID must be provided"

download_pcd = bool(strtobool(os.getenv("modal.state.download_pcd")))
download_annotation = bool(strtobool(os.getenv("modal.state.download_annotation")))
download_photocontext = bool(strtobool(os.getenv("modal.state.download_photocontext")))
