#%%
import tensorflow as tf
from tensorflow.keras.layers import layer, conv2d, globalaveragepooling2d, dense, add, batchnormalization, leakyrelu
from tensorflow.keras.models import model
#%%
class conv2d(layer):
    def __init__(self, filters, kernel_size, strides=1, **kwargs):
        super(conv2d, self).__init__(**kwargs)
        self.filters = filters
        self.kernel_size = kernel_size
        self.strides = strides

    def build(self, input_shape):
        self.conv = conv2d(self.filters, self.kernel_size, self.strides, padding=("same" if self.strides==1 else "valid"))
        super(conv2d, self).build(input_shape)

    def call(self, inputs):
        tensor = inputs
        if self.strides > 1:
            pad_total = self.kernel_size - 1
            pad_beg = pad_total // 2
            pad_end = pad_total - pad_beg
            tensor = tf.pad(tensor, [[0, 0], [pad_beg, pad_end], [pad_beg, pad_end], [0, 0]])
        tensor = self.conv(tensor)
        return tensor

#%%
class Darknet53(Model):
    def __init__(self):
        super(Darknet53, self).__init__(self)
        #convolution
        self.cv1_cv = conv2d(32, 3, name="conv1_conv")
        self.cv1_bn = BatchNormalization(name="conv1_bn")
        self.cv1_ac = LeakyReLU(name="conv1_leakyrelu")
        #convolution
        self.cv2_cv = conv2d(64, 3, 2, name="conv2_conv")
        self.cv2_bn = BatchNormalization(name="conv2_bn")
        self.cv2_ac = LeakyReLU(name="conv2_leakyrelu")
        #res block 1
        self.cv3_b1_1_cv = conv2d(32, 1, name="conv3_block1_1_conv")
        self.cv3_b1_1_bn = BatchNormalization(name="conv3_block1_1_bn")
        self.cv3_b1_1_ac = LeakyReLU(name="conv3_block1_1_leakyrelu")
        self.cv3_b1_2_cv = conv2d(64, 3, name="conv3_block1_2_conv")
        self.cv3_b1_2_bn = BatchNormalization(name="conv3_block1_2_bn")
        self.cv3_b1_2_ac = LeakyReLU(name="conv3_block1_2_leakyrelu")
        self.cv3_b1_add = Add(name="conv3_block1_add")
        #convolution
        self.cv4_cv = conv2d(128, 3, 2, name="conv4_conv")
        self.cv4_bn = BatchNormalization(name="conv4_bn")
        self.cv4_ac = LeakyReLU(name="conv4_leakyrelu")
        #res block 2 1
        self.cv5_b1_1_cv = conv2d(64, 1, name="conv5_block1_1_conv")
        self.cv5_b1_1_bn = BatchNormalization(name="conv5_block1_1_bn")
        self.cv5_b1_1_ac = LeakyReLU(name="conv5_block1_1_leakyrelu")
        self.cv5_b1_2_cv = conv2d(128, 3, name="conv5_block1_2_conv")
        self.cv5_b1_2_bn = BatchNormalization(name="conv5_block1_2_bn")
        self.cv5_b1_2_ac = LeakyReLU(name="conv5_block1_2_leakyrelu")
        self.cv5_b1_add = Add(name="conv5_block1_add")
        #res block 2 2
        self.cv5_b2_1_cv = conv2d(64, 1, name="conv5_block2_1_conv")
        self.cv5_b2_1_bn = BatchNormalization(name="conv5_block2_1_bn")
        self.cv5_b2_1_ac = LeakyReLU(name="conv5_block2_1_leakyrelu")
        self.cv5_b2_2_cv = conv2d(128, 3, name="conv5_block2_2_conv")
        self.cv5_b2_2_bn = BatchNormalization(name="conv5_block2_2_bn")
        self.cv5_b2_2_ac = LeakyReLU(name="conv5_block2_2_leakyrelu")
        self.cv5_b2_add = Add(name="conv5_block2_add")
        #convolution
        self.cv6_cv = conv2d(256, 3, 2, name="conv6_conv")
        self.cv6_bn = BatchNormalization(name="conv6_bn")
        self.cv6_ac = LeakyReLU(name="conv6_leakyrelu")
        # res block 3 1
        self.cv7_b1_1_cv = conv2d(128, 1, name="conv7_block1_1_conv")
        self.cv7_b1_1_bn = BatchNormalization(name="conv7_block1_1_bn")
        self.cv7_b1_1_ac = LeakyReLU(name="conv7_block1_1_leakyrelu")
        self.cv7_b1_2_cv = conv2d(256, 3, name="conv7_block1_2_conv")
        self.cv7_b1_2_bn = BatchNormalization(name="conv7_block1_2_bn")
        self.cv7_b1_2_ac = LeakyReLU(name="conv7_block1_2_leakyrelu")
        self.cv7_b1_add = Add(name="conv7_block1_add")
        # res block 3 2
        self.cv7_b2_1_cv = conv2d(128, 1, name="conv7_block2_1_conv")
        self.cv7_b2_1_bn = BatchNormalization(name="conv7_block2_1_bn")
        self.cv7_b2_1_ac = LeakyReLU(name="conv7_block2_1_leakyrelu")
        self.cv7_b2_2_cv = conv2d(256, 3, name="conv7_block2_2_conv")
        self.cv7_b2_2_bn = BatchNormalization(name="conv7_block2_2_bn")
        self.cv7_b2_2_ac = LeakyReLU(name="conv7_block2_2_leakyrelu")
        self.cv7_b2_add = Add(name="conv7_block2_add")
        # res block 3 3
        self.cv7_b3_1_cv = conv2d(128, 1, name="conv7_block3_1_conv")
        self.cv7_b3_1_bn = BatchNormalization(name="conv7_block3_1_bn")
        self.cv7_b3_1_ac = LeakyReLU(name="conv7_block3_1_leakyrelu")
        self.cv7_b3_2_cv = conv2d(256, 3, name="conv7_block3_2_conv")
        self.cv7_b3_2_bn = BatchNormalization(name="conv7_block3_2_bn")
        self.cv7_b3_2_ac = LeakyReLU(name="conv7_block3_2_leakyrelu")
        self.cv7_b3_add = Add(name="conv7_block3_add")
        # res block 3 4
        self.cv7_b4_1_cv = conv2d(128, 1, name="conv7_block4_1_conv")
        self.cv7_b4_1_bn = BatchNormalization(name="conv7_block4_1_bn")
        self.cv7_b4_1_ac = LeakyReLU(name="conv7_block4_1_leakyrelu")
        self.cv7_b4_2_cv = conv2d(256, 3, name="conv7_block4_2_conv")
        self.cv7_b4_2_bn = BatchNormalization(name="conv7_block4_2_bn")
        self.cv7_b4_2_ac = LeakyReLU(name="conv7_block4_2_leakyrelu")
        self.cv7_b4_add = Add(name="conv7_block4_add")
        # res block 3 5
        self.cv7_b5_1_cv = conv2d(128, 1, name="conv7_block5_1_conv")
        self.cv7_b5_1_bn = BatchNormalization(name="conv7_block5_1_bn")
        self.cv7_b5_1_ac = LeakyReLU(name="conv7_block5_1_leakyrelu")
        self.cv7_b5_2_cv = conv2d(256, 3, name="conv7_block5_2_conv")
        self.cv7_b5_2_bn = BatchNormalization(name="conv7_block5_2_bn")
        self.cv7_b5_2_ac = LeakyReLU(name="conv7_block5_2_leakyrelu")
        self.cv7_b5_add = Add(name="conv7_block5_add")
        # res block 3 6
        self.cv7_b6_1_cv = conv2d(128, 1, name="conv7_block6_1_conv")
        self.cv7_b6_1_bn = BatchNormalization(name="conv7_block6_1_bn")
        self.cv7_b6_1_ac = LeakyReLU(name="conv7_block6_1_leakyrelu")
        self.cv7_b6_2_cv = conv2d(256, 3, name="conv7_block6_2_conv")
        self.cv7_b6_2_bn = BatchNormalization(name="conv7_block6_2_bn")
        self.cv7_b6_2_ac = LeakyReLU(name="conv7_block6_2_leakyrelu")
        self.cv7_b6_add = Add(name="conv7_block6_add")
        # res block 3 7
        self.cv7_b7_1_cv = conv2d(128, 1, name="conv7_block7_1_conv")
        self.cv7_b7_1_bn = BatchNormalization(name="conv7_block7_1_bn")
        self.cv7_b7_1_ac = LeakyReLU(name="conv7_block7_1_leakyrelu")
        self.cv7_b7_2_cv = conv2d(256, 3, name="conv7_block7_2_conv")
        self.cv7_b7_2_bn = BatchNormalization(name="conv7_block7_2_bn")
        self.cv7_b7_2_ac = LeakyReLU(name="conv7_block7_2_leakyrelu")
        self.cv7_b7_add = Add(name="conv7_block7_add")
        # res block 3 8
        self.cv7_b8_1_cv = conv2d(128, 1, name="conv7_block8_1_conv")
        self.cv7_b8_1_bn = BatchNormalization(name="conv7_block8_1_bn")
        self.cv7_b8_1_ac = LeakyReLU(name="conv7_block8_1_leakyrelu")
        self.cv7_b8_2_cv = conv2d(256, 3, name="conv7_block8_2_conv")
        self.cv7_b8_2_bn = BatchNormalization(name="conv7_block8_2_bn")
        self.cv7_b8_2_ac = LeakyReLU(name="conv7_block8_2_leakyrelu")
        self.cv7_b8_add = Add(name="conv7_block8_add")
        #convolution
        self.cv8_cv = conv2d(512, 3, 2, name="conv8_conv")
        self.cv8_bn = BatchNormalization(name="conv8_bn")
        self.cv8_ac = LeakyReLU(name="conv8_leakyrelu")
        # res block 4 1
        self.cv9_b1_1_cv = conv2d(256, 1, name="conv9_block1_1_conv")
        self.cv9_b1_1_bn = BatchNormalization(name="conv9_block1_1_bn")
        self.cv9_b1_1_ac = LeakyReLU(name="conv9_block1_1_leakyrelu")
        self.cv9_b1_2_cv = conv2d(512, 3, name="conv9_block1_2_conv")
        self.cv9_b1_2_bn = BatchNormalization(name="conv9_block1_2_bn")
        self.cv9_b1_2_ac = LeakyReLU(name="conv9_block1_2_leakyrelu")
        self.cv9_b1_add = Add(name="conv9_block1_add")
        # res block 4 2
        self.cv9_b2_1_cv = conv2d(256, 1, name="conv9_block2_1_conv")
        self.cv9_b2_1_bn = BatchNormalization(name="conv9_block2_1_bn")
        self.cv9_b2_1_ac = LeakyReLU(name="conv9_block2_1_leakyrelu")
        self.cv9_b2_2_cv = conv2d(512, 3, name="conv9_block2_2_conv")
        self.cv9_b2_2_bn = BatchNormalization(name="conv9_block2_2_bn")
        self.cv9_b2_2_ac = LeakyReLU(name="conv9_block2_2_leakyrelu")
        self.cv9_b2_add = Add(name="conv9_block2_add")
        # res block 4 3
        self.cv9_b3_1_cv = conv2d(256, 1, name="conv9_block3_1_conv")
        self.cv9_b3_1_bn = BatchNormalization(name="conv9_block3_1_bn")
        self.cv9_b3_1_ac = LeakyReLU(name="conv9_block3_1_leakyrelu")
        self.cv9_b3_2_cv = conv2d(512, 3, name="conv9_block3_2_conv")
        self.cv9_b3_2_bn = BatchNormalization(name="conv9_block3_2_bn")
        self.cv9_b3_2_ac = LeakyReLU(name="conv9_block3_2_leakyrelu")
        self.cv9_b3_add = Add(name="conv9_block3_add")
        # res block 4 4
        self.cv9_b4_1_cv = conv2d(256, 1, name="conv9_block4_1_conv")
        self.cv9_b4_1_bn = BatchNormalization(name="conv9_block4_1_bn")
        self.cv9_b4_1_ac = LeakyReLU(name="conv9_block4_1_leakyrelu")
        self.cv9_b4_2_cv = conv2d(512, 3, name="conv9_block4_2_conv")
        self.cv9_b4_2_bn = BatchNormalization(name="conv9_block4_2_bn")
        self.cv9_b4_2_ac = LeakyReLU(name="conv9_block4_2_leakyrelu")
        self.cv9_b4_add = Add(name="conv9_block4_add")
        # res block 4 5
        self.cv9_b5_1_cv = conv2d(256, 1, name="conv9_block5_1_conv")
        self.cv9_b5_1_bn = BatchNormalization(name="conv9_block5_1_bn")
        self.cv9_b5_1_ac = LeakyReLU(name="conv9_block5_1_leakyrelu")
        self.cv9_b5_2_cv = conv2d(512, 3, name="conv9_block5_2_conv")
        self.cv9_b5_2_bn = BatchNormalization(name="conv9_block5_2_bn")
        self.cv9_b5_2_ac = LeakyReLU(name="conv9_block5_2_leakyrelu")
        self.cv9_b5_add = Add(name="conv9_block5_add")
        # res block 4 6
        self.cv9_b6_1_cv = conv2d(256, 1, name="conv9_block6_1_conv")
        self.cv9_b6_1_bn = BatchNormalization(name="conv9_block6_1_bn")
        self.cv9_b6_1_ac = LeakyReLU(name="conv9_block6_1_leakyrelu")
        self.cv9_b6_2_cv = conv2d(512, 3, name="conv9_block6_2_conv")
        self.cv9_b6_2_bn = BatchNormalization(name="conv9_block6_2_bn")
        self.cv9_b6_2_ac = LeakyReLU(name="conv9_block6_2_leakyrelu")
        self.cv9_b6_add = Add(name="conv9_block6_add")
        # res block 4 7
        self.cv9_b7_1_cv = conv2d(256, 1, name="conv9_block7_1_conv")
        self.cv9_b7_1_bn = BatchNormalization(name="conv9_block7_1_bn")
        self.cv9_b7_1_ac = LeakyReLU(name="conv9_block7_1_leakyrelu")
        self.cv9_b7_2_cv = conv2d(512, 3, name="conv9_block7_2_conv")
        self.cv9_b7_2_bn = BatchNormalization(name="conv9_block7_2_bn")
        self.cv9_b7_2_ac = LeakyReLU(name="conv9_block7_2_leakyrelu")
        self.cv9_b7_add = Add(name="conv9_block7_add")
        # res block 4 8
        self.cv9_b8_1_cv = conv2d(256, 1, name="conv9_block8_1_conv")
        self.cv9_b8_1_bn = BatchNormalization(name="conv9_block8_1_bn")
        self.cv9_b8_1_ac = LeakyReLU(name="conv9_block8_1_leakyrelu")
        self.cv9_b8_2_cv = conv2d(512, 3, name="conv9_block8_2_conv")
        self.cv9_b8_2_bn = BatchNormalization(name="conv9_block8_2_bn")
        self.cv9_b8_2_ac = LeakyReLU(name="conv9_block8_2_leakyrelu")
        self.cv9_b8_add = Add(name="conv9_block8_add")
        #convolution
        self.cv10_cv = conv2d(1024, 3, 2, name="conv10_conv")
        self.cv10_bn = BatchNormalization(name="conv10_bn")
        self.cv10_ac = LeakyReLU(name="conv10_leakyrelu")
        # res block 5 1
        self.cv11_b1_1_cv = conv2d(512, 1, name="conv11_block1_1_conv")
        self.cv11_b1_1_bn = BatchNormalization(name="conv11_block1_1_bn")
        self.cv11_b1_1_ac = LeakyReLU(name="conv11_block1_1_leakyrelu")
        self.cv11_b1_2_cv = conv2d(1024, 3, name="conv11_block1_2_conv")
        self.cv11_b1_2_bn = BatchNormalization(name="conv11_block1_2_bn")
        self.cv11_b1_2_ac = LeakyReLU(name="conv11_block1_2_leakyrelu")
        self.cv11_b1_add = Add(name="conv11_block1_add")
        # res block 5 2
        self.cv11_b2_1_cv = conv2d(512, 1, name="conv11_block2_1_conv")
        self.cv11_b2_1_bn = BatchNormalization(name="conv11_block2_1_bn")
        self.cv11_b2_1_ac = LeakyReLU(name="conv11_block2_1_leakyrelu")
        self.cv11_b2_2_cv = conv2d(1024, 3, name="conv11_block2_2_conv")
        self.cv11_b2_2_bn = BatchNormalization(name="conv11_block2_2_bn")
        self.cv11_b2_2_ac = LeakyReLU(name="conv11_block2_2_leakyrelu")
        self.cv11_b2_add = Add(name="conv11_block2_add")
        # res block 5 3
        self.cv11_b3_1_cv = conv2d(512, 1, name="conv11_block3_1_conv")
        self.cv11_b3_1_bn = BatchNormalization(name="conv11_block3_1_bn")
        self.cv11_b3_1_ac = LeakyReLU(name="conv11_block3_1_leakyrelu")
        self.cv11_b3_2_cv = conv2d(1024, 3, name="conv11_block3_2_conv")
        self.cv11_b3_2_bn = BatchNormalization(name="conv11_block3_2_bn")
        self.cv11_b3_2_ac = LeakyReLU(name="conv11_block3_2_leakyrelu")
        self.cv11_b3_add = Add(name="conv11_block3_add")
        # res block 5 4
        self.cv11_b4_1_cv = conv2d(512, 1, name="conv11_block4_1_conv")
        self.cv11_b4_1_bn = BatchNormalization(name="conv11_block4_1_bn")
        self.cv11_b4_1_ac = LeakyReLU(name="conv11_block4_1_leakyrelu")
        self.cv11_b4_2_cv = conv2d(1024, 3, name="conv11_block4_2_conv")
        self.cv11_b4_2_bn = BatchNormalization(name="conv11_block4_2_bn")
        self.cv11_b4_2_ac = LeakyReLU(name="conv11_block4_2_leakyrelu")
        self.cv11_b4_add = Add(name="conv11_block4_add")
        #
        self.avg_pool = GlobalAveragePooling2D(name="average_pool")
        self.dense = Dense(1000, activation="softmax", name="predictions")
            

    def call(self, inputs):
        #convolution
        x = self.cv1_cv(inputs)
        x = self.cv1_bn(x)
        x = self.cv1_ac(x)
        #convolution
        x = self.cv2_cv(x)
        x = self.cv2_bn(x)
        x = self.cv2_ac(x)
        #res block 1
        x_ = self.cv3_b1_1_cv(x)
        x_ = self.cv3_b1_1_bn(x_)
        x_ = self.cv3_b1_1_ac(x_)
        x_ = self.cv3_b1_2_cv(x_)
        x_ = self.cv3_b1_2_bn(x_)
        x_ = self.cv3_b1_2_ac(x_)
        x = self.cv3_b1_add([x, x_])
        #convolution
        x = self.cv4_cv(x)
        x = self.cv4_bn(x)
        x = self.cv4_ac(x)
        #res block 2 1
        x_ = self.cv5_b1_1_cv(x)
        x_ = self.cv5_b1_1_bn(x_)
        x_ = self.cv5_b1_1_ac(x_)
        x_ = self.cv5_b1_2_cv(x_)
        x_ = self.cv5_b1_2_bn(x_)
        x_ = self.cv5_b1_2_ac(x_)
        x = self.cv5_b1_add([x, x_])
        #res block 2 2
        x_ = self.cv5_b2_1_cv(x)
        x_ = self.cv5_b2_1_bn(x_)
        x_ = self.cv5_b2_1_ac(x_)
        x_ = self.cv5_b2_2_cv(x_)
        x_ = self.cv5_b2_2_bn(x_)
        x_ = self.cv5_b2_2_ac(x_)
        x = self.cv5_b2_add([x, x_])
        #convolution
        x = self.cv6_cv(x)
        x = self.cv6_bn(x)
        x = self.cv6_ac(x)
        # res block 3 1
        x_ = self.cv7_b1_1_cv(x)
        x_ = self.cv7_b1_1_bn(x_)
        x_ = self.cv7_b1_1_ac(x_)
        x_ = self.cv7_b1_2_cv(x_)
        x_ = self.cv7_b1_2_bn(x_)
        x_ = self.cv7_b1_2_ac(x_)
        x = self.cv7_b1_add([x, x_])
        # res block 3 2
        x_ = self.cv7_b2_1_cv(x)
        x_ = self.cv7_b2_1_bn(x_)
        x_ = self.cv7_b2_1_ac(x_)
        x_ = self.cv7_b2_2_cv(x_)
        x_ = self.cv7_b2_2_bn(x_)
        x_ = self.cv7_b2_2_ac(x_)
        x = self.cv7_b2_add([x, x_])
        # res block 3 3
        x_ = self.cv7_b3_1_cv(x)
        x_ = self.cv7_b3_1_bn(x_)
        x_ = self.cv7_b3_1_ac(x_)
        x_ = self.cv7_b3_2_cv(x_)
        x_ = self.cv7_b3_2_bn(x_)
        x_ = self.cv7_b3_2_ac(x_)
        x = self.cv7_b3_add([x, x_])
        # res block 3 4
        x_ = self.cv7_b4_1_cv(x)
        x_ = self.cv7_b4_1_bn(x_)
        x_ = self.cv7_b4_1_ac(x_)
        x_ = self.cv7_b4_2_cv(x_)
        x_ = self.cv7_b4_2_bn(x_)
        x_ = self.cv7_b4_2_ac(x_)
        x = self.cv7_b4_add([x, x_])
        # res block 3 5
        x_ = self.cv7_b5_1_cv(x)
        x_ = self.cv7_b5_1_bn(x_)
        x_ = self.cv7_b5_1_ac(x_)
        x_ = self.cv7_b5_2_cv(x_)
        x_ = self.cv7_b5_2_bn(x_)
        x_ = self.cv7_b5_2_ac(x_)
        x = self.cv7_b5_add([x, x_])
        # res block 3 6
        x_ = self.cv7_b6_1_cv(x)
        x_ = self.cv7_b6_1_bn(x_)
        x_ = self.cv7_b6_1_ac(x_)
        x_ = self.cv7_b6_2_cv(x_)
        x_ = self.cv7_b6_2_bn(x_)
        x_ = self.cv7_b6_2_ac(x_)
        x = self.cv7_b6_add([x, x_])
        # res block 3 7
        x_ = self.cv7_b7_1_cv(x)
        x_ = self.cv7_b7_1_bn(x_)
        x_ = self.cv7_b7_1_ac(x_)
        x_ = self.cv7_b7_2_cv(x_)
        x_ = self.cv7_b7_2_bn(x_)
        x_ = self.cv7_b7_2_ac(x_)
        x = self.cv7_b7_add([x, x_])
        # res block 3 8
        x_ = self.cv7_b8_1_cv(x)
        x_ = self.cv7_b8_1_bn(x_)
        x_ = self.cv7_b8_1_ac(x_)
        x_ = self.cv7_b8_2_cv(x_)
        x_ = self.cv7_b8_2_bn(x_)
        x_ = self.cv7_b8_2_ac(x_)
        x = self.cv7_b8_add([x, x_])
        #convolution
        x = self.cv8_cv(x)
        x = self.cv8_bn(x)
        x = self.cv8_ac(x)
        # res block 4 1
        x_ = self.cv9_b1_1_cv(x)
        x_ = self.cv9_b1_1_bn(x_)
        x_ = self.cv9_b1_1_ac(x_)
        x_ = self.cv9_b1_2_cv(x_)
        x_ = self.cv9_b1_2_bn(x_)
        x_ = self.cv9_b1_2_ac(x_)
        x = self.cv9_b1_add([x, x_])
        # res block 4 2
        x_ = self.cv9_b2_1_cv(x)
        x_ = self.cv9_b2_1_bn(x_)
        x_ = self.cv9_b2_1_ac(x_)
        x_ = self.cv9_b2_2_cv(x_)
        x_ = self.cv9_b2_2_bn(x_)
        x_ = self.cv9_b2_2_ac(x_)
        x = self.cv9_b2_add([x, x_])
        # res block 4 3
        x_ = self.cv9_b3_1_cv(x)
        x_ = self.cv9_b3_1_bn(x_)
        x_ = self.cv9_b3_1_ac(x_)
        x_ = self.cv9_b3_2_cv(x_)
        x_ = self.cv9_b3_2_bn(x_)
        x_ = self.cv9_b3_2_ac(x_)
        x = self.cv9_b3_add([x, x_])
        # res block 4 4
        x_ = self.cv9_b4_1_cv(x)
        x_ = self.cv9_b4_1_bn(x_)
        x_ = self.cv9_b4_1_ac(x_)
        x_ = self.cv9_b4_2_cv(x_)
        x_ = self.cv9_b4_2_bn(x_)
        x_ = self.cv9_b4_2_ac(x_)
        x = self.cv9_b4_add([x, x_])
        # res block 4 5
        x_ = self.cv9_b5_1_cv(x)
        x_ = self.cv9_b5_1_bn(x_)
        x_ = self.cv9_b5_1_ac(x_)
        x_ = self.cv9_b5_2_cv(x_)
        x_ = self.cv9_b5_2_bn(x_)
        x_ = self.cv9_b5_2_ac(x_)
        x = self.cv9_b5_add([x, x_])
        # res block 4 6
        x_ = self.cv9_b6_1_cv(x)
        x_ = self.cv9_b6_1_bn(x_)
        x_ = self.cv9_b6_1_ac(x_)
        x_ = self.cv9_b6_2_cv(x_)
        x_ = self.cv9_b6_2_bn(x_)
        x_ = self.cv9_b6_2_ac(x_)
        x = self.cv9_b6_add([x, x_])
        # res block 4 7
        x_ = self.cv9_b7_1_cv(x)
        x_ = self.cv9_b7_1_bn(x_)
        x_ = self.cv9_b7_1_ac(x_)
        x_ = self.cv9_b7_2_cv(x_)
        x_ = self.cv9_b7_2_bn(x_)
        x_ = self.cv9_b7_2_ac(x_)
        x = self.cv9_b7_add([x, x_])
        # res block 4 8
        x_ = self.cv9_b8_1_cv(x)
        x_ = self.cv9_b8_1_bn(x_)
        x_ = self.cv9_b8_1_ac(x_)
        x_ = self.cv9_b8_2_cv(x_)
        x_ = self.cv9_b8_2_bn(x_)
        x_ = self.cv9_b8_2_ac(x_)
        x = self.cv9_b8_add([x, x_])
        #convolution
        x = self.cv10_cv(x)
        x = self.cv10_bn(x)
        x = self.cv10_ac(x)
        # res block 5 1
        x_ = self.cv11_b1_1_cv(x)
        x_ = self.cv11_b1_1_bn(x_)
        x_ = self.cv11_b1_1_ac(x_)
        x_ = self.cv11_b1_2_cv(x_)
        x_ = self.cv11_b1_2_bn(x_)
        x_ = self.cv11_b1_2_ac(x_)
        x = self.cv11_b1_add([x, x_])
        # res block 5 2
        x_ = self.cv11_b2_1_cv(x)
        x_ = self.cv11_b2_1_bn(x_)
        x_ = self.cv11_b2_1_ac(x_)
        x_ = self.cv11_b2_2_cv(x_)
        x_ = self.cv11_b2_2_bn(x_)
        x_ = self.cv11_b2_2_ac(x_)
        x = self.cv11_b2_add([x, x_])
        # res block 5 3
        x_ = self.cv11_b3_1_cv(x)
        x_ = self.cv11_b3_1_bn(x_)
        x_ = self.cv11_b3_1_ac(x_)
        x_ = self.cv11_b3_2_cv(x_)
        x_ = self.cv11_b3_2_bn(x_)
        x_ = self.cv11_b3_2_ac(x_)
        x = self.cv11_b3_add([x, x_])
        # res block 5 4
        x_ = self.cv11_b4_1_cv(x)
        x_ = self.cv11_b4_1_bn(x_)
        x_ = self.cv11_b4_1_ac(x_)
        x_ = self.cv11_b4_2_cv(x_)
        x_ = self.cv11_b4_2_bn(x_)
        x_ = self.cv11_b4_2_ac(x_)
        x = self.cv11_b4_add([x, x_])
        #
        x = self.avg_pool(x)
        output = self.dense(x)
        #
        return output
#%%