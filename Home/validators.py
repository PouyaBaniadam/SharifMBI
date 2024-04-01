from django.core.exceptions import ValidationError


def max_size_validator(limit_in_mb):
    """
    Custom validator to restrict file size in megabytes.

    Args:
        limit_in_mb (int): The maximum allowed size of the file in megabytes.
    """
    limit = limit_in_mb * 1024 * 1024  # Convert MB to bytes

    def _validator(value):
        if value.size > limit:
            raise ValidationError(f'فایل باید کمتر از {limit_in_mb} مگابایت باشد.')

    return _validator
