text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = text.split()

new_text = []
for text in words:
    ing_text = text + "ing"
    ing_text2 = ing_text.replace(',ing', 'ing,')
    ing_text3 = ing_text2.replace('.ing', 'ing.')
    new_text.append(ing_text3)
print(' '.join(new_text))
