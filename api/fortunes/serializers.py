from apistar import typesystem


class FortuneSerializer(typesystem.Object):
    properties = {
        'uuid': typesystem.string(max_length=250),
        'message': typesystem.string(max_length=250),
    }
