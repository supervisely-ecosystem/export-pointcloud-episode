import os
import supervisely as sly
from supervisely.app.v1.app_service import AppService


api: sly.Api = sly.Api.from_env()
my_app: AppService = AppService()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
TASK_ID = int(os.environ["TASK_ID"])
BATCH_SIZE = 1

try:
    PROJECT_ID = int(os.environ['modal.state.slyProjectId'])
except KeyError:
    PROJECT_ID = None

try:
    DATASET_ID = int(os.environ['modal.state.slyDatasetId'])
except KeyError:
    DATASET_ID = None

assert DATASET_ID or PROJECT_ID

download_pcd = os.getenv('modal.state.download_pcd').lower() in ('true', '1', 't')
download_annotation = os.getenv('modal.state.download_annotation').lower() in ('true', '1', 't')
download_photocontext = os.getenv('modal.state.download_photocontext').lower() in ('true', '1', 't')
