# SoundCoop
This repository contains Jupyter notebooks developed by the passive acoustic community for the SoundCoop project.

The SoundCoop Project was a three-year effort funded by NOAA Integrated Ocean Observing System, Bureau for Ocean Energy Management, U.S Navy Living Marine Resources, and the Office of Naval Research. The goal of the project was to develop technology in collaboration with the passive acoustic monitoring (PAM) community to enable scalable processing of comparable sound level metrics and to provide open access to centralized data for science and management applications. 

U.S. and international scientists contributed PAM data spanning 12 separate long-term monitoring projects. Datasets from ten of these projects were used to calculate a specific sound level metric, [hybrid millidecade (HMD) spectra](https://doi.org/10.1121/10.0003324), across a diversity of labs and instruments.

The collaborative effort of the SoundCoop led to several advances in data management, processing, dissemination, visualization, and knowledge sharing. 
* Two open access software toolkits were produced/enhanced by project members to process SoundCoop datasets into one-minute HMD spectra, namely [MANTA](https://bitbucket.org/CLO-BRP/manta-wiki/wiki/Home) and [PyPAM](https://github.com/lifewatch/pypam)/ [PyPAM-Based Processing](https://pypi.org/project/mbari-pbp/)
* SoundCoop Project members, along with the NCEI passive acoustic data archive team, established a standards-driven netCDF format, which greatly facilitated comparison and distribution of the hybrid millidecade sound levels.
* The project developers at Axiom Data Science built an [interactive data portal](https://soundcoop.portal.axds.co/#) to visualize and explore the SoundCoop datasets alongside environmental data to show the benefits of connecting acoustic and non-acoustic information.

Three main Jupyter notebooks were created to demonstrate how to process passive acoustic data collected from two different recording instruments, accessed from two different open access cloud buckets, into hybrid millidecade spectra using PyPAM and PyPAM-Based Processing and output the result in the SoundCoop netCDF standard. The notebooks also demonstrate how to read in and visualize the hybrid millidecade netCDFs and integrate non-acoustic data.

## Jupyter Notebooks
1. Access X days of data recorded from the Monterey Bay Aquarium Research Institute (MBARI) Monterey Accelerated Research System (MARS) [undersea cabled observatory](https://www.mbari.org/data/passive-acoustic-data/) from the [Amazon Web Services (AWS) Registry of Open Data](https://www.mbari.org/project/open-acoustic-data/), create a timekeeping JSON of the data, apply calibration, create one-minute HMD spectra and output as a netCDF.
2. Access X days of data recorded from the NOAA-National Park Service Ocean Noise Reference Station Network [(NRS)](https://www.pmel.noaa.gov/acoustics/ocean-noise-reference.html) from the [NCEI Passive Acoustic Data Archive](https://www.ncei.noaa.gov/products/passive-acoustic-data) Google Cloud Platform (GCP) bucket available through the NOAA NODD Program, create a timekeeping JSON of the data, apply calibration, create one-minute HMD spectra and output as a netCDF.
3. Access one month of one-minute HMD recorded in the Stellwagen Bank National Marine Sanctuary as part of the [SanctSound project](https://sanctuaries.noaa.gov/science/monitoring/sound/sanctsound.html) from GCP and one month of MBARI-MARS one-minute HMD from AWS, 
