echo "BUILD START"
python3.12 -m pip install -r requirements.txt || { echo "pip install failed"; exit 1; }
python3.12 manage.py collectstatic --noinput --clear || { echo "collectstatic failed"; exit 1; }
echo "BUILD END"
