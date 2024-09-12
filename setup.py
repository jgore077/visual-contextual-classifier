from distutils.core import setup
import setuptools

setup(name='Visual-Contextual Classifier',
      version='1.0',
      description='Predicts whether a sentence is a visual sentence or a contextual sentence',
      author='James Gore',
      author_email='james.gore@maine.edu',
      url='https://github.com/jgore077/visual-contextual-classifier/blob/main/README.md',
      install_requires=[
        'transformers>=4.44.2',
        'torch>=2.4.1',
        'requests>=2.32.3',
        'tqdm>=4.66.5'
      ],
      packages=setuptools.find_packages(),
     )