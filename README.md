
# ABOUT

- this PoC demonstrates how to use  [streamlit](https://streamlit.io/) library
- it was inspired by awesome example from [Dataprofessor](https://github.com/dataprofessor)

# how to run


 - create & activate new env
    ```
    python3 -m venv env & source env/bin/activate
    ```
 - install dependencies
    ```
    pip install -r requirements.txt
    ```     
 - run streamlit: streamlit 
    ```
    streamlit run main.py
    ```
 - !! or all-in-one command 
    ```
    python3 -m venv env && source env/bin/activate \
     && pip install -r requirements.txt \
     && streamlit run main.py
    ```

# 101
* prereqs on linux:
   
    ```
    sudo apt install python3.12-venv
    ```
* steps used to create/activate python venv
    ```
    python3 -m venv env
    source env/bin/activate
    pip install streamlit yfinance pandas
    pip freeze > requirements.txt
    deactivate

    ```