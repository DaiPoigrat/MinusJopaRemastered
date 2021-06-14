from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import socket


class Test (App):
	def build(self):
		self.ready = False
		self.msg = ''
		self.shutdown = False
		self.join = False
		self.ip = TextInput(pos = (0, 0), multiline = False)
		self.host = socket.gethostbyname(socket.gethostname())
		self.port = 0
		self.adress = ''
		self.server = (self.adress, 9090)

		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind((self.host, self.port))
		self.s.setblocking(0)

		layout = BoxLayout(orientation = 'vertical', padding = [20], spacing = 5)
		layout.add_widget(self.ip)
		layout.add_widget(Button(text = 'Connect', on_press = self.client_on))
		layout.add_widget(Button(text = 'Disconnect', on_press = self.client_off))
		layout.add_widget(Button(text = 'Play', on_press = self.Click))
		layout.add_widget(Button(text = 'Pause', on_press = self.Click))
		layout.add_widget(Button(text = 'Next', on_press = self.Click))
		return layout


	def Click(self, instance):
		self.s.sendto((instance.text).encode("utf-8"), self.server)
		print(instance.text)


	def client_on(self, instance): #чисто на проверо4ку
		print(instance.text)
		self.adress = self.ip.text
		self.server = (str(self.adress), 9090)
		self.s.sendto(("connected").encode("utf-8"), self.server)


	def client_off(self, instance):
		print(instance.text)
		self.s.sendto(("disconnected").encode("utf-8"), self.server)
		self.s.close()


Test().run()
