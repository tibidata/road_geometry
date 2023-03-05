import imageio as iio
import matplotlib.pyplot as plt


filename = '../test_images/production ID_4832678.mp4'

video = iio.get_reader(filename,'ffmpeg')

for frame in iio.imiter(filename, plugin="pyav"):
    print(frame.shape, frame.dtype)
    print(frame)

