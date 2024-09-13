# SoundCoop
This repository contains Jupyter notebooks developed by the SoundCoop project team for the passive acoustic community.

The SoundCoop Project was a three-year effort funded by NOAA Integrated Ocean Observing System, Bureau for Ocean Energy Management, U.S Navy Living Marine Resources, and the Office of Naval Research. The goal of the project was to develop technology in collaboration with the passive acoustic monitoring (PAM) community to enable scalable processing of comparable sound level metrics and to provide open access to centralized data for science and management applications. 

U.S. and international scientists contributed PAM data spanning 12 separate long-term monitoring projects. Datasets from ten of these projects were used to calculate a specific sound level metric, [hybrid millidecade (HMD) spectra](https://doi.org/10.1121/10.0003324), across a diversity of labs and instruments.

The collaborative effort of the SoundCoop led to several advances in data management, processing, dissemination, visualization, and knowledge sharing. 
* Two open access software toolkits were produced/enhanced by project members to process SoundCoop datasets into one-minute HMD spectra, namely [MANTA](https://bitbucket.org/CLO-BRP/manta-wiki/wiki/Home) and [PyPAM](https://github.com/lifewatch/pypam)/[PyPAM-Based Processing](https://pypi.org/project/mbari-pbp/)
* SoundCoop Project members, along with the NCEI passive acoustic data archive team, established a standards-driven netCDF format, which greatly facilitated comparison and distribution of the hybrid millidecade sound levels.
* The project developers at Axiom Data Science built an [interactive data portal](https://soundcoop.portal.axds.co/#) to visualize and explore the SoundCoop datasets alongside environmental data to show the benefits of connecting acoustic and non-acoustic information.

Four main Jupyter notebooks were created to demonstrate how to process passive acoustic data collected from two different recording instruments, accessed from two different open access cloud buckets, into hybrid millidecade spectra using PyPAM and PyPAM-Based Processing and output the result in the SoundCoop netCDF standard. The notebooks also demonstrate how to read in and visualize the hybrid millidecade netCDFs and integrate non-acoustic data.

## Jupyter Notebooks
**MARS Data**: Access X days of data recorded from the Monterey Bay Aquarium Research Institute (MBARI) Monterey Accelerated Research System (MARS) [undersea cabled observatory](https://www.mbari.org/data/passive-acoustic-data/) from the [Amazon Web Services (AWS) Registry of Open Data](https://www.mbari.org/project/open-acoustic-data/), create a timekeeping JSON of the data, apply calibration, create one-minute HMD spectra and output as a netCDF.

**NRS DATA**: Access X days of data recorded from the NOAA-National Park Service Ocean Noise Reference Station Network [(NRS)](https://www.pmel.noaa.gov/acoustics/ocean-noise-reference.html) from the [NCEI Passive Acoustic Data Archive](https://www.ncei.noaa.gov/products/passive-acoustic-data) Google Cloud Platform (GCP) bucket available through the NOAA NODD Program, create a timekeeping JSON of the data, apply calibration, create one-minute HMD spectra and output as a netCDF.

**HMD with PyPAM**: Access one year of one-minute HMD recorded in the Stellwagen Bank National Marine Sanctuary as part of the [SanctSound project](https://sanctuaries.noaa.gov/science/monitoring/sound/sanctsound.html) from GCP and one month of MBARI-MARS one-minute HMD from AWS, read in and plot the time series for both sites where data quality tags are set to 'Good', aggregate the data to one week resolution, extract and plot the blue and fin whale call index (CI), and reprocess the one-week resolution HMD into monthly broadband spectra and plot.

**plot_sound_environmental_and_climatology_data**: Access two months of HMD recorded at Monhegan Island site in the Gulf of Maine from the GCP bucket, access associated wind speed and wave height recorded at the 44007 environmental sensor station located ~72 km from the listening site from October 23, 2021 to November 17, 2021, and plot the one-hour resolution HMD spectra recorded during three wind speed and wave height categories. This example shows the passing of two storms where elevated wind speed and wave height increase the amplitude of the ocean soundscape.
  + This notebook replicates plots created in the SoundCoop portal. Use the portal to select the acoustic dataset, environmental sensor or model dataset as well as the desired time period and frequency range. Copy the snippet of python code displayed in the portal that identifies the ERDDAP ID for the selected environmental dataset and parameters for the selected acoustic dataset, and paste it in this notebook to reproduce the plots.
  + This notebook also contains an additional feature where the sound levels are plotted by temperature anomaly bins calculated using [NOAA 1-degree World Ocean Atlas 2023](https://www.ncei.noaa.gov/products/world-ocean-atlas) temperature values for a given point and month.
  + Note: a limited number of recorded days (~20) are recommended to avoid memory issues during processing. If more days are desired for your analysis, ensure your compute environment has enough RAM and CPU/GPU

Several additional notebooks are included in this repository to demonstrate how to access datasets from different repositories
**use_minio_to_access_GCP**: This notebook shows how to download files from Google Cloud Platform, specifically SB03 HMD netCDFs from the NCEI SoundCoop bucket on GCP.

**download_ESONS_from_rw**: This notebook shows how to access HMD netCDF files recorded at the ESONS listening site from the Axiom Data Science Research Workspace

**download_JOMOPANS_from_rw**: This notebook shows how to access one-third octave sound levels recorded at a listening site in the North Sea as part of the [JOMOPANS project](https://northsearegion.eu/jomopans/). Originally accessed from the [ICES database](https://www.ices.dk/data/data-portals/Pages/Continuous-Noise.aspx), the HDF files were translated into netCDF and are hosted on the Axiom Data Science Research Workspace

## Running the Notebooks
The notebooks were built so they could run in free environments such as [MyBinder](https://mybinder.org/), [Google Colab](https://colab.research.google.com/), and [JupyterLab](https://jupyter.org/), meaning they aimed to have low requirements for RAM an CPU. The tradeoff is a reduced amount of data to view and process. These notebooks are for demonstration purposes and can serve as the foundation for large scale processing that is typical of passive acoustic data analyses. 

Please review the content in the following links regarding the processing environments noted above
* [Usage guidelines for MyBinder](https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html)
* [Quotas and limites for Google Colab](https://cloud.google.com/colab/docs/quotas)
* [Some info on JupyterLab 4.0 set up and environment](https://lwn.net/Articles/936340/)
  
An environment yaml file is provided to ensure that the jupyter notebooks can be run without issues related to system and library dependencies.

