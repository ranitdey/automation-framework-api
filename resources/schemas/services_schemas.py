

services_get_all_schema = {
    "type": "object",
    "required":
        [
            "total",
            "limit",
            "skip",
            "data"
        ],
    "properties":
        {
            "total":
                {
                    "type": "integer"
                },
            "limit":
                {
                    "type": "integer"
                },
            "skip":
                {
                    "type": "integer"
                },
            "data":
                {
                    "type": "array",
                    "items":
                        {
                            "type": "object",
                            "required":
                                [
                                    "id",
                                    "name",
                                    "createdAt",
                                    "updatedAt"
                                ],
                            "properties":
                                {
                                    "id":
                                        {
                                            "type": "integer"
                                        },
                                    "name":
                                        {
                                            "type": "string"
                                        },
                                    "createdAt":
                                        {
                                            "type": "string"
                                        },
                                    "updatedAt":
                                        {
                                            "type": "string"
                                        }
                                }
                        }
                }
        }
}

services_success_schema = {
    "type": "object",
    "required":
        [
            "id",
            "name",
            "updatedAt",
            "createdAt"
        ],
    "properties":
        {
            "id":
                {
                    "type": "integer",
                },
            "name":
                {
                    "type": "string"
                },
            "updatedAt":
                {
                    "type": "string"
                },
            "createdAt":
                {
                    "type": "string",
                }
        }
}

services_error_schema = {
    "type": "object",
    "required":
        [
            "name",
            "message",
            "code",
            "className",
            "errors"
        ],
    "properties":
        {
            "name":
                {
                    "type": "string"
                },
            "message":
                {
                    "type": "string"
                },
            "code":
                {
                    "type": "integer"
                },
            "className":
                {
                    "type": "string"
                },
            "errors":
                {
                    "type": "object"
                }
        }
}
