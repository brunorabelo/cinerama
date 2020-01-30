from core.models import User


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze

def user_mary():
    mary = User.objects.create_user(
        username='mary',
        first_name='Mother',
        last_name='Mary',
        email='mary@example.com',
        password='mary',
    )
    return mary


