import pyxel

class App(object):
	def __init__(self, x, y, caption, fps):
		print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
		self.pset_x = int(x / 2) - 50
		self.pset_y = int(y / 2)
		pyxel.init(x, y, caption = caption, fps = fps)
		pyxel.run(self.update, self.draw)

	def update(self):
		self.pset_x += 1
		print('updating...')

	def draw(self):
		pyxel.cls(0)
		pyxel.pset(self.pset_x, self.pset_y, 11)
		print('drawing...')

App(160,160,"Moving pixel", 5)
