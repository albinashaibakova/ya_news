import pytest

from django.test.client import Client

from news.models import News, Comment


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass

@pytest.fixture
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    return news

@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client

@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client

@pytest.fixture
def comment(author, news):
    comment = Comment.objects.create(
        news = news,
        text='Текст',
        author=author,
    )
    return comment

@pytest.fixture
def id_for_args(comment):
    return (comment.id,)