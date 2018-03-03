## 步骤
1. 下载数据
2. 压缩数据
3. 网络配置
3. 训练网络

### 1. 下载数据
```
./data/mnist/get_mnist.sh
```

* 问题
1. 执行 `./data/mnist/get_mnist.sh`下载数据的时候报错
    ```
    getting error /usr/bin/env: sh: No such file or directory when running command play
    ```
    * 解决方案：
        * 先执行 `dos2unix [filename]` 在下载数据
        * [reference](https://stackoverflow.com/questions/18172405/getting-error-usr-bin-env-sh-no-such-file-or-directory-when-running-command-p)
    * 原因说明
        * sh文件中可能存在window结尾符，需要转换成unix的
* 执行结果：
    * 会把数据下载到data/mnist下
    
    
### 2. 压缩数据到数据库
```
./examples/mnist/create_mnist.sh
```
* 说明：
    * 该脚本通过利用 `caffe-master/build/examples/mnist/convert_mnist_data.bin`工具
    * 将`mnist data`转换为`caffe`可以使用的`lmdb`文件格式
    
* 执行结果
    1. 在 `./examples/mnist/`下生成
        * mnist-train-lmdb
        * mnist-test-lmdb
        
### 3.训练网络
```
./examples/mnist/train_lenet.sh
```