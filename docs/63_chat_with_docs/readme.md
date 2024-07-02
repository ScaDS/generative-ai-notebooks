# Simple Chat with Docs

This repository contains a simple Chat interface based on [voila](https://github.com/voila-dashboards/voila), [OpenAI](https://openai.com/index/openai-api/)  and [llama-index](https://github.com/run-llama/llama_index) that allows you to query information from documents using human language.

After installation (see below) you can start the chat using this terminal command:

```
voila chat-with-docs.ipynb
```

![](docs/screenshot.png)

The cods in this repository is derived from the tutorial [here](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/).

## Installation

Create an OpenAI API Key and add it to your environment variables as explained on [this page](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety).

You can install everything necessary using pip. It is recommended to install it into via conda/mamba environment. If you have never used conda before, please [read this guide first](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html).  

```
mamba create --name simple-chat python=3.11 git
```

```
mamba activate simple-chat
```

```
git clone https://github.com/haesleinhuepf/simple-chat-with-docs
```

```
cd simple-chat-with-docs
```

```
pip install -r requirements.txt
```