# pypam notebooks

> [!NOTE]
> - Under testing/tuning.
>

## Binder
To run the notebooks on mybinder, please follow:
For analysis notebook:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ioos/soundcoop/HEAD?labpath=2_analysis_of_HMD_pypam%2Fdata_analysis_with_pypam.ipynb)

For dimension reduction notebook: 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ioos/soundcoop/HEAD?labpath=2_analysis_of_HMD_pypam%2Fdimension_reduction_and_clustering.ipynb)


## Colab 
To run the notebooks in this repository in Google Colab, click on the colab link below: Note that you will need to have a Google account to run the notebooks in Colab.

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ioos/soundcoop/)


## Any jupyterhub environment (with the git plugin)
Once in the jupyterhub, go to Git > Clone a Repository
There you can add this repository url: https://github.com/ioos/soundcoop
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
