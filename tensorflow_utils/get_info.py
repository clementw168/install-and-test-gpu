import tensorflow as tf

def tf_info():
    print('TensorFlow version:', tf.__version__)
    print('Tensorflow is build with CUDA:', tf.test.is_built_with_cuda())

def gpu_info():
    gpu_list = tf.config.experimental.list_physical_devices('GPU')
    print('GPU is available:', len(gpu_list) > 0)
    if len(gpu_list) > 0:
        print('TensorFlow GPU count:', len(gpu_list))
        for ind, gpu in enumerate(gpu_list):
            print("*"*20)
            print("GPU {}:".format(ind))
            print("Tensorflow name:", gpu.name)
            device = tf.config.experimental.get_device_details(gpu)
            print("Device name:", device["device_name"])
            print("Compute capability:", device["compute_capability"])

