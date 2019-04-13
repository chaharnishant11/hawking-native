from audio_analyzer import AudioAnalyze
from sklearn import preprocessing
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


def predict(filename):
    with open('./Autism/model_autism.pkl', 'rb') as f:
        classifier = pickle.load(f)
    sc = StandardScaler()

    lab_enc = preprocessing.LabelEncoder()
    analyzed_audio = AudioAnalyze('./'+filename)

    check = analyzed_audio.slice_audio_parameters()
    check = sc.fit_transform(check)
    check = check.ravel()
    check = lab_enc.fit_transform(check)
    #y_train = lab_enc.fit_transform(y_train)
    check = np.reshape(check, (-1, 19))
    prediction = classifier.predict(check)
    print("Autism : ", prediction)
    return prediction

predict("cry1.wav")