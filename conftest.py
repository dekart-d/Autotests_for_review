#Фикстура в которой передаётся значение сессии, что бы во время вызова её в тестах у нас не открывался браузер по новой, а продолжался тест после предыдущего
import pytest
from fixture.app import application




@pytest.fixture (scope="session")
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture











