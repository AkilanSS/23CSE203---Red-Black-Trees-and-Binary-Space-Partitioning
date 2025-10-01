class Renderer:
    """Manages and renders all renderable objects, handling camera and layers."""
    def __init__(self):
        self.objects = []
        self.camera_offset = [0, 0]

    def add(self, obj):
        """Add a renderable object to the list."""
        if obj not in self.objects:
            self.objects.append(obj)

    def remove(self, obj):
        """Remove a renderable object from the list."""
        if obj in self.objects:
            self.objects.remove(obj)

    def draw(self, surface):
        """Draw all objects, sorted by layer, with the camera offset."""
        # Sort objects by layer so they are drawn in the correct order.
        sorted_objects = sorted(self.objects, key=lambda o: o.layer)
        for obj in sorted_objects:
            obj.draw(surface, self.camera_offset)