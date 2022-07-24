# Install and test GPU with python libraries

Basic repository to create your venv with tensorflow or pytorch using CUDA. When I am writing this, I am on a Windows 11 laptop with a GTX 1050.

## Install CUDA Toolkit

### Uninstall all CUDA related software

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

### Download CUDA Toolkit 


