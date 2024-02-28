import commune as c

class Miner(c.Module):
    def __init__(self, module='model.openai', **kwargs):
        self.model = c.module(module)(**kwargs)
        print(self.model)

    def forward(self, text='Hello, world!', **kwargs):
        self.model.forward(text, **kwargs)
        
Miner.serve(remote=False)