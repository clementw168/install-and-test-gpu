# Install and test GPU with python libraries

Basic repository to install CUDA and create your venv with Tensorflow or Pytorch using CUDA. When I am writing this, I am on a Windows 11 laptop with a GTX 1050. I will not use Conda.

## Summary

- [Install CUDA Toolkit](#install-cuda-toolkit)
  - [Uninstall CUDA](#uninstall-cuda)
  - [Find your CUDA version](#find-your-cuda-version)
  - [Install CUDA Toolkit](#install-cuda-toolkit)
  - [Download cuDNN](#download-cudnn)
  - [Test your installation](#test-your-installation)
- [Run a test with Pytorch or Tensorflow](#run-a-test-with-pytorch-or-tensorflow)
  - [Get started with Virtual Environment](#get-started-with-virtual-environment)
  - [Run a test with Pytorch](#run-a-test-with-pytorch)
  - [Run a test with Tensorflow](#run-a-test-with-tensorflow)

## Install CUDA Toolkit

### Uninstall CUDA

If you have previously installed a version of CUDA, you should get rid of it before proceeding. If not, you can skip this part.

To uninstall CUDA on Windows,

- Go to the Program and Features widget in the control panel on Windows
- Search for "CUDA" and uninstall everything related to this previous version of CUDA:
  - NVIDIA CUDA Visual Studio Integration
  - NVIDIA CUDA Samples
  - NVIDIA CUDA Runtime
  - NVIDIA CUDA Documentation
  - NVIDIA CUDA Development

That's all ! You can go on :)

### Find your CUDA version

DO NOT SKIP THIS STEP. I had to reinstall CUDA because of that... Before proceeding, you should know which version of Cuda you want according to which version your GPU can handle AND what library you will use.

All GPUs are not Cuda compatible. You have to check [here](https://en.wikipedia.org/wiki/CUDA#GPUs_supported). For instance, my GTX 1050 has a compute compatibility of 6.1 which can support any versions of CUDA for the moment. I could go on with any CUDA version from 10.0 to 10.2 and from 11.0 to 11.7.

However, if you are installing Cuda, you probably want to use another library such as Tensorflow and Pytorch. Your version of CUDA has to be compatible with any library you will use.
For Pytorch, you can easily check [here](https://pytorch.org/get-started/locally/).
For Tensorflow, you can check [here](https://docs.nvidia.com/deeplearning/frameworks/tensorflow-wheel-release-notes/overview.html#overview). If there is wheel that matches your desired CUDA version then it is ok! Be careful about what you read on the Internet. The latest version of Tensorflow right now is 2.9.0 which is optimized for CUDA 11.2. However, more recent versions of CUDA can still be compatible as long as the correct wheel does exist!

I will go on with CUDA 11.6 as though Tensorflow supports 11.7, Pytorch does not support 11.7 yet.

### Install CUDA Toolkit

- Click on this [link](https://developer.nvidia.com/cuda-toolkit)
- Click on the button "Download" and you will be redirected to the latest version of CUDA.
- If that is not the correct version,
  - Scroll down to the resources
  - Click on "Archive of Previous CUDA Releases"
  - Find your version and download it.
- Install CUDA through the program

You might need to update your CUDA Drivers.

### Download cuDNN

Cuda is a library that allows you to use the GPU efficiently. However, to use your GPU even more efficiently, cuDNN implements some standard operations for Deep Neural Networks such as forward propagation, backpropagation for convolutions, pooling, normalization, etc. In order to you Pytorch and Tensorflow, you need to install cuDNN.

- Click on this [link](https://developer.nvidia.com/cudnn)
- Click on the button "Download" and you will be redirected to the latest version of cuDNN. If any doubt, you can check this [compatibility matrix](https://docs.nvidia.com/deeplearning/cudnn/support-matrix/index.html).
- You might be asked to register and fill a form.
- Find the version corresponding to your version of CUDA and download it.
- Extract all folders:
  - lib
  - include
  - bin
- Copy `<cudnn_path>\bin\cudnn\*.dll` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vx.x\bin`
- Copy `<cudnn_path>\cuda\include\cudnn\*.h` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vx.x\include`
- Copy `<cudnn_path>\cuda\lib\x64\cudnn\*.lib` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vx.x\lib\x64`
- You can then delete cuDNN folder
  Note : Some people just replace CUDA folders by cuDNN folders so it should not a problem.

### Test your installation

- Open a Command line interface and type `nvcc -V` (`V` is uppercase). It should display the correct Cuda version.
- Try to run a test with Pytorch or Tensorflow.

## Run a test with Pytorch or Tensorflow

### Get started with Virtual Environment

Skip this part if you already know what virtual environments are and how to use them

You could just install all your packages in your default Python environment. You would have all your packages by default, and that is not so bad if you just want to test something on your computer. However, more often than not, you will want to use virtual environments to have a clean environment, especially when you are working in a team or when you are working on a project that will be used by others.

Main reasons for using virtual environments are:

- You want to isolate your packages from the rest of your computer. Then you know exactly what packages with which version are used by your project. This is useful, especially for someone else, to know what packages are used by your project.
- You can break your environment if you want to. You can easily delete a virtual environment and create a new one. Everyone has already broken python because of dependencies issues.
- Conda does the same more or less and is sometimes more convenient. However, it takes a lot more memory on the computer. Conda is also more likely to break because of dependencies issues, as it automatically downloads many packages. Virtual environments make you more flexible, so less likely to break as you know what you are doing.

Good practice is to create a virtual environment for each project.

Virtual environments need a `requirements.txt` file. This file contains the packages needed by your project. Then you can install them with `pip install -r requirements.txt`. That way, anyone can use your project, and you will not have to worry about dependencies issues.

To create a virtual environment, you can use the following command:

```
python -m venv <virtual_environment_name>
```

You can then activate the virtual environment with the following command:

```
source <virtual_environment_name>/Scripts/activate
```

Now you can install your packages with

```
pip install <package_name>
```

You can also install all dependencies of a project with a `requirements.txt` file:

```
pip install -r requirements.txt
```

### Run a test with Pytorch

Create a virtual environment for your project.

```
python -m venv <virtual_environment_name>
```

Before proceeding, you should check the correct version of Pytorch for your version of CUDA [here](https://pytorch.org/get-started/locally/). Choose a stable version to install with pip, which corresponds to your version of CUDA. Then, open `pytorch_utils/pytorch_requirements.txt` and change the wheel for Pytorch installation if necessary.

You can then install your packages with

```
pip install -r pytorch_utils/pytorch_requirements.txt
```

If something went wrong, I also put an exact requirements.txt file in the repository : `pytorch_utils/pytroch_exact_requirements.txt`.
To test your installation, you can run the following command:

```
python -m pytorch_main
```

It should display some information on your GPU and train a multiperceptron on MNIST. You can check that your GPU is used on your `task Manager`. Open it with `Ctrl+Shift+Esc`.

### Run a test with Tensorflow

Create a virtual environment for your project.

```
python -m venv <virtual_environment_name>
```

You can then install your packages with

```
pip install -r tensorflow_utils/tf_requirements.txt
```

If something went wrong, I also put an exact requirements.txt file in the repository : `tensorflow_utils/tf_exact_requirements.txt`.
To test your installation, you can run the following command:

```
python -m tensorflow_main
```

It should display some information on your GPU and train a multiperceptron on MNIST. You can check that your GPU is used on your `task Manager`. Open it with `Ctrl+Shift+Esc`.
