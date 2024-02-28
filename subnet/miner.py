import commune as c

class Miner(c.Module):
    def __init__(self, module='model.openai', **kwargs):
        self.model = c.module('model.openai')(**kwargs)

    def forward(self, text='Hello, world!', **kwargs):
        self.model.forward(text, **kwargs)
        
Miner.serve()