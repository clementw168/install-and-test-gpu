# Install and test GPU with python libraries

Basic repository to create your venv with tensorflow or pytorch using CUDA. When I am writing this, I am on a Windows 11 laptop with a GTX 1050. I will not use Conda. 

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

### Download CUDA Toolkit 

- Click on this [link](https://developer.nvidia.com/cuda-toolkit) 
- Click on the button "Download" and you will be redirected to the latest version of CUDA. 
- If that is not the correct version, 
  - Scroll down to the ressources
  - Click on "Archive of Previous CUDA Releases"
  - Find you version and download it. 
- Install CUDA throught the programm 

And you are done!

### Test your installation

- Open a Command line interface and type `nvcc -V` (`V` is uppercase). It should display the correct Cuda version. 
- Try to run a test with Pytorch or Tensorflow.

## Run a test with Pytorch


## Run a test with Tensorflow 

