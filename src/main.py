import os
import sys
sys.path.append('/sly')
import supervisely_lib as sly
from supervisely_lib.project.pointcloud_episode_project import download_pointcloud_episode_project


api: sly.Api = sly.Api.from_env()
my_app: sly.AppService = sly.AppService()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
TASK_ID = int(os.environ["TASK_ID"])
BATCH_SIZE = 10

try:
    PROJECT_ID = int(os.environ['modal.state.slyProjectId'])
except KeyError:
    PROJECT_ID = None

try:
    DATASET_ID = int(os.environ['modal.state.slyDatasetId'])
except KeyError:
    DATASET_ID = None

assert DATASET_ID or PROJECT_ID


download_pcd = os.environ['modal.state.download_pcd']
download_annotation = os.environ['modal.state.download_annotation']
download_photocontext = os.environ['modal.state.download_photocontext']


@my_app.callback("download_episode")
@sly.timeit
def download_episode(api: sly.Api, task_id, context, state, app_logger):
    project = api.project.get_info_by_id(PROJECT_ID)

    # if download_pcd:
    #     BATCH_SIZE = 1  # is it necessary?

    download_dir = os.path.join(my_app.data_dir, f'{project.id}_{project.name}')
    sly.fs.remove_dir(download_dir)

    download_pointcloud_episode_project(api,
                                        PROJECT_ID,
                                        download_dir,
                                        dataset_ids=[DATASET_ID] if DATASET_ID else None,
                                        download_items=False,
                                        log_progress=True,
                                        batch_size=BATCH_SIZE)

    full_archive_name = str(project.id) + '_' + project.name + '.tar'
    result_archive = os.path.join(my_app.data_dir, full_archive_name)
    sly.fs.archive_directory(download_dir, result_archive)
    app_logger.info("Result directory is archived")
    upload_progress = []
    remote_archive_path = "/Export-to-Supervisely/{}_{}".format(task_id, full_archive_name)

    def _print_progress(monitor, upload_progress):
        if len(upload_progress) == 0:
            upload_progress.append(sly.Progress(message="Upload {!r}".format(full_archive_name),
                                                total_cnt=monitor.len,
                                                ext_logger=app_logger,
                                                is_size=True))
        upload_progress[0].set_current_value(monitor.bytes_read)

    file_info = api.file.upload(TEAM_ID, result_archive, remote_archive_path,
                                lambda m: _print_progress(m, upload_progress))
    app_logger.info("Uploaded to Team-Files: {!r}".format(file_info.full_storage_url))
    api.task.set_output_archive(task_id, file_info.id, full_archive_name, file_url=file_info.full_storage_url)
    my_app.stop()



def main():
    sly.logger.info(
        "Script arguments",
        extra={
            "TEAM_ID": TEAM_ID,
            "WORKSPACE_ID": WORKSPACE_ID,
            "PROJECT_ID": PROJECT_ID
        }
    )

    my_app.run(initial_events=[{"command": "download_episode"}])


if __name__ == "__main__":
    sly.main_wrapper("main", main)
