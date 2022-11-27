from locales_dict import Locale, LocalesDict

locale_pt = Locale()
locale_ru = Locale()
locale_uk = Locale()
locale_de = Locale()
locale_it = Locale()

locales = LocalesDict({
    'pt': locale_pt,
    'ru': locale_ru,
    'uk': locale_uk,
    'de': locale_de,
    'it': locale_it
}, locale_pt)

# TOO_LONG_TITLE
locale_pt.too_long_title = '😮 sᴜᴀ ᴍᴇɴsᴀɢᴇᴍ ᴇ ᴍᴜɪᴛᴏ ʟᴏɴɢᴀ'
locale_ru.too_long_title = 'Слишком длинное сообщение'
locale_uk.too_long_title = 'Занадто довге повідомлення'
locale_de.too_long_title = 'Deine Nachricht ist zu lang'
locale_it.too_long_title = 'Il tuo messaggio è troppo lungo'

# FOR_TITLE
locale_pt.for_title = '💬 ᴇɴᴠɪᴀʀ ᴍᴇɴsᴀɢᴇᴍ ᴘᴀʀᴀ %s'
locale_ru.for_title = 'Для %s'
locale_uk.for_title = 'Для %s'
locale_de.for_title = 'Für %s'
locale_it.for_title = 'Per %s'

# EXCEPT_TITLE
locale_pt.except_title = '💬 ᴇɴᴠɪᴀʀ ᴍᴇɴsᴀɢᴇᴍ ᴘᴀʀᴀ ᴛᴏᴅᴏs, ᴍᴇɴᴏs %s'
locale_ru.except_title = 'Кроме %s'
locale_uk.except_title = 'Крім %s'
locale_de.except_title = 'Akzeptiere %s'
locale_it.except_title = 'Tranne %s'

# SPOILER_TITLE
locale_pt.spoiler_title = '✅ ʀᴇᴠᴇʟᴀʀ ᴍᴇɴsᴀɢᴇᴍ ᴘᴀʀᴀ ᴛᴏᴅᴏs'    
locale_ru.spoiler_title = 'Спойлер'
locale_uk.spoiler_title = 'Спойлер'
locale_de.spoiler_title = 'Spoiler'
locale_it.spoiler_title = 'Spoiler'

# TOO_LONG_MESSAGE
locale_pt.too_long_message = (
        '🛑🇲 🇪 🇳 🇸 🇦 🇬 🇪 🇲  🇱 🇴 🇳 🇬 🇦 🛑\n\n'
        '🥺 ᴅᴇsᴄᴜʟᴘᴇ, sᴜᴀ ᴍᴇɴsᴀɢᴇᴍ ɴᴀᴏ ᴘᴏᴅᴇ sᴇʀ ᴇɴᴠɪᴀᴅᴀ ' 
        'ᴘᴏʀǫᴜᴇ ᴇxᴄᴇᴅᴇ ᴏ ʟɪᴍɪᴛᴇ ᴅᴇ 200 ᴄᴀʀᴀᴄᴛᴇʀᴇs.')
locale_ru.too_long_message = '🥺 Ваше сообщение не может быть отправлено, так как его длина превышает лимит в 200 символов.'
locale_uk.too_long_message = '🥺 Ваше повідомлення не може бути відправлено, так як його довжина перевищує ліміт в 200 символів.'
locale_de.too_long_message = '🥺 Sorry, deine Nachricht kann nicht gesendet werden, da sie das Limit von 200 Zeichptüberschreitet.'
locale_it.too_long_message = '🥺 Mi dispiace, il tuo messaggio non può essere mandato, supera il limite di 200 caratteri.'

# FOR_MESSAGE
locale_pt.for_message = (
        '✉️🇲 🇪 🇳 🇸 🇦 🇬 🇪 🇲  🇸 🇪 🇨 🇷 🇪 🇹 🇦 ✉️\n\n'
        '🔍 ʟᴇᴍʙʀᴇ-sᴇ sᴏᴍᴇɴᴛᴇ ᴀ ᴘᴇssᴏᴀ ᴘᴀʀᴀ ǫᴜᴇᴍ ᴠᴏᴄᴇ ᴇɴᴠɪᴏᴜ '
        'ᴀ ᴍᴇɴsᴀɢᴇᴍ, ᴘᴏᴅᴇʀᴀ ʟᴇ-ʟᴀ.\n\n'
        '🔒 sᴇɢʀᴇᴅɪɴʜᴏ ᴘʀɪᴠᴀᴅᴏ ᴇɴᴠɪᴀᴅᴏ ᴄᴏᴍ sᴜᴄᴇssᴏ ᴘᴀʀᴀ %s.')
