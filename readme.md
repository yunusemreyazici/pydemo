#### - first you must open terminal and type this command

```
xcode-select --install
```

#### - then you must install miniconda with this link
https://docs.conda.io/en/latest/miniconda.html

### - and u must create a new environment with this command

```
conda create -n yuem python -y
```

### - then you must activate the environment with this command

```
conda activate yuem
```

### - then you must install the requirements with this command

```
conda install scikit-learn
conda install pandas
conda install matplotlib
pip install jupyterlab
pip install pandas-datareader
pip install tqdm
pip install h5py 
pip install flask 
pip install boto3
```

### and lets install apple metal acceleration with this command

```
pip install tensorflow-macos
pip install tensorflow-metal
pip install bayesian-optimization
pip install gym 
pip install kaggle
```

## Accelerated PyTorch training on Mac installation

```
conda install pytorch torchvision torchaudio -c pytorch-nightly

pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

conda install -c apple tensorflow-deps

```
### - and finally you must run this command

```
conda install -y jupyter
conda install pandas-datareader   
conda install tqdm
conda install flask
conda install boto3
conda install pyyaml
pip install chardet

conda update -n base -c defaults conda

jupyter lab
```

