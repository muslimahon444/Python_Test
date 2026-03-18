import logging 
logging.basicConfig(
    filename = 'app.log',
    level = logging.INFO,
    format = '%(asctime)s -%(levelname)s - %(message)s',
    encoding='utf-8'
)
def get_user():
    logging.info('Начилась опросник')
    try:
        age_in =input('Введиете ваш возраст ')
        age = int(age_in)
        logging.info (f'пользовотель вел возраст {age}')
        print(f'Спасибо ваш возраст: {age}')
    except ValueError:
        logging.error('Ошибка вы вели не число')
        print('Просим ввести только число ')
if __name__== '__main__':
    logging.info ('Программа заработала ')
    get_user()
    logging.info ('Программа удачно завершилось')
    
    
import unittest