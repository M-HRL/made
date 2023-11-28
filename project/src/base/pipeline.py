from src.base.block import Block


class Pipeline(Block):
    def __init__(self):
        self.blocks: list[Block] = []

    def register(self, block: Block):
        self.blocks.append(block)
        return self

    def invoke(self, *args) -> tuple:
        for block in self.blocks:
            args = block.invoke(*args)
        return args
