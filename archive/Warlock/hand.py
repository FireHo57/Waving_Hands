class hand:

    def __init__(self,name="Hand"):
        self.name = name
        self.gestures=""
        self.current_gesture=""

    def get_current_gesture(self):
        return self.current_gesture

    def get_gestures(self,number_since_Last=0):
        return self.gestures[-number_since_Last:]

    def make_gesture(self,gesture):
        self.current_gesture=gesture
        self.gestures+=gesture