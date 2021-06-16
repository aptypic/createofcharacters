from faker import Faker
import file_operations
import random
fake = Faker("ru_RU")
min_range = 3
max_range = 18
forms_count = 10
basic_abilities = [
    "Стремительный прыжок", "Электрический выстрел",
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


def create_runic_skills(basic_abilities):
    runic_skills = []
    for ability in basic_abilities:
        for letter in ability:
            ability = ability.replace(letter, letters_mapping[letter])
        runic_skills.append(ability)
    return runic_skills


def create_graphic_forms(min_range, max_range):
    runic_ability_1, runic_ability_2, runic_ability_3 = (
        random.sample(create_runic_skills(basic_abilities), 3)
    )
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randrange(min_range, max_range),
        "agility": random.randrange(min_range, max_range),
        "endurance": random.randrange(min_range, max_range),
        "intelligence": random.randrange(min_range, max_range),
        "luck": random.randrange(min_range, max_range),
        "skill_1": runic_ability_1,
        "skill_2": runic_ability_2,
        "skill_3": runic_ability_3,
    }
    return context


def generate_templates(forms_count):
    for graphic_forms in range(forms_count):
        file_operations.render_template(
            'src/graphic_form.svg',
            f'Ready_templates/template-{graphic_forms}.svg',
            create_graphic_forms(min_range, max_range))


def main():
    generate_templates(forms_count)


if __name__ == "__main__":
    main()
