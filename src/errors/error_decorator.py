from src.errors.errors import ValidationError
from src.errors.error_messages import generic_error_message


def input_error(error_messages):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (IndexError, ValueError):
                return error_messages.get('FormatError') if 'FormatError' in error_messages else generic_error_message
            except KeyError:
                return error_messages.get('KeyError') if 'KeyError' in error_messages else generic_error_message
            except ValidationError:
                return error_messages.get('ValidationError') if 'ValidationError' in error_messages else generic_error_message
            except Exception as e:
                return generic_error_message
        return inner
    return decorator
