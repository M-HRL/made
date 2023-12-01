from src.base.block import Block


class Pipeline(Block):
    def __init__(self):
        self._blocks: list[Block] = []

    def register(self, block: Block):
        self._blocks.append(block)
        return self

    def invoke(self, *args) -> tuple:
        for block in self._blocks:
            args = block.invoke(*args)
        return args
