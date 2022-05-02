# stop the build if there are Python syntax errors or undefined names
flake8 /usr/test --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 /usr/src--count --select=E9,F63,F7,F82 --show-source --statistics

# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 /usr/test --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 /usr/src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# run pytest
cd /usr
python -m pytest test/unittests