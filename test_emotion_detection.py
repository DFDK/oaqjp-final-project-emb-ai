from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotions(self):
        assert emotion_detector("I am glad this happened")["dominat_emotion"] == "joy"
        assert emotion_detector("I am really mad about this")["dominat_emotion"] == "anger"
        assert emotion_detector("I feel disgusted just hearing about this")["dominat_emotion"] == "disgust"
        assert emotion_detector("I am so sad about this")["dominat_emotion"] == "sadness"
        assert emotion_detector("I am really afraid that this will happen")["dominat_emotion"] == "fear"

unittest.main()