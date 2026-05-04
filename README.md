#To create python project
python -m uv init test_with_code_coverage

#To activate scripts
 python -m venv .venv
.venv\Scripts\activate

#pytest

pip install pytest pytest-cov

pytest
#For code coverge
pytest --cov=main --cov-report=html
