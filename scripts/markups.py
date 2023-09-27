from aiogram import types

menu = types.InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          types.InlineKeyboardButton(text="Формулы", callback_data='formulas')
                                      ]
                                  ])


formulas_list = types.InlineKeyboardMarkup(row_width=4,
                                           inline_keyboard=[
                                               [
                                                   types.InlineKeyboardButton(text='Закон кулона',
                                                                              callback_data='culon_law'),
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 2',
                                                                              callback_data='formula2'),
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 3',
                                                                              callback_data='formula3'),
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 4',
                                                                              callback_data='formula4')
                                               ],
                                               [
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 1',
                                                                              callback_data='formula1'),
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 2',
                                                                              callback_data='formula2'),
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 3',
                                                                              callback_data='formula3')
                                               ],
                                               [
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 1',
                                                                              callback_data='formula1'),
                                                   types.InlineKeyboardButton(text='ФОРМУЛА 2',
                                                                              callback_data='formula2')
                                               ],
                                               [
                                                   types.InlineKeyboardButton(text='Назад', callback_data='back')
                                               ]
                                           ])
