#BY_Lursy>:)
from time import sleep

#Cores
Ve = '\033[1;31m' #Vermelho
Vd = '\033[1;32m' #Verde
Am = '\033[1;33m' #Amarelo
Az = '\033[1;34m' #Azul
Br = '\033[1;37m' #Branco

#Banner
L = f'''
{Vd}   _____                  _
  / ____|                | |
 | |        ___    _ __  | |  _   _  __  __
 | |       / _ \  | '__| | | | | | | \ \/ /
 | |____  | (_) | | |    | | | |_| |  >  <
  \_____|  \___/  |_|    |_|  \__,_| /_/\_\ \n\n'''

Op = f'''{Br}Cores:\n\n
___________
{Ve}"Vermelho"{Br}/_
{Vd}"Verde"    {Br}/
{Am}"Amarelo" {Br}/
{Az}"Azul"   {Br}/
{Br}________/\n\n {Am}//: {Br}'''

os.system('clear')
print(f'{L}')
cor = input(f'{Op}')

if cor == 'Vermelho' or cor == 'vermelho':
 os.chdir('/data/data/com.termux/files/home/Corlux/Bash/')
 os.system('cp Vermelho /data/data/com.termux/files/usr/etc/')
 os.chdir('/data/data/com.termux/files/usr/etc/')
 os.system('rm -rf bash.bashrc')
 os.system('mv Vermelho bash.bashrc')
 print(f'{Vd}Pronto! \n\n')
 print('Para salvar use o comando "exit" e volte ao terminal.')
elif cor == 'Verde' or cor == 'verde':
 os.chdir('/data/data/com.termux/files/home/Corlux/Bash/')
 os.system('cp Verde /data/data/com.termux/files/usr/etc/')
 os.chdir('/data/data/com.termux/files/usr/etc/')
 os.system('rm -rf bash.bashrc')
 os.system('mv Verde bash.bashrc')
 print(f'{Vd}Pronto! \n\n')
 print('Para salvar use o comando "exit" e volte ao terminal.')
elif cor == 'Amarelo' or cor == 'amarelo':
 os.chdir('/data/data/com.termux/files/home/Corlux/Bash/')
 os.system('cp Amarelo /data/data/com.termux/files/usr/etc/')
 os.chdir('/data/data/com.termux/files/usr/etc/')
 os.system('rm -rf bash.bashrc')
 os.system('mv Amarelo bash.bashrc')
 print(f'\n{Vd}Pronto! \n\n')
 print('Para salvar use o comando "exit" e volte ao terminal.')
elif cor == 'Azul' or cor == 'azul':
 os.chdir('/data/data/com.termux/files/home/Corlux/Bash/')
 os.system('cp Azul /data/data/com.termux/files/usr/etc/')
 os.chdir('/data/data/com.termux/files/usr/etc/')
 os.system('rm -rf bash.bashrc')
 os.system('mv Azul bash.bashrc')
 print(f'\n{Vd}Pronto! \n\n')
 print('Para salvar use o comando "exit" e volte ao terminal.')
else:
 os.system('clear')
 print(f'{L}')
 print(f'''{Br}Cores:\n\n
___________
{Ve}"Vermelho"{Br}/_
{Vd}"Verde"    {Br}/
{Am}"Amarelo" {Br}/
{Az}"Azul"   {Br}/
{Br}________/
\n {Am}//: {Ve}{cor}''')
 sleep(1)
 print('Comando não reconhecido.')
 sleep(2)
 os.system('python corlux.py')
