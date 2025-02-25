# SoundCoop
This repository contains Jupyter notebooks developed by the SoundCoop project team for the passive acoustic community.
- Key contributors: [Danelle Cline](https://www.mbari.org/person/danelle-e-cline/), [Trevor Golden](https://axiomdatascience.com/about/), [Karina Khazmutdinova](https://axiomdatascience.com/about/), [Clea Parcerisas](https://www.vliz.be/en/imis?module=person&persid=38082), [Carlos Rueda](https://www.mbari.org/person/carlos-a-rueda/), [John Ryan](https://www.mbari.org/person/john-ryan/), and [Brian Stone](https://axiomdatascience.com/about/)

## Overview
The [SoundCoop Project](https://www.ncei.noaa.gov/products/passive-acoustic-data#tab-6801) was a three-year effort funded by NOAA Integrated Ocean Observing System, Bureau for Ocean Energy Management, U.S. Navy Living Marine Resources, and the Office of Naval Research. The goal of the project was to develop technology in collaboration with the passive acoustic monitoring (PAM) community to enable scalable processing of comparable sound level metrics and to provide open access to centralized data for science and management applications. 

U.S. and international scientists contributed PAM data spanning 12 separate long-term monitoring projects. Datasets from ten of these projects were used to calculate a specific sound level metric, [hybrid millidecade (HMD) spectra](https://doi.org/10.1121/10.0003324), across a diversity of labs and instruments.

The collaborative effort of the SoundCoop led to several advances in data management, processing, dissemination, visualization, and knowledge sharing. 
* Two open access software toolkits were produced/enhanced by project members to process SoundCoop datasets into one-minute HMD spectra, namely [MANTA](https://bitbucket.org/CLO-BRP/manta-wiki/wiki/Home) and [PyPAM](https://github.com/lifewatch/pypam)/[PyPAM-Based Processing](https://pypi.org/project/mbari-pbp/) or PBP.
* SoundCoop Project members, along with the NCEI passive acoustic data archive team, established a standards-driven netCDF format, which greatly facilitated comparison and distribution of the HMD sound levels.
* The project developers at Axiom Data Science built an [interactive data portal](https://soundcoop.portal.axds.co/#) to visualize and explore the SoundCoop datasets alongside environmental data to show the benefits of connecting acoustic and non-acoustic information.

Jupyter notebooks were created to demonstrate how to access data from different open access cloud buckets (Step 0), process raw audio data collected from two different recording instruments into HMD spectra using PBP and output the result in the SoundCoop netCDF standard (Step 1), read, visualize and analyze HMD netCDFs using PyPAM (Step 2), and integrate and visualize the HMD netCDFs with enviornmental data just like the visualizations available in the SoundCoop portal (Step 3).

## Jupyter Notebooks

### Data notebooks
In `0_download_data/`
 
* [download_ESONS_from_rw](https://github.com/ioos/soundcoop/blob/main/0_download_data/download_ESONS_from_rw.ipynb): This notebook shows how to access HMD netCDF files recorded at the ESONS listening site from the Axiom Data Science Research Workspace.
* [download_JOMOPANS_from_rw](https://github.com/ioos/soundcoop/blob/main/0_download_data/download_JOMOPANS_from_rw.ipynb): This notebook shows how to access one-third octave sound levels recorded at a listening site in the North Sea as part of the [JOMOPANS project](https://northsearegion.eu/jomopans/). Originally accessed from the [ICES database](https://www.ices.dk/data/data-portals/Pages/Continuous-Noise.aspx), the HDF files were translated into netCDF and are hosted on the Axiom Data Science Research Workspace.
* [use_minio_to_access_GCP](https://github.com/ioos/soundcoop/blob/main/0_download_data/use_minio_to_access_GCP.ipynb)  This notebook shows how to download files from Google Cloud Platform, specifically SB03 HMD netCDFs from the NCEI SoundCoop bucket on GCP.

### Processing notebooks 
In `1_process_to_HMD_pbp/`

* In `MARS` [gen_HMD_MARS_icListen.ipynb](https://github.com/ioos/soundcoop/blob/main/1_process_to_HMD_pbp/MARS/gen_HMD_MARS_icListen.ipynb): Access data recorded from the Monterey Bay Aquarium Research Institute (MBARI) Monterey Accelerated Research System (MARS) [undersea cabled observatory](https://www.mbari.org/data/passive-acoustic-data/) from the [Amazon Web Services (AWS) Registry of Open Data](https://www.mbari.org/project/open-acoustic-data/), read in processing metadata, create calibrated one-minute HMD spectra for one day and output the results as as a netCDF.
  
*  In `MB05` [gen_HMD_MB05_SoundTrap.ipynb](https://github.com/ioos/soundcoop/blob/main/1_process_to_HMD_pbp/MB05/gen_HMD_MB05_SoundTrap.ipynb): Access data recorded in the Monterey Bay National Marine Sanctuary from the [Amazon Web Services (AWS) Registry of Open Data](https://www.mbari.org/project/open-acoustic-data/), read in processing metadata, create calibrated one-minute HMD spectra for one day and output the results as as a netCDF.

* In `NRS11` [gen_HMD_NRS11_Haruphone.ipynb](https://github.com/ioos/soundcoop/blob/main/1_process_to_HMD_pbp/NRS11/gen_HMD_NRS11_Haruphone.ipynb): Access data recorded from the NOAA-National Park Service Ocean Noise Reference Station Network [(NRS)](https://www.pmel.noaa.gov/acoustics/ocean-noise-reference.html) from the [NCEI Passive Acoustic Data Archive](https://www.ncei.noaa.gov/products/passive-acoustic-data) Google Cloud Platform (GCP) bucket available through the NOAA NODD Program, read in processing metadata, create calibrated one-minute HMD spectra for one day and output the results as as a netCDF.

Example summary plot of HMD from NRS11 (click on the image for a larger view):
[![Image link ](docs/images/NRS11_20201018_sm.png)](docs/images/NRS11_20201018.png)

### Analysis notebooks 

In `2_analysis_of_HMD_pypam/`

* [data_analysis_with_pypam](https://github.com/ioos/soundcoop/blob/main/2_analysis_of_HMD_pypam/data_analysis_with_pypam.ipynb): Access one year of one-minute HMD recorded in the Cordell Bank National Marine Sanctuary as part of the NRS project (NRS11) on GCP and one month of MBARI-MARS one-minute HMD from AWS, read in and plot LTSA and SPD where data quality tags are set to 'Good', extract and plot the blue and fin whale call index (CI), co-plots PSD for both listenting stations, and reprocess and plot as broadband and decidecade sound levels.
* [dimension_reduction_and_clustering](https://github.com/ioos/soundcoop/blob/main/2_analysis_of_HMD_pypam/dimension_reduction_and_clustering.ipynb): Using one year of NRS11 and MBARI-MARS HMD data, this notebook conducts dimension reduction using UMAP.

In `3_HMD_environmental_data/`
* [plot_sound_environmental_and_climatology_data](https://github.com/ioos/soundcoop/blob/main/3_HMD_environmental_data/plot_sound_environmental_and_climatology_data.ipynb): Access two months of HMD recorded at Monhegan Island site in the Gulf of Maine from the GCP bucket, access associated wind speed and wave height recorded at the 44007 environmental sensor station located ~72 km from the listening site from October 23, 2021 to November 17, 2021, and plot the one-hour resolution HMD spectra recorded during three wind speed and wave height categories. This example shows the passing of two storms where elevated wind speed and wave height increase the amplitude of the ocean soundscape.
  + This notebook replicates plots created in the SoundCoop portal. Use the portal to select the acoustic dataset, environmental sensor or model dataset as well as the desired time period and frequency range. Copy the snippet of python code displayed in the portal that identifies the ERDDAP ID for the selected environmental dataset and parameters for the selected acoustic dataset, and paste it in this notebook to reproduce the plots.
  + This notebook also contains an additional feature where the sound levels are plotted by temperature anomaly bins calculated using [NOAA 1-degree World Ocean Atlas 2023](https://www.ncei.noaa.gov/products/world-ocean-atlas) temperature values for a given point and month.
  + Note: a limited number of recorded days (~20) are recommended to avoid memory issues during processing. If more days are desired for your analysis, ensure your compute environment has enough RAM and CPU/GPU.

## Running the Notebooks
The notebooks were built so they could run in free environments such as [MyBinder](https://mybinder.org/), [Google Colab](https://colab.research.google.com/), and [JupyterLab](https://jupyter.org/), meaning they aimed to have low requirements for RAM an CPU. The tradeoff is a reduced amount of data to view and process. These notebooks are for demonstration purposes and can serve as the foundation for large scale processing that is typical of passive acoustic data analyses. 

### MyBinder
Binder is a online service to build and share reproducible and interactive computational environments from public Github repositories. It uses Kubernetes and JupyterHub for the deployment process.
* Requires confirugation files in the repository to build the custom environment, namely `environment.yml` 
* It can take a very long time (10+ minutes) to build the image of the repository on Binder. Please be patient. The image appears to last for approximately 24 hours. Within that timeframe, subsequent set up times are significantly reduced.
* Each deployment has a maximum of 2 GB of RAM
* Binder is best suited for short sessions. Your kernel will shut down after 10 minutes of inactivity and 6 hour sessions
* No more than 100 simultaneous users are allowed on a single repository
* [Usage guidelines for MyBinder](https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html)

To run this repository's notebooks on MyBinder, please follow: 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ioos/soundcoop/v0.0.2)

### Google Colaboratory (Colab)
Colab is a online hosting service to run Jupyter Notebooks using free computing resources
* Sessions run for up to 12 hours
* VMs have ~ 13 GB of RAM
* Colab resources are dynamic. Usage limits, timeout periods, VM lifetime, available GPU types, etc vary over time.
* You will need a gmail account
* [Quotas and limits for Google Colab](https://cloud.google.com/colab/docs/quotas)

To run any of this repository's notebooks (separately) on Google Colab, please follow: 
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ioos/soundcoop/)

### JupyterLab
JupyterLab is a free browser-based software for interactive development and computing environment for notebooks
* Provides access to computational environments and resources
* Runs on the cloud or on your own hardware
* *Local environment*: You can access local data. Requires python and jupyter installation
* *Free environment*: You can't store your data. Has limited resources
* *Institution-based environment*: You can store your data and have vastly expanded resources available. Not widely available to everyone
* [Some info on JupyterLab 4.0 set up and environment](https://lwn.net/Articles/936340/)
* [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop), which takes advantage of your local machine's memory allocations and processing capabilities

To clone and run the notebooks of this repository on jupyterlab, follow: 
go to Git > Clone a Repository and add this repository url: https://github.com/ioos/soundcoop (or clone via terminal)
The notebook will be downloaded for you on this space, and you are ready to go! 
Make sure you either first install all the dependencies from the repository, by either running the install cells of each notebook or by initially install all the required dependencies. 
This second option can be done with 
```shell
poetry install
```

or 
```shell
pip install -r requirements.txt
```

