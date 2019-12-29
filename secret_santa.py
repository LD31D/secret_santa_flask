from random import choice


def return_santa_list(people_list):

	people_list = [human.replace("\r", "") for human in people_list if len(human.replace(" ", "")) != 0]

	print(people_list)

	if len(people_list) <= 1:
		return None

	if people_list != list(set(people_list)):
		return None

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