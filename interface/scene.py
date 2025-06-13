# Clase para crear un objeto Scene

# Clase Scene
class Scene(object):
    def __init__(self):
        self.next_scene = self

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

    def get_next_scene(self):
        return self.next_scene
