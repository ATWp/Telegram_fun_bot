from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from services.work_with_database import load_database

import random
from config import RESOURCE_FONT


class TransformImage:

    def __init__(self, image_name):
        self.image_name = image_name
        self.image = Image.open(image_name)
        self.drawing = ImageDraw.Draw(self.image)
        self.width_image, self.height_image = self.image.size
        self.size_symbols = int(self.height_image * 0.07)
        self.font = ImageFont.truetype(RESOURCE_FONT, self.size_symbols)
        self.colour_text = "white"
        self.phrase = ""
        self.data_random_phrase()
        self.transform_image_name = '{0[0]}/transform_{0[1]}'.format(self.image_name.split('/'))

    def divided_string(self):
        new_string = ''
        summary_word_length = 0
        list_split_string_to_words = self.phrase.split()
        max_new_string_size = self.width_image // self.size_symbols * 2
        good_divided_string = []
        for word in list_split_string_to_words:
            word = word.strip()
            if summary_word_length + len(word) > max_new_string_size:
                good_divided_string.append(new_string)
                new_string = word + ' '
                summary_word_length = len(word) + 1
            else:
                new_string += word + ' '
                summary_word_length += len(word) + 1
        if new_string != '':
            good_divided_string.append(new_string)

        return good_divided_string

    def draw_text_on_the_image(self, good_divided_string):
        step = self.size_symbols
        for list_item_number, item in enumerate(good_divided_string):
            width_phrase_in_list = self.drawing.textsize(item, font=self.font)[0]
            indent = (self.width_image - width_phrase_in_list) // 2
            pos = (indent, self.height_image * 2 / 3 + step * (list_item_number + 1))
            self.drawing.text(pos, item, fill=self.colour_text, font=self.font)

    def data_random_phrase(self):
        self.phrase = random.choice(load_database())

    def save_transform_image(self):
        self.image.save(self.transform_image_name)

    def transform_image(self):
        self.draw_text_on_the_image(self.divided_string())
        self.save_transform_image()
        return self.transform_image_name