locale_ru.for_message = 'Приватное сообщение для %s.'
locale_uk.for_message = 'Приватне повідомлення для %s.'
locale_de.for_message = 'Private Nachricht für %s.'
locale_it.for_message = 'Messaggio privato per %s.'

# EXCEPT_MESSAGE
locale_pt.except_message = (
        '☢️🇲 🇪 🇳 🇸 🇦 🇬 🇪 🇲  🇸 🇪 🇱 🇪 🇹 🇮 🇻 🇦☢️\n\n'
        '💬 %s, ᴠᴏᴄᴇ ғᴏɪ ᴇxʟᴜɪᴅᴏ(ᴀ) ᴅᴇsᴛᴀ ᴍᴇɴsᴀɢᴇᴍ ᴘʀɪᴠᴀᴅᴀ.\n\n'
        '🔥 sᴇʀᴀ ǫᴜᴇ ᴇsᴛᴀᴏ ғᴀʟᴀɴᴅᴏ ᴍᴀʟ ᴅᴇ ᴛɪ?🤔')
locale_ru.except_message = 'Приватное сообщение для всех, кроме %s.'
locale_uk.except_message = 'Приватне повідомлення для всіх, крім %s.'
locale_de.except_message = 'Private Nachricht an alle außer %s.'
locale_it.except_message = 'Messaggio privato per tutti tranne %s.'

# SPOILER_MESSAGE
locale_pt.spoiler_message = (
        '📌🇲 🇪 🇳 🇸 🇦 🇬 🇪 🇲  🇵 🇺 🇧 🇱 🇮 🇨 🇦📌\n\n'
        '👥ᴍᴇɴsᴀɢᴇᴍ ᴇɴᴠɪᴀᴅᴀ ᴘᴀʀᴀ ᴛᴏᴅᴏs ᴅᴏ ɢʀᴜᴘᴏ.\n\n'
        '👀ᴀɢᴏʀᴀ ᴇ sᴜᴀ ᴏᴘᴏʀᴛᴜɴɪᴅᴀᴅᴇ, ᴄᴜʀɪᴏsᴏ(ᴀ) ᴅᴇ ᴘʟᴀɴᴛãᴏ!')
locale_ru.spoiler_message = 'Публичное сообщение под спойлером.'
locale_uk.spoiler_message = 'Публічне повідомлення під спойлером.'
locale_de.spoiler_message = 'Öffentlicher Spoiler für alle:'
locale_it.spoiler_message = 'Messaggio contenente spoiler.'

# GROUP_GREETING_MESSAGE
locale_pt.group_greeting_message = (
        '👋 Oi! 𝕆𝕚! 𝕄𝕖𝕦 𝕟𝕠𝕞𝕖 𝕖 %s 𝕖 𝕡𝕠𝕤𝕤𝕠 𝕒𝕛𝕦𝕕𝕒-𝕝𝕠 𝕒 𝕖𝕟𝕧𝕚𝕒𝕣 𝕞𝕖𝕟𝕤𝕒𝕘𝕖𝕟𝕤 𝕡𝕣𝕚𝕧𝕒𝕕𝕒𝕤 𝕢𝕦𝕖 𝕒𝕡𝕖𝕟𝕒𝕤 𝕒𝕝𝕘𝕦𝕞𝕒𝕤 𝕡𝕖𝕤𝕤𝕠𝕒𝕤 𝕡𝕠𝕕𝕖𝕞 𝕧𝕖𝕣. '
        'ℙ𝕒𝕣𝕒 𝕤𝕒𝕓𝕖𝕣 𝕞𝕒𝕚𝕤 𝕖𝕟𝕧𝕚𝕖 /start@%s 𝕖 𝕤𝕚𝕟𝕥𝕒-𝕤𝕖 à 𝕧𝕠𝕟𝕥𝕒𝕕𝕖 𝕡𝕒𝕣𝕒 𝕡𝕖𝕕𝕚𝕣 𝕒𝕛𝕦𝕕𝕒 𝕖𝕞 𝕟𝕠𝕤𝕤𝕠 '
        '<a href="t.me/lbrabo">𝕔𝕒𝕟𝕒𝕝 𝕕𝕖 𝕤𝕥𝕚𝕔𝕜𝕖𝕣𝕤</a> ℙ𝕠𝕕𝕖 𝕣𝕠𝕦𝕓𝕒𝕣 𝕢𝕦𝕒𝕟𝕥𝕒𝕤 𝕗𝕚𝕘𝕦𝕣𝕚𝕟𝕙𝕒𝕤 𝕢𝕦𝕚𝕤𝕖𝕣!')
