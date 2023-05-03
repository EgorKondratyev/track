import datetime
import requests


def get_tracks(shipped_from: datetime.date,
               shipped_to: datetime.date,
               starting_from: int = 0,
               end_before: int = 100):
    """
    Получение треков на основе только интервала дат (ОТ какой даты и ДО какой даты необходимо получить треки)
    :param shipped_from: ОТ
    :param shipped_to: ДО
    :param starting_from: Начиная с какого трека. Example: от 1 трека
    :param end_before: Заканчивая каким треком. Example: до 100 трека
    :return:
    """
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0I' \
              'joxNTE2MjM5MDIyfQ.QuvPiOzkYgLLFaz-dtjyrHHtHb3ES0LS22qkuQrGXqg'
    headers = {
        'X-API-Key': api_key
    }
    response_api = requests.get(url=f'https://postscraper.cfd/api/tracks?'
                                    f'skip={starting_from}&'
                                    f'limit={end_before}&'
                                    f'from_date={shipped_from}&'
                                    f'to_date={shipped_to}', headers=headers)
    if response_api.status_code == 200:
        return response_api.json()
