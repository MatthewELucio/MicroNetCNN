# MicroNetCNN
training cnn on micronet

## Setup

Create virtual environment (in MicroNetCNN directory) and install python packages/libraries

```bash
python3 -m venv .venv
source .venv/bin/activate # (or open new terminal and it should do this automatically)
pip install -r requirements.txt
```

Then run script to populate micronet_images directory

```bash
python3 download_images.py
```