locale_ru.group_greeting_message = (
        '👋 Привет! Меня зовут %s и я могу помочь вам отправлять сообщения, которые смогут прочитать только '
        'определённый круг лиц. Чтобы узнать больше отправьте команду /start@%s и не стесняйтесь просить о помощи '
        'в нашем <a href="t.me/lbrabo">стикер канала</a>, если у вас появятся какие-либо вопросы.')
locale_uk.group_greeting_message = (
        '👋 Привіт! Мене звуть %s і я можу допомогти вам відправляти повідомлення, які зможуть прочитати тільки '
        'певне коло осіб. Щоб дізнатися більше відправте команду /start@%s і не соромтеся просити про допомогу '
        'в нашому <a href="t.me/lbrabo">публічному чаті</a>, якщо у вас виникнуть будь-які питання.')
locale_de.group_greeting_message = (
        '👋 Hi! Mein Name ist %s und ich kann dir helfen, private Nachrichten zu verschicken, die nur bestimmte Personen sehen können. '
        'Um zu sehen, wie das geht, sende einfach /start@%s! Fühle dich frei, bei Fragen, in unserer '
        '<a href="t.me/lbrabo">Support Gruppe</a> zu fragen.')
locale_it.group_greeting_message = (
        '👋 Ciao! Il mio nome è %s E posso aiutarti ad inviare messaggi privati che solo alcuni possono vedere. '
        'per sapere di più invia /start@%s e sentiti libero di chiedere aiuto '
        '<a href="t.me/lbrabo">canale adesivo</a> se hai domande.')

# INFO_MESSAGE
locale_pt.info_message = (
        'sᴇ ᴠᴏᴄᴇ ᴀɪɴᴅᴀ ᴛɪᴠᴇʀ ᴅᴜᴠɪᴅᴀs ᴅᴇᴘᴏɪs ᴅᴇ ʟᴇʀ ᴏ ᴀʀᴛɪɢᴏ, ᴇɴᴛʀᴇ ᴇᴍ ᴄᴏɴᴛᴀᴛᴏ ᴄᴏᴍ ᴏ sᴜᴘᴏʀᴛᴇ ᴏᴜ sɪᴍᴘʟᴇsᴍᴇɴᴛᴇ ᴘᴇʀɢᴜɴᴛᴇ '
        'ᴘᴀʀᴀ ᴏʙᴛᴇʀ ᴀᴊᴜᴅᴀ ᴇᴍ ɴᴏssᴏ ʙᴀᴛᴇ-ᴘᴀᴘᴏ ᴘúʙʟɪᴄᴏ ᴀ ǫᴜᴀʟǫᴜᴇʀ ᴍᴏᴍᴇɴᴛᴏ.\n\n'
        '👥 ᴄᴀɴᴀʟ: @ʟʙʀᴀʙᴏ\n'
        '⚙ sᴜᴘᴏʀᴛᴇ: @ᴋʏʟᴏʀᴇɴsʙᴏᴛ')
locale_ru.info_message = (
        'Если у вас остались вопросы после прочтения статьи, вы можете в любое время обратиться в '
        'поддержку или попросить о помощи в нашем публичном чате.\n\n'
        '👥 Публичный чат: @ʟʙʀᴀʙᴏ\n'
        '⚙ Поддержка: @kylorensBot')
locale_uk.info_message = (
        'Якщо у вас залишилися питання після прочитання статті, ви можете в будь-який час звернутися в службу '
        'підтримки або попросити про допомогу в нашому публічному чаті.\n\n'
        '👥 Публічний чат: @ʟʙʀᴀʙᴏ\n'
        '⚙ Підтримка: @kylorensBot')
