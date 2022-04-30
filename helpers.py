

def createrare(id):
    x = randomgen(id)
    return createunit(name='Редкий слизнюк', id=-300, identeficator=x, weapon='sliznuk', hp=10, maxhp=10,
                      damagelimit=999)


def createlava(chatid, id='lava'):
    x = randomgen(chatid)
    text = 'Алмазный голем'
    hp = 4
    return createunit(id=id, weapon='lava', name=text, hp=hp, maxhp=hp, animal=None, identeficator=x, damagelimit=15)


def createpauk(id, hp):
    for ids in games:
        if id in games[ids]['bots']:
            id2 = games[ids]['chatid']
    x = randomgen(id2)
    t = users.find_one({'id': id})
    text = 'Паук[' + t['bot']['name'] + ']'
    return createunit(id=id, name=text, weapon='bite', hp=hp, maxhp=hp, damagelimit=7, identeficator=x)


def createdouble(id, ids):
    x = randomgen(id)
    text = 'Двойник[' + ids['name'] + ']'
    return createunit(id=ids['id'], name=text, weapon=ids['weapon'], hp=ids['hp'], maxhp=ids['hp'],
                      skills=ids['skills'], skin=ids['skin'],
                      damagelimit=ids['damagelimit'], energy=ids['maxenergy'], maxenergy=ids['maxenergy'],
                      identeficator=x, shockcd=0)


def createmonster(id, weapon, hp, animal):
    for ids in games:
        if id in games[ids]['bots']:
            id2 = games[ids]['chatid']
    x = randomgen(id2)
    t = users.find_one({'id': id})
    text = 'Кошмарное слияние[' + t['bot']['name'] + ']'
    return createunit(id=id, weapon=weapon, name=text, hp=hp, maxhp=hp, animal=animal, identeficator=x, damagelimit=2)


def createsniper(chatid, id='sniper'):
    x = randomgen(chatid)
    text = 'Зомби-снайпер'
    hp = 1
    return createunit(id=id, weapon='rifle', name=text, hp=hp, maxhp=hp, animal=None, identeficator=x, damagelimit=1,
                      zombie=6)


def createboss(chatid, id=441399484):
    x = id
    text = 'Повелитель печенья'
    hp = 13
    return createunit(id=id, weapon='cookie', name=text, hp=hp, maxhp=hp, animal=None, identeficator=None,
                      damagelimit=10,
                      skills=['cookiegolem', 'cookiegun', 'cookiecharge', 'cookieclone', 'trap'])


def randomgen(id):
    i = 0
    text = ''
    while i < 4:
        print('cycle')
        text += random.choice(symbollist)
        i += 1
    no = 0
    for ids in games[id]['bots']:
        try:
            if games[id]['bots']['identeficator'] == text:
                no = 1
        except:
            pass
    if no == 0:
        return text
    else:
        return randomgen(id)


def createzombie(id):
    for ids in games:
        if id in games[ids]['bots']:
            id2 = games[ids]['chatid']
    x = randomgen(id2)
    t = users.find_one({'id': id})
    text = 'Зомби[' + t['bot']['name'] + ']'
    return createunit(id=id, name=text, weapon='zombiebite', energy=20, maxenergy=20, zombie=6, hp=1, maxhp=1,
                      identeficator=x)

