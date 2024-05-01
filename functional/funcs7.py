def cli(executable: str, **options: str):
    print(f'\n{executable = }\n{type(options)}\n{options = }')
    ...


cli('python', ENV='path_to_virtualenv_dir')

# executable = 'python'
# <class 'dict'>
# options = {'ENV': 'path_to_virtualenv_dir'}


args = {
    'executable': 'program',
    '--arg1': 100,
    '--arg2': 'mode'
}
cli(**args)

# executable = 'program'
# <class 'dict'>
# options = {'--arg1': 100, '--arg2': 'mode'}


def func(pos, /, pos_key, *args, key1, **kwargs, key2=...):
    print(
        f'{pos = }\n'
        f'{pos_key = }\n'
        f'{args = }\n'
        f'{key1 = }\n'
        f'{kwargs = }\n'
        f'{key2 = }'
    )
    ...

