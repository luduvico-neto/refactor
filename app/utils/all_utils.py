class AllUtils:
    def __init__(self, field_name, field_value):
        self.field_name = field_name
        self.field_value = field_value

    @property
    def get_field_name(self):
        return self.field_name

    @property
    def get_field_value(self):
        return self.field_value

    def __str__(self):
        return f"{self.field_name}: {self.field_value}"


class SiengeGatewayUtils:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    @property
    def get_endpoint(self):
        return self.endpoint

    @property
    def get_api_key(self):
        return self.api_key

    def __str__(self):
        return f"SiengeGatewayUtils(endpoint={self.endpoint}, api_key={self.api_key})"

    def __int__(self):
        return hash((self.endpoint, self.api_key))

    def __eq__(self, other):
        if isinstance(other, SiengeGatewayUtils):
            return self.endpoint == other.endpoint and self.api_key == other.api_key
        return False

    def __hash__(self):
        return hash((self.endpoint, self.api_key))

    def __repr__(self):
        return f"SiengeGatewayUtils(endpoint={self.endpoint}, api_key={self.api_key})"

    def __getattr__(self, name):
        pass


class SiengeGatewayUtilsFactory:
    @staticmethod
    def create_sienge_gateway_utils(endpoint, api_key):
        return SiengeGatewayUtils(endpoint, api_key)


class AllUtilsFactory:
    @staticmethod
    def create_all_utils(field_name, field_value):
        return AllUtils(field_name, field_value)
