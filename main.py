from faker import Faker
import file_operations
import random

runic_skills = []
runic_abilities = ["Стремительный прыжок", "Электрический выстрел",
                   "Ледяной удар", "Стремительный удар", "Кислотный взгляд",
                   "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
letters_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
for ability in runic_abilities:
    runic_ability = ability
    for letter in ability:
        for key, value in letters_mapping.items():
            if letter == key:
                runic_ability = runic_ability.replace(letter, value)
    runic_skills.append(runic_ability)
fake = Faker("ru_RU")
for charsheet in range(1, 11):
    runic_ability_1, runic_ability_2, runic_ability_3 = (
        random.sample(runic_skills, 3)
    )
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randrange(8, 14, 1),
        "agility": random.randrange(8, 14, 1),
        "endurance": random.randrange(8, 14, 1),
        "intelligence": random.randrange(8, 14, 1),
        "luck": random.randrange(8, 14, 1),
        "skill_1": runic_ability_1,
        "skill_2": runic_ability_2,
        "skill_3": runic_ability_3,
    }
    file_operations.render_template('src/charsheet.svg',
                                    f'Ready_templates/template-{charsheet}.svg',
                                    context)
