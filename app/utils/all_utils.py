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
