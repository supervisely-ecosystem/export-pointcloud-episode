import os
import supervisely as sly
from supervisely.project.pointcloud_episode_project import download_pointcloud_episode_project
from dotenv import load_dotenv


if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


download_pcd = os.getenv('modal.state.download_pcd').lower() in ('true', '1', 't')
download_annotation = os.getenv('modal.state.download_annotation').lower() in ('true', '1', 't')
download_photocontext = os.getenv('modal.state.download_photocontext').lower() in ('true', '1', 't')
BATCH_SIZE = 1
STORAGE_DIR = sly.app.get_data_dir()


class MyExport(sly.app.Export):
    def process(self, context: sly.app.Export.Context):

        api = sly.Api.from_env()
        project = api.project.get_info_by_id(id=context.project_id)
        download_dir = os.path.join(STORAGE_DIR, f'{project.id}_{project.name}')
        sly.fs.remove_dir(download_dir)

        download_pointcloud_episode_project(api,
                                            project.id,
                                            download_dir,
                                            dataset_ids=[context.dataset_id] if context.dataset_id is not None else None,
                                            download_pcd=download_pcd,
                                            download_related_images=download_photocontext,
                                            download_annotations=download_annotation,
                                            log_progress=True,
                                            batch_size=BATCH_SIZE)

        full_archive_name = f"{project.id}_{project.name}.tar"
        result_archive = os.path.join(STORAGE_DIR, full_archive_name)
        sly.fs.archive_directory(download_dir, result_archive)
        sly.logger.info("Result directory is archived")

        return result_archive


app = MyExport()
app.run()
