echo "BUILD STARTED..."

# Ensure pip is installed for Python 3.9
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip setuptools wheel

# Install requirements
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD ENDED..."