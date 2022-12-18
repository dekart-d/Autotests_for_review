#метод для удаления лишних символов из значения с фронтенда для соответствия валидации
import re



def clear_validate(c):
      result = re.sub("[+() -]", "", c)
      return result






