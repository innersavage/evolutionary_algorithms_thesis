from .mutationbase import MutationBase


class NoMutation(MutationBase):
    datatype = 'any'

    def mutate(self, population, **kwargs):
        return population
