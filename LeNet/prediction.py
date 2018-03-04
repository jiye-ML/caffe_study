# 导入必要的模块
import caffe
from skimage import io

modelfile = 'deploy.prototxt'
pretrain = 'lenet_iter_10000.caffemodel'
imagefile = '3.jpeg'

img = io.imread(imagefile)
io.imshow(img)

inputimage = caffe.io.load_image(imagefile, color=False)

net = caffe.Classifier(modelfile, pretrain)
prediction = net.predict([inputimage], oversample=False)
caffe.set_mode_gpu()

print('predicted class:', prediction[0].argmax())
