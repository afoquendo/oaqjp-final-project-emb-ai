"""
This module run unit tests on the emotion_detector function.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Class for emotion detector unit test.
    """
    def test_emotion_detector(self):
        """
        Function thar check correct dominant emotion for test texts.
        """
        # Test for joy
        response_1 = emotion_detector("I am glad this happened")
        self.assertEqual(response_1['dominant_emotion'], 'joy')

        # Test for anger
        response_2 = emotion_detector("I am really mad about this.")
        self.assertEqual(response_2['dominant_emotion'], 'anger')

        # Test for disgust
        response_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response_3['dominant_emotion'], 'disgust')

        # Test for sadness
        response_4 = emotion_detector("I am so sad about this")
        self.assertEqual(response_4['dominant_emotion'], 'sadness')

        # Test for fear
        response_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response_5['dominant_emotion'], 'fear')

unittest.main()
