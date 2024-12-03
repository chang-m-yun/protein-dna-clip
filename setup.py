from setuptools import setup, find_packages

setup(
    name='protein-dna-clip',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[        
        "numpy >= 1.14.2",
        "scipy >= 1.0.0",
        "pandas >= 1.3.3",
        "torch >= 1.9.0",
        'pytorch-lightning',
        "pytables >= 3.6.1",
        "h5py >= 3.7.0",
        "tqdm >= 4.64.1",
        "seaborn >= 0.11.2",
        "biopython >= 1.79",
        "modisco-lite >= 2.0.0",
        "tangermeme >= 0.2.3"
    ],
)