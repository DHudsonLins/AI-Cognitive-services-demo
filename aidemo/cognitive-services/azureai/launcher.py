"""Esse código é executado quando executa o script python, não mexer. Ele é apenas um pré-req
"""
import os
import sys
import types
try:
    from inspect import getfullargspec as get_arg_spec
except ImportError:
    from inspect import getargspec as get_arg_spec



class SubscriptionKeyError(Exception):
    pass


def iniciar_launcher(func, subscription_key):
    print(func.__doc__)
    func(subscription_key)
    print("\n\n")


def executar_launcher(module_globals, key_env_variable):
    try:
        subscription_key = sys.argv[1] if len(
            sys.argv) >= 2 else os.environ[key_env_variable]
    except KeyError:
        raise SubscriptionKeyError(
            "Missing {} env variable.".format(key_env_variable))

    for func in list(module_globals.values()):
        if not isinstance(func, types.FunctionType):
            continue
        args = get_arg_spec(func).args
        if 'subscription_key' in args:
            iniciar_launcher(func, subscription_key)
