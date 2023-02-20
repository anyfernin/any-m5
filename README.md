# Activate virtual env
source streamlit-env/bin/activate

# Run hello_world.py
streamlit run hello_world.py --server.enableCORS false --server.enableXsrfProtection false

# Run dataset.py
streamlit run dataset.py --server.enableCORS false --server.enableXsrfProtection false