from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Why so quiet'
    elif 'hello' in lowered:
        return 'hi'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,100)}'