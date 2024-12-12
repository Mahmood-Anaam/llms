from setuptools import setup, find_packages


setup(
    name="llms",
    version="0.1.0",
    description="Arabic VQA",
    author="Mahmood Anaam",
    author_email="eng.mahmood.anaam@gmail.com",
    url="https://github.com/Mahmood-Anaam/llms",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    install_requires=[
        
        "torch>=1.13.1",
        "torchvision>=0.14.1",
        "transformers>=4.12.0",
        "pytorch-transformers>=1.2.0",
        "numpy>=1.23.5",
        "pandas>=1.1.5",
        "scipy>=1.5.4",
        "scikit-learn>=0.24.2",
        "opencv-python>=4.5.3",
        "Pillow>=8.3.2",
        "matplotlib>=3.4.3",
        "tqdm>=4.62.3",
        "anytree>=2.12.1",
        "yacs>=0.1.8",
        "pycocotools",
        "timm",
        "einops",
        "PyYAML>=5.4.1",
        "cython",
        "ninja",
        "clint>=0.5.1",
        "cityscapesScripts>=2.2.4",
        "h5py",
        "nltk",
        "joblib",
        "ipython",
        "ipykernel==5.5.6",

        ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

# Install the sub-package first


# restart_kernel()
