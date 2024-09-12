

class Collider:
    def __init__(self, entity, x_offset, y_offset, width, height):
        self.entity = entity
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x = self.entity.x + self.x_offset
        self.y = self.entity.y + self.y_offset
        self.width = width
        self.height = height

    def collides(self, other: 'Collider') -> bool:
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)
    
    def update(self):
        self.x = self.entity.x + self.x_offset
        self.y = self.entity.y + self.y_offset