locale_de.info_message = (
        'Wenn du nach dem Lesen des Artikels noch Fragen hast, kannst du den Support kontaktieren oder einfach '
        'in unserem öffentlichen Chat um Hilfe bitten, wann immer du willst.\n\n'
        '👥 öffentlichen Chat: @ʟʙʀᴀʙᴏ\n'
        '⚙ Hilfe: @kylorensBot')
locale_it.info_message = (
         'Se hai ancora domande dopo aver letto questo articolo, puoi contattare il supporto nella nostra '
         'chat pubblica quando vuoi.\n\n'
         '👥 Gruppo pubblico: @ʟʙʀᴀʙᴏ\n'
         '⚙ Supporto: @kylorensBot')

# HOW_TO_USE
locale_pt.how_to_use = '🤖ᴄᴏᴍᴏ ᴜsᴀʀ ᴇsᴛᴇ ʙᴏᴛ?🤖'
locale_ru.how_to_use = 'Как пользоваться этим ботом?'
locale_uk.how_to_use = 'Як користуватися цим ботом?'
locale_de.how_to_use = 'Wie geht das?'
locale_it.how_to_use = 'Come usare questo bot?'

# TOO_LONG_DESCRIPTION
locale_pt.too_long_description = 'ʀᴇᴅᴜᴢᴀ ᴏ ᴛᴀᴍᴀɴʜᴏ ᴅᴀ sᴜᴀ ᴍᴇɴsᴀɢᴇᴍ ᴘᴀʀᴀ ǫᴜᴇ ɴᴀᴏ ᴇxᴄᴇᴅᴀ ᴏ ʟɪᴍɪᴛᴇ ᴅᴇ 200 ᴄᴀʀᴀᴄᴛᴇʀᴇs.🤏'
locale_ru.too_long_description = 'Пожалуйста, сократите длину вашего сообщения, чтобы она не превышала лимит в 200 символов.'
locale_uk.too_long_description = 'Будь ласка, скоротіть довжину Вашого повідомлення, щоб вона не перевищувала ліміт в 200 символів.'
locale_de.too_long_description = 'Bitte fasse dich etwas kürzer und überschreite das Limit von 200 Zeichen nicht.'
locale_it.too_long_description = 'Perfavore accorcia la lunghezza del tuo messaggio in modo che non superi i 200 caratteri.'

# NOT_ALLOWED
locale_pt.not_allowed = (
        '⚜️ᴠᴏᴄᴇ ᴇ ᴄᴜʀɪᴏsᴏ(ᴀ) ᴅᴇ ᴍᴀɪs ᴇɪɴ!⚜️\n\n'
        '⚠️ᴠᴏᴄê ɴãᴏ ᴛᴇᴍ ᴘᴇʀᴍɪssãᴏ ᴘᴀʀᴀ ᴠɪsᴜᴀʟɪᴢᴀʀ ᴇsᴛᴇ ᴄᴏɴᴛᴇᴜᴅᴏ⚠️')
locale_ru.not_allowed = 'Вам запрещено просматривать этот контент.'
locale_uk.not_allowed = 'Вам заборонено переглядати цей контент.'
locale_de.not_allowed = 'Dir ist nicht gestattet, diesen Inhalt zu lesen.'
locale_it.not_allowed = 'Non hai il permesso per vedere questo messaggio.'

# NOT_ACCESSIBLE
locale_pt.not_accessible = '⛔ᴇsᴛᴇ ᴄᴏɴᴛᴇúᴅᴏ ɴãᴏ ᴇsᴛᴀ ᴍᴀɪs ᴀᴄᴇssɪᴠᴇʟ⛔'
locale_ru.not_accessible = 'Этот контент больше недоступен.'
locale_uk.not_accessible = 'Цей контент більше недоступний.'
locale_de.not_accessible = 'Der Inhalt ist nicht mehr sichtbar.'
locale_it.not_accessible = 'Questo contenuto non è più accessibile.'

# VIEW
locale_pt.view = '⭐ 𝕍𝕖𝕣 ⭐'
locale_ru.view = 'Открыть'
locale_uk.view = 'Відкрити'
locale_de.view = 'Ansehen'
locale_it.view = 'Vedi'

# AND_CONNECTOR
locale_pt.and_connector = 'ᴇ'
locale_ru.and_connector = 'и'
locale_uk.and_connector = 'i'
locale_de.and_connector = '&'
locale_it.and_connector = 'e'
