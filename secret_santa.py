from random import choice


def return_santa_list(people_list):

	people_list = [human.replace("\r", "") for human in people_list if len(human.replace(" ", "")) != 0]

	print(people_list)

	if len(people_list) <= 1:
		print(1)
		return None

	if len(people_list) != len(set(people_list)):
		print(2)
		return None

	print(3)

	senders = []
	recipients = []

	for element in people_list:
		senders.append(element)
		recipients.append(element)

	print(senders)
	print(recipients)

	result = []

	for sender in senders:
		
		while True:
			recipient = choice(recipients)

			if recipient != sender:
				break

			else:
				continue

		couple = {
			'sender': sender,
			'recipient': recipient
		}

		result.append(couple)
		recipients.remove(recipient)

	print(people_list)

	return result