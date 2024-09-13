# Visual Contextual Classifier

## Install
To install the library run this command
```
pip install visual-contextual-classifier
```
## Usage
```python
from VisualContextualClassifier import VisualContextualClassifier
# Instantiate the object (will download model files on the first creation)
classifier=VisualContextualClassifier()
classifier.predict("The sentence you want to classify")
```

## Explanation
Artwork descriptions typically have two types of sentences, visual & contextual. A visual sentence will contain words and phrases that relate to or explain the visual content of the artwork. A contextual sentence will talk about the artpiece such as the artist, the time period, or the inspirations behind the work.
### Visual
```python
classifier.predict("A vast river is laid out with a deep blue hue")
```
```javascript
{'contextual': 0.005291305482387543, 'visual': 0.9947086572647095}
```
### Contextual
```python
classifier.predict("This was the last artpiece the artist ever produced, he died 14 days after finishing this piece")
```
```javascript
{'contextual': 0.9987691044807434, 'visual': 0.0012308646691963077}
```

