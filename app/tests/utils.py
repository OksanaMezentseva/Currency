def get_access_token(api_client):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    user = User.objects.create_user(
        username='testuser',
        email='test@gmail.com',
        password='password'
    )

    login_data = {
        'email': user.email,
        'password': 'password'
    }

    # authentication
    token_response = api_client.post('/api/token/', login_data)
    return token_response
