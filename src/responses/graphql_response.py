class GraphqlError:

    def __init__(self, message,):
        self.message = message
        self.success = False


class GraphqlMutationResponse:
    def __init__(self, message):
        self.message = message
        self.success = True
