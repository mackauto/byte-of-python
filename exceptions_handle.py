#-*-coding:utf-8-*-

try:
    text = input('Enter somethin-->')
except EOFError:
    print('Why did you do an EOF on me ?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))