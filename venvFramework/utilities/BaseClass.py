import pytest

#Classe base para ser usada como herança nos testes
@pytest.mark.usefixtures('setBrowser')
class BaseClass:
    pass