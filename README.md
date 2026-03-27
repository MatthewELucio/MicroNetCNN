# MicroNetCNN
training cnn on micronet

## Setup

On the UVA CS portal create virtual environment (in MicroNetCNN directory) and install python packages/libraries

```bash
module load gcc # can add to ~/.bashrc
module load clang # can add to ~/.bashrc
python3 -m venv .venv
source .venv/bin/activate # (or open new terminal and it should do this automatically)
pip install -r requirements.txt
```

Then run script to populate micronet_images directory

```bash
python3 download_images.py
```