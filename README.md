# graph-transfer-learning

This repository contains ongoing research into the transfer learning of
Graph Neural Networks.


# Installation

This project uses `poetry` for dependency management.

The following system configurations are supported:

| System type | Install methods | 
|-------------|-----------------|
| Linux + CUDA 11.7 compatible card | Docker, Poetry|
| Apple Silcon Macs (GPU accelerated) | Poetry|
| Intel Macs (CPU) | Poetry|


Further systems could be added (if desired) by adding the systems' `dgl` wheels to the `pyproject.toml` file.

## Docker

Docker container running CUDA 11.7 has been provided. A working installation of NVIDIA container toolkit on the host machine is requried for this to work.

This has been tested on Ubuntu and a GTX 3060 card only.


**Run the following from this directory:**

First, build the container:

```
docker build . -t graph-transfer-learning/devel
```

Then, run the container:

```
docker run -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 --runtime=nvidia -v "$(pwd):/workspace" graph-transfer-learning/devel
```

The repository on your local system will be mounted to the `/workspace/` folder in the container.

## Poetry

After installing `poetry`, run `poetry shell` to enter the project environment.

# Usage

* Library code is contained within the `src` directory.

* Executable code, including experiments, is contained in the `scripts`
  directory. 

<!-- vim: tw=80 cc=80
-->



