import numpy as np
from sklearn.preprocessing import LabelEncoder

# Assuming `labels` is the list of your pill classes
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Save the classes
np.save('classes.npy', label_encoder.classes_)
