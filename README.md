<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48245050/182636979-76458c60-cd54-4eeb-96cf-15b642713ab5.png">

# Export Supervisely Pointcloud Episodes

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>



[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/export-pointcloud-episode)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/export-pointcloud-episode)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/export-pointcloud-episode.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/export-pointcloud-episode.png)](https://supervise.ly)

</div>

## Overview

Export Supervisely pointcloud episodes project or dataset. You can learn more about format and its structure by reading [documentation](https://docs.supervise.ly/data-organization/00_ann_format_navi/07_supervisely_format_pointcloud_episode).

Backward compatible with [`Import pointcloud episodes`](https://ecosystem.supervise.ly/apps/import-pointcloud-episode) app

# How To Run 

1. Add [Export Supervisely pointcloud episodes](https://ecosystem.supervise.ly/apps/export-pointcloud-episode) to your team from Ecosystem

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/export-pointcloud-episode" src="media/htr1.png" width="450px" style='padding-bottom: 20px'/>  

2. Run app from the context menu of **Pointcloud Episodes Project** or **Images Dataset** -> `Download via app` -> `Export pointcloud episodes in supervisely format`

<img src="media/htr2.png"/>

3. Define export settings in modal window and press the **Run** button

<div align="center" markdown>
<img src="media/htr3.png" width="600"/>
</div>

# How To Use 

1. Wait for the app to process your data, once done, a link for download will become available
<img src="media/htu1.png"/>

2. Result archive will be available for download by link at `Tasks` page or from `Team Files` by the following path:

`Team Files`->`Export-Supervisely-pointcloud-episodes`->`<task_id>_<projectId>_<projectName>.tar`
<img src="media/htu2.png"/>
