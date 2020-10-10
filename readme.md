### caffe 特点

* caffe全称Convolutional Architecture for Fast Feature Embedding
* 开源，核心语言c++， 
* 提供完整的工具包,用来训练、测试、微调、部署模型
* 模块化
    * caffe设计之初就做到了尽可能的模块化。允许对数据格式、网络层和损失函数进行扩展。
* 表示和实现分离
    * caffe的模型定义是用 `Protocol Buffer`语言写进配置文件的，以任意有向无环的形式、caffe支持网络架构。
    * caffe会根据网络需要来正确占用内存。
    * 通过一个函数调用，实现`CPU`和`GPU`之间的切换

### caffe的架构

* 数据存储
    * caffe 通过 `Blobs`即以四维数组的方式存储和传递数据。`Blobs`提供了一个统一的内存接口，用于批量图像的操作和参数更新
    
### 安装
* 具体参见[ Installment/caffe.md ](https://github.com/jiye-ML/Installment/blob/master/caffe.md)
* `caffe` 编译完成后，会生成一个`build`目录,在该目录下有个`tools`，这里有可执行的文件`caffe`

### 一般步骤
1. 数据格式处理d
2. 编写网络结构文件 `.prototxt`在`Data`层中引入数据文件
3. 网络求解文件 'solver.prototxt'用 `net`配置网络结构文件
4. 训练网络
    ```
    ./build/tools/caffe train --solver=solver.prototxt 
    ```
### 生成 `prototxt`
* pycaffe


### 网络定义
* [参见说明](1.net_define.md)

### LeNet 模型
* [LeNet.md](2.LeNet.md)

### Reference

* [[Caffe]:关于caffe新手入门(http://blog.csdn.net/cham_3/article/details/72141753)
* [深度学习（六）caffe入门学习](http://blog.csdn.net/hjimce/article/details/48933813)
* [Caffe源码导读](https://ymgd.github.io/codereader/2016/10/20/caffe_sourcecode_analysis/)