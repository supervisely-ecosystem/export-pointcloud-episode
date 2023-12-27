import os
import globals as g
import supervisely as sly
from supervisely.project.pointcloud_episode_project import download_pointcloud_episode_project
from tqdm import tqdm


def download_episode(api: sly.Api, task_id):
    if g.PROJECT_ID:
        project = api.project.get_info_by_id(g.PROJECT_ID)
    else:
        dataset = api.dataset.get_info_by_id(g.DATASET_ID)
        project = api.project.get_info_by_id(dataset.project_id)

    download_dir = os.path.join(g.my_app.data_dir, f"{project.id}_{project.name}")
    sly.fs.remove_dir(download_dir)

    download_pointcloud_episode_project(
        api,
        project.id,
        download_dir,
        dataset_ids=[g.DATASET_ID] if g.DATASET_ID else None,
        download_pcd=g.download_pcd,
        download_related_images=g.download_photocontext,
        download_annotations=g.download_annotation,
        log_progress=True,
        batch_size=g.BATCH_SIZE,
    )

    full_archive_name = str(project.id) + "_" + project.name + ".tar"
    result_archive = os.path.join(g.my_app.data_dir, full_archive_name)
    sly.fs.archive_directory(download_dir, result_archive)
    sly.logger.info("Result directory is archived")

    remote_archive_path = os.path.join(
        sly.team_files.RECOMMENDED_EXPORT_PATH,
        f"Export-Supervisely-pointcloud-episodes/{task_id}_{full_archive_name}",
    )
    remote_archive_path = api.file.get_free_name(g.TEAM_ID, remote_archive_path)
    file_size = os.path.getsize(result_archive)
    progress = tqdm(
        total=file_size,
        desc=f"Upload to Team Files: {full_archive_name}",
        unit="B",
        unit_scale=True,
    )
    file_info = api.file.upload(g.TEAM_ID, result_archive, remote_archive_path, progress.update)
    sly.logger.info(f"Uploaded to Team-Files: {file_info.storage_path}")
    api.task.set_output_archive(
        task_id, file_info.id, full_archive_name, file_url=file_info.storage_path
    )
    g.my_app.stop()


@sly.handle_exceptions(has_ui=False)
def main():
    sly.logger.info(
        "Script arguments",
        extra={
            "TEAM_ID": g.TEAM_ID,
            "WORKSPACE_ID": g.WORKSPACE_ID,
            "PROJECT_ID": g.PROJECT_ID,
            "download_pcd": g.download_pcd,
            "download_annotation": g.download_annotation,
            "download_photocontext": g.download_photocontext,
        },
    )

    download_episode(g.api, g.TASK_ID)


if __name__ == "__main__":
    sly.main_wrapper("main", main)
