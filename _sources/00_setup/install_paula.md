# Installation instructions for Scientific Computing Uni Leipzig (paula)

Request a [Scientific Computing Account at ULei](https://www.urz.uni-leipzig.de/servicedesk-und-hilfe/hilfe-zu-unseren-services/forschung/hilfe-webbasiertes-data-science-und-machine-learning-mit-jupyter).

Login to VPN and [Jupyter Hub](https://lab.sc.uni-leipzig.de/), select the configuration paula/A30:

![](config-paula.png)

Open a terminal and install [ana]conda
```
module load Anaconda3
```

```
module load Mamba
```

```
conda init bash
```

At this point, we need to reopen the terminal. Afterwards, create a conda environment with one specific python version only.

```
mamba env create -f https://raw.githubusercontent.com/ScaDS/generative-ai-notebooks/main/docs/00_setup/environment-gpu.yml
```

```
conda activate genai-gpu
```

Make this conda environment available to Jupyter hub like this:
```
python -m ipykernel install --user --name 'genai' --display-name "ScaDS.AI genai"
```

To make stackview work, install it outside the conda environment:
```
conda deactivate
```

```
pip install stackview --user
```
... and reload the page (in browser)


Just in case you want to install more packages later, reopen the terminal, activate the environment and install them:
```
conda activate genai-gpu
pip install other-package 
```

## Troubleshooting

In case the Jupyter Kernel doesn't work and/or needs to be removed, you can check if it's installed by printing out the list of installed kernels:

```
jupyter kernelspec list
```

And you can uninstall them using this command:

```
jupyter kernelspec uninstall genai
```

## Read more

These instructions were derived/modified from [this page](https://www.sc.uni-leipzig.de/05_Instructions/Jupyter/#how-to-use-your-own-environments-and-kernels).