def createunit(id, name, weapon, hp=4, maxhp=4, skills=[], identeficator=None, maxenergy=5, energy=5, items=[],
               accuracy=0, damagelimit=6, skin=[], \
               animal=None, zombie=0, die=0, shockcd=0, strenght=1, oracle=1, drops=[]):
    return {identeficator: {'name': name,
                            'dopname': None,
                            'weapon': weapon,
                            'mutations': [],
                            'effects': [],
                            'msg': None,
                            'skills': skills,
                            'team': None,
                            'hp': hp,
                            'shockcd': shockcd,
                            'maxenergy': maxenergy,
                            'energy': energy,
                            'items': items,
                            'attack': 0,
                            'yvorot': 0,
                            'reload': 0,
                            'skill': 0,
                            'item': 0,
                            'miss': 0,
                            'shield': 0,
                            'stun': 0,
                            'takendmg': 0,
                            'die': die,
                            'yvorotkd': 0,
                            'id': id,
                            'blood': 0,
                            'bought': [],
                            'accuracy': accuracy,
                            'damagelimit': damagelimit,
                            'zombie': zombie,
                            'heal': 0,
                            'shieldgen': 0,
                            'skin': skin,
                            'oracle': oracle,
                            'target': None,
                            'exp': 0,
                            'gipnoz': 0,
                            'maxhp': hp,
                            'currentarmor': 0,
                            'armorturns': 0,
                            'boundwith': None,
                            'boundtime': 0,
                            'boundacted': 0,
                            'bowcharge': 0,
                            'mainitem': [],
                            'weapons': ['hand'],
                            'animal': animal,
                            'allrounddmg': 0,
                            'deffromgun': 0,
                            'dieturn': 0,
                            'magicshieldkd': 0,
                            'fire': 0,
                            'firearmor': 0,
                            'identeficator': identeficator,
                            'chance': 0,
                            'hit': 0,
                            'doptext': '',
                            'dopdmg': 0,
                            'blight': 0,
                            'reservenergy': 0,
                            'realid': None,
                            'strenght': strenght,
                            'drops': drops,
                            'firearmorkd': 0,
                            'mainskill': []
                            }
            }

def skintoname(x):
    try:
        if x[0] == 'oracle':
            return 'Оракул'
        if x[0] == 'robot':
            return 'Робот'
        if x[0] == 'oldman':
            return 'Мудрец'
    except:
        return 'ничего'


def weapontoname(x):
    if x == 'saw':
        return 'Пилострел'
    elif x == 'ak':
        return 'Пистолет'
    elif x == 'bow':
        return 'Лук'
    elif x == None:
        return 'Кулаки'
    elif x == 'rock':
        return 'Камень'
    elif x == 'chlen':
        return 'Флюгегенхаймен'
    elif x == 'hand':
        return 'Кулаки'
    elif x == 'kinzhal':
        return 'Кинжал'
    elif x == 'slizgun':
        return 'Слиземёт'
    elif x == 'emojthrow':
        return 'Эмоджимёт'


def infomenu(user):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('🐺Оборотень', callback_data='dna info werewolf'),
           types.InlineKeyboardButton(text='⚡️Электродемон', callback_data='dna info electro'))
    kb.add(types.InlineKeyboardButton('Назад', callback_data='dna back1'))
    bot.send_message(user['id'], 'Выберите мутацию для просмотра:', reply_markup=kb)


def dnamenu(user):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('🏢Строения', callback_data='dna buildings'),
           types.InlineKeyboardButton(text='Генерация 🧬ДНК', callback_data='dna buy'))
    kb.add(types.InlineKeyboardButton('📀Клонирование', callback_data='dna cloning'),
           types.InlineKeyboardButton('👨‍🔬Исследования', callback_data='dna research'))
    kb.add(types.InlineKeyboardButton('🧪Мутирование', callback_data='dna mutate'),
           types.InlineKeyboardButton('Инфа о мутациях', callback_data='dna info'))
    kb.add(types.InlineKeyboardButton('Закрыть меню', callback_data='close'))
    bot.send_message(user['id'], 'Выберите меню.', reply_markup=kb)


def buildmenu(user):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('🏭ДНК-генератор', callback_data='dna generator'),
           types.InlineKeyboardButton('📀Клонирователь', callback_data='dna cloner'))
    kb.add(types.InlineKeyboardButton('Назад', callback_data='dna back1'))
    kb.add(types.InlineKeyboardButton('Закрыть меню', callback_data='close'))
    bot.send_message(user['id'], 'Выберите строение.', reply_markup=kb)


def researchmenu(user):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('🔥⚡️Мутации', callback_data='dna mutations'))
    kb.add(types.InlineKeyboardButton('Назад', callback_data='dna back1'))
    kb.add(types.InlineKeyboardButton('Закрыть меню', callback_data='close'))
    bot.send_message(user['id'], 'Выберите меню.', reply_markup=kb)

