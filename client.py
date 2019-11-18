from transport import Transport

def main():
	
	transport = Transport()

	print("""
[*] Choose your option :

1) Change state
2) List vehicles in current state
3) Select next vehicle in current state
4) Quit (or Ctrl+C)
		""")
	while(True):
		try:
			i = int(input(">>> "))
			if i == 1:
				transport.toggle_wheels()
			elif i == 2:
				transport.listVehicles()
			elif i == 3:
				transport.selectNextVehicle()
			elif i == 4:
				print("[-] Exiting ...")
				break
			else:
				print("[-] Invalid option")
		except KeyboardInterrupt:
			print("\n[-] Exiting ...")
			break			

if __name__ == "__main__":
	main()	