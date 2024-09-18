YOLOv8 sample implementation

### Installation

```
conda create -n YOLOv8 python=3.10 -y
conda activate YOLOv8

pip install ultralytics
```

Pip install the ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).


### Train

* Run `python src/train.py` for training


### Test

* Run `python src/test.py` for testing


### Dataset structure

    ├── dataset 
        ├── train
            ├── images
                ├── 2.jpg
                ├── 3.jpg
                ├── ...
            ├── labels
                ├── 2.txt
                ├── 3.txt
                ├── ...
        ├── val
            ├── images
                ├── 20.jpg
                ├── 30.jpg
                ├── ...
            ├── labels
                ├── 20.txt
                ├── 30.txt
                ├── ...
        ├── test
            ├── images
                ├── 200.jpg
                ├── 300.jpg
                ├── ...
            ├── labels
                ├── 200.txt
                ├── 300.txt
                ├── ...


#### Reference

* https://github.com/ultralytics/ultralytics