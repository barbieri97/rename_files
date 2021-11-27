import subprocess

path = input('informe o caminho absoluto da pasta que desja formatar: ')

x = subprocess.run(['ls', path], capture_output=True, text=True)

x = x.stdout

x = x.split('\n')


lista = [y.lower().replace(' ', '_') for y in x if y != '']

for x, y in zip(x, lista):
    subprocess.run(['mv', path+'/'+x, path+'/'+y])
