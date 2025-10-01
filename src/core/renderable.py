class Renderable:
    """Base class for anything that can be rendered."""
    def __init__(self, layer=0):
        self.layer = layer

    def draw(self, surface, camera_offset=(0, 0)):
        """This method should be overridden by subclasses."""
        raise NotImplementedError