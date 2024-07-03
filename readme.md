# Generative Artificial Intelligence Notebooks
<!--[![DOI](https://zenodo.org/badge/449194300.svg)](https://zenodo.org/badge/latestdoi/449194300)-->

This repository contains a collection of Python Jupyter notebooks explaining generative artificial intelligence using Python to a broad audience. The content is available at

https://scads.github.io/generative-ai-notebooks

It is maintained using [Jupyter lab](https://jupyterlab.readthedocs.io/en/stable/) and build using [Jupyter book](https://jupyterbook.org/intro.html).

To edit this book, install depencencies like this:

```
pip install pyclesperanto-prototype
pip install jupyterlab
pip install jupyter-book
pip install jupyterlab-spellchecker

git clone https://github.com/scads/generative-ai-notebooks
cd  generative-ai-notebooks
jupyter lab
```

To build the book, you can run this from the same folder (tested on MacOS only):
```
cd docs
jupyterbook build .
```

## Acknowledgements

We acknowledge the financial support by the Federal Ministry of Education and Research of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the programme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig“, project identification number: ScaDS.AI