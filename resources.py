import random

from aiogram import types

from locales_dict import LocalesDict
from models import PostMode

class QueryResults:
    def __init__(self, locales: LocalesDict):
        self.locales = locales

    def message_too_long(self, lang: str):
        message_content = types.InputTextMessageContent(self.locales[lang].too_long_message)
        return types.InlineQueryResultArticle(
            id = '1', title = self.locales[lang].too_long_title,
            input_message_content = message_content,
            description = self.locales[lang].too_long_description,
            thumb_url = 'https://i.imgur.com/xblMvAx.png')

    def mode_for(self, lang: str, post_id, body, scope_string):
        keyboard = types.InlineKeyboardMarkup(inline_keyboard =
            [[types.InlineKeyboardButton(self.locales[lang].view, callback_data = str(post_id) +
            ' ' + PostMode.parse_key(PostMode.FOR))]])
        message_content = types.InputTextMessageContent(self.locales[lang].for_message % scope_string)
        return types.InlineQueryResultArticle(
            id = str(PostMode.FOR), title = self.locales[lang].for_title % scope_string,
            input_message_content = message_content,
            reply_markup = keyboard,
            description = body,
            thumb_url = 'https://i.imgur.com/hHIkDSu.png')

    def mode_except(self, lang: str, post_id, body, scope_string):
        keyboard = types.InlineKeyboardMarkup(inline_keyboard =
            [[types.InlineKeyboardButton(self.locales[lang].view, callback_data = str(post_id) +
            ' ' + PostMode.parse_key(PostMode.EXCEPT))]])
        message_content = types.InputTextMessageContent(self.locales[lang].except_message % scope_string)
        return types.InlineQueryResultArticle(
            id = str(PostMode.EXCEPT), title = self.locales[lang].except_title % scope_string,
            input_message_content = message_content,
            reply_markup = keyboard,
            description = body,
            thumb_url = 'https://i.imgur.com/S6OZMHd.png')

    def mode_spoiler(self, lang: str, post_id, body):
        keyboard = types.InlineKeyboardMarkup(inline_keyboard =
            [[types.InlineKeyboardButton(self.locales[lang].view, callback_data = str(post_id) +
            ' ' + PostMode.parse_key(PostMode.SPOILER))]])
        message_content = types.InputTextMessageContent(self.locales[lang].spoiler_message)
        return types.InlineQueryResultArticle(
            id = str(PostMode.SPOILER), title = self.locales[lang].spoiler_title,
            input_message_content = message_content,
            reply_markup = keyboard,
            description = body,
            thumb_url = 'https://i.imgur.com/mS2ir0T.png')

class Keyboards:
    def info_keyboard(self):
        return types.InlineKeyboardMarkup(inline_keyboard=
             [[types.InlineKeyboardButton('🇧🇷 Português-BR',    url='https://teletype.in/@leviobrabo/pombomsgbot_pt'),
               types.InlineKeyboardButton('🇺🇸 English',    url='https://teletype.in/@leviobrabo/pombomsgbot_en')],
              [types.InlineKeyboardButton('🇷🇺 Русский',    url='https://teletype.in/@leviobrabo/pombomsgbot_ru'),
               types.InlineKeyboardButton('🇺🇦 Українська', url='https://teletype.in/@leviobrabo/pombomsgbot_ua')],
              [types.InlineKeyboardButton('🇮🇹 Italiano',   url='https://teletype.in/@leviobrabo/pombomsgbot_it'),
               types.InlineKeyboardButton('🇨🇿 Čeština',    url='https://teletype.in/@leviobrabo/pombomsgbot_cz')],
              [types.InlineKeyboardButton('🇪🇸 Español',    url='https://teletype.in/@leviobrabo/pombomsgbot_es'),
             types.InlineKeyboardButton('🇵🇱 Polski',     url='https://teletype.in/@leviobrabo/pombomsgbot_pl')]])


class Media:
    def group_greeting_sticker_id(self):
        return random.choice(('CAACAgEAAxkBAAISQWOC8VsrqyfpWlpii-alLy1_DUbUAAI2AgAC5b2wRNk2tzRjCpEeKwQ',
                              'CAACAgEAAxkBAAISQmOC8W08_Xbhp48ieLdp8EYyj27wAAKKAgACK_tIRbbur0yldiPDKwQ',
                              'CAACAgEAAxkBAAISQ2OC8Xi3K9ijOfd6S3p0z3rv0Z5SAAIeBQACHJoIRMdNoaZYgx2EKwQ'))

class Resources:
    def __init__(self, locales: LocalesDict):
        self.query_results = QueryResults(locales)
        self.keyboards = Keyboards()
        self.media = Media()
