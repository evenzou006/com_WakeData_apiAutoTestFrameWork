import pytest
from common.logs import log_clean

log_clean()
pytest.main()
# os.system('allure generate ./result_data/ -o ./report/ --clean')