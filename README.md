# Demon Overlord - A bot to supplement some cool functions

## The Directory Structure

```
/
+-- src
|   +-- commands            (everything to do with handling custom commands)
|   |   +-- __init__.py
|   |   +-- help.py         (module to handle the help command)
|   |   +-- ship.py         (handling everything to do with Izzy's ships)
|   |   \-- (more stuff)
|   +-- main.py             (main bot executable)
|   \-- misc.py             (miscellaneous functions to make main.py less crowded)
+-- Procfile                (the start script for heroku)
+-- requirements.txt        (the non-standard packages that are used)
+-- LICENSE                 (The License File)
\-- README.md               (the readme)
```

## How all this works
Every command gets its own file with the name of the command. Here's an example:

We want to create the command `test` what do we do?

1. create a file named `test.py` in `src/commands/`
2. create a function named `test_handler` that taked the following positional arguments in this order:
    ```
    bot      :: a reference to the bot
    message  :: a reference to the message being handled (for ease of use)
    command  :: the parsed command that is being handled.
    devRole  :: the developer role
    ```
3. import `test` in `src/commands/__init__.py` and add it to the `__all__` list 
3. add the command to the `handler` function in `src/misc.py`

that's it, everything inside your custom module is up to you. 
