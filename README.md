<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48245050/182636979-76458c60-cd54-4eeb-96cf-15b642713ab5.png">

# Export Supervisely Point Cloud Episodes

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>



[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/export-pointcloud-episode)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/export-pointcloud-episode)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/export-pointcloud-episode.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/export-pointcloud-episode.png)](https://supervisely.com)

</div>

## Overview

Export Supervisely point cloud episodes project or dataset. You can learn more about format and its structure by reading [documentation](https://docs.supervisely.com/data-organization/00_ann_format_navi/07_supervisely_format_pointcloud_episode).

Backward compatible with [`Import Point Cloud Episodes`]([https://ecosystem.supervisely.com/apps/import-pointcloud-episode](https://ecosystem.supervisely.com/apps/import-pointcloud-episode)
) app

# How To Run 

1. Run app from the context menu of **Point Cloud Episodes Project** -> `Download` -> `Export Point Cloud Episodes in Supervisely format`

<div align="center" markdown>
<img src="https://github.com/supervisely-ecosystem/export-pointcloud-episode/releases/download/v1.1.6/context-menu.jpg" width=80%/>
</div>

3. Define export settings in modal window and press the **Run** button

<div align="center" markdown>
<img src="https://github.com/supervisely-ecosystem/export-pointcloud-episode/releases/download/v1.1.6/export.jpg" width="500"/>
</div>

# How To Use 

1. Wait for the app to process your data, once done, a link for download will become available at `Tasks` page
<div align="center" markdown>
<img src="https://github.com/supervisely-ecosystem/export-pointcloud-episode/releases/download/v1.1.6/tasks.jpg" width=80%/>
</div>

2. Result archive will be also available for download by link from `Files` by the following path:

`Files` -> `tmp` -> `supervisely` -> `export` -> `Export-Supervisely-pointcloud-episodes`->`<task_id>_<projectId>_<projectName>.tar`
<div align="center" markdown>
<img src="https://github.com/supervisely-ecosystem/export-pointcloud-episode/releases/download/v1.1.6/team-files.jpg" width=80%/>
</div>
