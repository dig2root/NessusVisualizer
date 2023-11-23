class IComponent:

    def __init__(self, id: str):
        self.id = id
    
    def render(self):
        raise NotImplementedError("IComponent.render() is not implemented")

    def get_id(self):
        return self.id