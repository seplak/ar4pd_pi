# Raspberry Pi

This repository holds the code that is run on the Raspberry Pi.

## Set Up Python

Follow these directions to set up the Python envrionment so multiple Pi's can be worked on at once:

1. Run the following:

    $ sudo apt-get update && sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl openssl bzip2 pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev

2. Install pyenv:

    $ curl https://pyenv.run | bash

3. Add the following to your `~/.bashrc` file:


```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

4. Restart your shell:

    $ exec $SHELL

5. Install Python 3.6.0

    $ pyenv install 3.6.0

6. Create a new virtualenv

    $ pyenv virtualenv 3.6.0 capstone-3.6.0

7. Use the virtualenv:

    $ pyenv global capstone-3.6.0

8. Install pybluez

    $ pip install pybluez pybluez[ble]6. Create a new virtualenv

    $ pyenv virtualenv 3.6.0 capstone-3.6.0

7. Use the virtualenv:

    $ pyenv global capstone-3.6.0

8. Install pybluez

    $ pip install pybluez pybluez[ble]6. Create a new virtualenv

    $ pyenv virtualenv 3.6.0 capstone-3.6.0

7. Use the virtualenv:

    $ pyenv global capstone-3.6.0

8. Install pybluez

    $ pip install pybluez pybluez[ble]6. Create a new virtualenv

    $ pyenv virtualenv 3.6.0 capstone-3.6.0

7. Use the virtualenv:

    $ pyenv global capstone-3.6.0

8. Install pybluez

    $ pip install pybluez pybluez[ble]6. Create a new virtualenv

    $ pyenv virtualenv 3.6.0 capstone-3.6.0

7. Use the virtualenv:

    $ pyenv global capstone-3.6.0

8. Install pybluez

    $ pip install pybluez pybluez[ble]6. Create a new virtualenv

    $ pyenv virtualenv 3.6.0 capstone-3.6.0

7. Use the virtualenv:

    $ pyenv global capstone-3.6.0

At this point, you should now have a virtualenv set up with the minimum requirements. Ensure to capture any other necessary steps in this README.
