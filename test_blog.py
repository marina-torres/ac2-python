import pytest
from unittest.mock import Mock, patch
from blog import Blog

api_response_4 = [
    {'userId': 7, 'id': 7, 'title': 'Último Titulo 1', 'body': 'Último Conteúdo do blog 1'},
    {'userId': 8, 'id': 8, 'title': 'Último Titulo 2', 'body': 'Último Teste de conteúdo do blog 2'}
]

@pytest.fixture
def mock_requests_get_4():
    with patch('blog.requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def blog_instance_4(mock_requests_get_4):
    mock_requests_get_4.return_value.json.return_value = api_response_4
    return Blog()

def test_posts_4(blog_instance_4):
    result = blog_instance_4.posts()
    assert result == api_response_4

def test_post_by_user_id_4(blog_instance_4, mock_requests_get_4):
    mock_requests_get_4.return_value.json.return_value = api_response_4[0]
    result = blog_instance_4.post_by_user_id(7)
    assert result == api_response_4[0]

