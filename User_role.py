def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError(f"{user_type} is not allowed to"
                             "call this function")
    return wrapper


@is_admin
def show_customer_receipt(*args, **kwargs):
    print("Receipt details")


try:
    show_customer_receipt(user_type='admin')
except ValueError as e:
    print(e)

# show_customer_receipt(user_type='admin') - або викликати її так
